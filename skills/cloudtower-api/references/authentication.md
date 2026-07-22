# Authentication

CloudTower uses a token as the API credential, sent as the `Authorization` header. `scripts/call.sh` adds the header automatically from `$CLOUDTOWER_TOKEN` or from its cached env file.

## Step 1 — discover existing credentials (always do this first)

Credentials are usually already present: platforms commonly inject `CLOUDTOWER_USERNAME` / `CLOUDTOWER_USER` and `CLOUDTOWER_PASSWORD`, and an earlier session may have cached a token in `/tmp/cloudtower.env` (which `call.sh` loads automatically). So simply:

```bash
export CLOUDTOWER_ENDPOINT="https://tower.example.com"
bash scripts/call.sh login
```

**The login command IS the credential check** — it knows every credential variable (`CLOUDTOWER_USERNAME`, the `CLOUDTOWER_USER` alias, the cached token) so run it directly instead of writing your own env inspection. When something is genuinely missing, its error message names the exact variable — that is the cue for step 2.

## Step 2 — only when discovery fails, ask the user

Ask for a token directly, or for the **names** of environment variables / config files that hold the username and password. The user MUST NOT paste a password into the conversation — work through variables they name. Equally, never print credentials yourself: don't `cat` or `echo` a file or variable containing a password or token.

```bash
export CLOUDTOWER_TOKEN="<token>"          # token route
# or, with the credential variables the user named:
export CLOUDTOWER_USERNAME="$TOWER_USER"
export CLOUDTOWER_PASSWORD="$TOWER_PASS"
bash scripts/call.sh login
```

- Login `source` defaults to `LOCAL`; set `CLOUDTOWER_SOURCE` to another [UserSource](schemas/User/UserSource.md) value (`AUTHN`, `LDAP`, `SSO`) only when the user asks for it.
- `call.sh login` caches the token in `/tmp/cloudtower.env` — later calls read it automatically even when each shell starts with a fresh environment.

**References:**

- Resource: [User](resources/User.md)
- Operation: [Login](operations/Login.md)
- Request schema: [LoginInput](schemas/Login/LoginInput.md)
- Response schema: [WithTask_LoginResponse_](schemas/With/WithTask-LoginResponse.md)
- Data schema: [LoginResponse](schemas/Login/LoginResponse.md)
