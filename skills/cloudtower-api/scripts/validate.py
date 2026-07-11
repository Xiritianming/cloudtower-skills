#!/usr/bin/env python3
"""Validate a CloudTower API request body against the bundled OpenAPI spec.

Usage: validate.py <OperationId|path> <body.json>
  OperationId  e.g. CreateVm, or the request path e.g. /v2/api/create-vm

Prints OK and exits 0 when the body matches the operation's request schema.
Otherwise prints one error per line (with a JSON path) and exits 1.

Checks: required fields, unknown fields (with did-you-mean suggestions),
types, and enum membership. Stdlib only.
"""
import difflib
import json
import os
import sys

SPEC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references", "openapi.json")
API_PREFIX = "/v2/api"

TYPE_CHECKS = {
    "string": lambda v: isinstance(v, str),
    "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
    "number": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
    "boolean": lambda v: isinstance(v, bool),
    "object": lambda v: isinstance(v, dict),
    "array": lambda v: isinstance(v, list),
}


def deref(spec, schema):
    while isinstance(schema, dict) and "$ref" in schema:
        name = schema["$ref"].rsplit("/", 1)[-1]
        schema = spec["components"]["schemas"].get(name, {})
    return schema or {}


def merge_allof(spec, schema):
    """Flatten allOf into a single object schema (properties/required union)."""
    schema = deref(spec, schema)
    if "allOf" not in schema:
        return schema
    merged = {k: v for k, v in schema.items() if k != "allOf"}
    props, required = dict(merged.get("properties", {})), list(merged.get("required", []))
    for part in schema["allOf"]:
        part = merge_allof(spec, part)
        props.update(part.get("properties", {}))
        required += [r for r in part.get("required", []) if r not in required]
        merged.setdefault("type", part.get("type"))
    if props:
        merged["properties"] = props
    if required:
        merged["required"] = required
    return merged


def validate(spec, schema, value, path, errors):
    schema = merge_allof(spec, schema)

    variants = schema.get("oneOf") or schema.get("anyOf")
    if variants:
        best = None
        for variant in variants:
            attempt = []
            validate(spec, variant, value, path, attempt)
            if not attempt:
                return
            if best is None or len(attempt) < len(best):
                best = attempt
        errors.extend(best or [])
        return

    if value is None:
        if not schema.get("nullable"):
            errors.append(f"{path}: null is not allowed here")
        return

    if "enum" in schema:
        if value not in schema["enum"]:
            allowed = ", ".join(repr(v) for v in schema["enum"][:20])
            errors.append(f"{path}: {value!r} is not one of the allowed values [{allowed}]")
        return

    stype = schema.get("type") or ("object" if "properties" in schema else None)
    if stype and not TYPE_CHECKS.get(stype, lambda v: True)(value):
        errors.append(f"{path}: expected {stype}, got {type(value).__name__}")
        return

    if stype == "object":
        props = schema.get("properties", {})
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}.{key}: missing required field")
        additional = schema.get("additionalProperties")
        for key, item in value.items():
            if key in props:
                validate(spec, props[key], item, f"{path}.{key}", errors)
            elif props and not additional:
                # The spec never sets additionalProperties, so unknown keys are
                # treated as errors: an invented field name is the failure this
                # validator exists to catch.
                hint = difflib.get_close_matches(key, props.keys(), n=1)
                suggest = f" (did you mean `{hint[0]}`?)" if hint else ""
                errors.append(f"{path}.{key}: unknown field{suggest}")
            elif isinstance(additional, dict):
                validate(spec, additional, item, f"{path}.{key}", errors)
    elif stype == "array":
        for i, item in enumerate(value):
            validate(spec, schema.get("items", {}), item, f"{path}[{i}]", errors)


def find_operation(spec, key):
    want_path = key if key.startswith("/") else None
    if want_path and want_path.startswith(API_PREFIX):
        want_path = want_path[len(API_PREFIX):]
    for spec_path, item in spec.get("paths", {}).items():
        for method, op in item.items():
            if not isinstance(op, dict):
                continue
            if want_path == spec_path or (not want_path and op.get("operationId", "").lower() == key.lower()):
                return op
    return None


def main():
    if len(sys.argv) != 3:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    op_key, body_path = sys.argv[1], sys.argv[2]

    with open(SPEC_PATH) as f:
        spec = json.load(f)
    op = find_operation(spec, op_key)
    if op is None:
        print(f"operation not found: {op_key} (use the Operation ID or the request path)", file=sys.stderr)
        return 2

    request_body = op.get("requestBody", {})
    if "$ref" in request_body:
        name = request_body["$ref"].rsplit("/", 1)[-1]
        request_body = spec["components"].get("requestBodies", {}).get(name, {})
    schema = request_body.get("content", {}).get("application/json", {}).get("schema")
    if schema is None:
        print(f"{op_key} has no application/json request body; nothing to validate")
        return 0

    try:
        with open(body_path) as f:
            body = json.load(f)
    except json.JSONDecodeError as e:
        print(f"{body_path} is not valid JSON: {e}", file=sys.stderr)
        return 1

    errors = []
    validate(spec, schema, body, "body", errors)
    if errors:
        for err in errors:
            print(err)
        print(f"FAIL: {len(errors)} error(s); fix them and re-run")
        return 1
    print(f"OK: body matches the {op.get('operationId', op_key)} request schema")
    return 0


if __name__ == "__main__":
    sys.exit(main())
