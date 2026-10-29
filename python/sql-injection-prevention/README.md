# SQL injection prevention (Python)

**Insecure pattern:** build SQL with f-strings or `%` formatting of request data.

**Secure pattern:** pass a tuple of values to `cursor.execute(sql, params)` so the driver sends data separately from the statement.

The unit test uses a username that *looks* like a classic injection string. The secure helper must return `None` (no row), not every user in the table.
