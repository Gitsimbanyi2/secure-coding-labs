# Secure coding checklist (reviewers)

- [ ] Queries use bind parameters — no string-built SQL
- [ ] HTML/JS context encodes untrusted output
- [ ] Passwords hashed with a slow KDF (PBKDF2/bcrypt/argon2), unique salt
- [ ] Secrets not in source; no default passwords
- [ ] Authn then authz on every object (`user_id` from session, not from the body alone)
- [ ] Uploads: allow-list extension + MIME + size + stored outside web root under a random name
- [ ] API: schema validation, rate limit, HTTPS
- [ ] Session cookie: HttpOnly, Secure, SameSite
- [ ] Dependencies scanned; no known-critical CVEs left untracked
- [ ] SAST run on the PR (Bandit / Semgrep in this lab)
- [ ] Errors do not leak stack traces to the client
