# Secure Coding Labs

Practical examples of secure software development,
vulnerability prevention, security testing, and
code review.

## Objectives
- Apply secure coding principles.
- Identify and remediate common vulnerabilities.
- Practice OWASP-aligned security testing.
- Integrate security checks into development workflows.

## Languages
Python, PHP, Java, JavaScript

## Disclaimer
All demonstrations use authorized, controlled lab
environments and synthetic data.

This repository shows **insecure patterns as comments or clearly named anti-examples**, then the **secure implementation**, then a **test that the fix holds**. It does not include exploit payloads, attack scripts, or production application source.

## Layout

| Path | Topic |
|------|--------|
| `python/sql-injection-prevention/` | Parameterized queries (sqlite3) |
| `python/input-validation/` | Allow-lists and size limits |
| `python/password-security/` | PBKDF2 hashing, no reversible storage |
| `php/secure-database-queries/` | mysqli prepared statements |
| `php/xss-prevention/` | `htmlspecialchars` output encoding |
| `java/authentication/` | Session and password notes + sample verifier |
| `java/input-validation/` | Allow-list validation |
| `javascript/api-security/` | API input checks and safe JSON handling |
| `code-review/sample-security-review.md` | Review of a synthetic change |
| `security-testing/bandit/` | Bandit config for the Python labs |
| `security-testing/semgrep/` | Semgrep rule for string-built SQL |
| `docs/ssdlc-and-owasp.md` | SSDLC and OWASP Top 10 map |
| `docs/secure-coding-checklist.md` | Review checklist |

## How to run the Python labs

```bash
python python/sql-injection-prevention/test_secure_query.py
python python/input-validation/test_validate.py
python python/password-security/test_passwords.py
```

Lab data is local sqlite / in-memory only. No live databases.

## Author

Gitsimbanyi Prosper — Ag. Senior Manager, Cybersecurity & Compliance
