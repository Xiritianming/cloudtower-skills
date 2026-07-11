# Authentication

CloudTower uses a token as the API credential, sent as the `Authorization` header. `scripts/call.sh` adds the header automatically from `$CLOUDTOWER_TOKEN`.

Ask the user for a token directly, or for the names of environment variables / config files that already hold their username and password. The user MUST NOT paste a password into the conversation — always work through environment variables they name.

## Token workflow

If a token is available (directly or via env), export it and call the API:

```bash
export CLOUDTOWER_ENDPOINT="https://tower.example.com"
export CLOUDTOWER_TOKEN="<token>"
```

## Username and password workflow

Call [Login](operations/Login.md) to obtain a token (`/v2/api/login` needs no `Authorization` header, so `call.sh` works before `CLOUDTOWER_TOKEN` is set). With credentials in env vars the user named (here `$TOWER_USER` / `$TOWER_PASS`):

```bash
jq -n --arg u "$TOWER_USER" --arg p "$TOWER_PASS" \
  '{username: $u, password: $p, source: "LOCAL"}' > /tmp/login.json
bash scripts/call.sh /v2/api/login /tmp/login.json
export CLOUDTOWER_TOKEN=$(jq -r '.data.token' /tmp/tower_*.json | tail -1)
```

- `source` uses enum [UserSource](schemas/User/UserSource.md): `AUTHN`, `LDAP`, `LOCAL`, `SSO`. Use `LOCAL` unless the user explicitly requests another source.
- The exact response file path is printed by `call.sh`; prefer it over the glob above when extracting the token.

**References:**

- Resource: [User](resources/User.md)
- Operation: [Login](operations/Login.md)
- Request schema: [LoginInput](schemas/Login/LoginInput.md)
- Response schema: [WithTask_LoginResponse_](schemas/With/WithTask-LoginResponse.md)
- Data schema: [LoginResponse](schemas/Login/LoginResponse.md)
