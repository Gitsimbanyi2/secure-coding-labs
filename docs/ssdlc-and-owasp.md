# SSDLC and OWASP Top 10 (lab map)

## Secure SDLC (high level)

1. **Requirements** — authn/z, data class, logging, crypto.
2. **Design** — threat model the trust boundaries (browser, API, DB).
3. **Implement** — parameterized queries, encoding, hashed secrets.
4. **Verify** — unit tests of the *secure* behaviour, SAST, dependency scan.
5. **Release / operate** — secrets in a vault, least privilege, patch.

Security is a gate in each phase, not a pentest the week before go-live.

## OWASP Top 10 mapped to this repo

| OWASP class | Lab |
|-------------|-----|
| A03 Injection | `python/sql-injection-prevention`, `php/secure-database-queries` |
| A03 XSS (injection into HTML) | `php/xss-prevention`, `javascript/api-security` |
| A07 Identification and authentication | `python/password-security`, `java/authentication` |
| A01 Broken access control | `javascript/api-security` (object-level notes) |
| A02 Cryptographic failures | `python/password-security` |
| A04 Insecure design | `docs/secure-coding-checklist.md` |
| A05 Security misconfiguration | `security-testing/` |
| A06 Vulnerable components | dependency scan note in `security-testing/bandit/` |
| A08 Data integrity | checksum / review in `code-review/` |
| A10 SSRF | checklist item only (no live callbacks) |

Do not treat this table as a full OWASP training course. Use it as a map to the labs.
