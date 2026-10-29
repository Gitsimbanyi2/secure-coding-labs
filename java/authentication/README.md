# Java — authentication notes (lab)

- Identify the user (password / SSO), then **authorize** the object (`accountId` from the session).
- Session cookie: `HttpOnly`, `Secure`, `SameSite=Lax` or `Strict`.
- Invalidate the session on logout and on password change.
- Store PBKDF2/bcrypt/argon2 hashes only (`PasswordVerifier.java`).

This folder is not a complete Spring Security app.
