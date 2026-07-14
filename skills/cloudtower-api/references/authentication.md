# Authentication

CloudTower uses a token as the API credential, sent as the `Authorization` header. `scripts/call.sh` adds the header automatically from `$CLOUDTOWER_TOKEN` or from its cached env file.

Ask the user for a token directly, or for the names of environment variables / config files that already hold their username and password. The user MUST NOT paste a password into the conversation — always work through environment variables they name. Equally, never print credentials yourself: don't `cat` or `echo` a file or variable containing a password or token.

## Token workflow

If a token is available (directly or via env), export it and call the API:

```bash
export CLOUDTOWER_ENDPOINT="https://tower.example.com"
export CLOUDTOWER_TOKEN="<token>"
```

## Username and password workflow

`scripts/call.sh login` exchanges credentials for a token and caches it in `/tmp/cloudtower.env` — nothing sensitive is printed, and later `call.sh` invocations read the cached token automatically even when each shell starts with a fresh environment:

```bash
export CLOUDTOWER_ENDPOINT="https://tower.example.com"
export CLOUDTOWER_USERNAME="$TOWER_USER"    # from the env vars the user named
export CLOUDTOWER_PASSWORD="$TOWER_PASS"
bash scripts/call.sh login
```

- `CLOUDTOWER_USER` is accepted as an alias for `CLOUDTOWER_USERNAME`; if the platform already sets these variables, just run `bash scripts/call.sh login`.
- Login `source` defaults to `LOCAL`; set `CLOUDTOWER_SOURCE` to another [UserSource](schemas/User/UserSource.md) value (`AUTHN`, `LDAP`, `SSO`) only when the user asks for it.

**References:**

- Resource: [User](resources/User.md)
- Operation: [Login](operations/Login.md)
- Request schema: [LoginInput](schemas/Login/LoginInput.md)
- Response schema: [WithTask_LoginResponse_](schemas/With/WithTask-LoginResponse.md)
- Data schema: [LoginResponse](schemas/Login/LoginResponse.md)
