# Sample secure code review (synthetic PR)

**Change:** “lookup user by username from a query parameter.”  
**Reviewer:** Gitsimbanyi Prosper  
**Verdict:** Request changes.

## Findings

| ID | Severity | Issue | Remediation in this repo |
|----|----------|--------|---------------------------|
| R-1 | High | SQL built with string format | `python/sql-injection-prevention` |
| R-2 | Medium | Username not allow-listed | `python/input-validation` |
| R-3 | Low | Password compared in plaintext in an older commit | `python/password-security` |

## What good looks like

```python
cur.execute("SELECT id FROM users WHERE username = ?", (username,))
```

Re-review after the parameterized query and allow-list are in place, with the unit tests green.
