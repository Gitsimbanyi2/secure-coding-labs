# Semgrep (lab)

```bash
pip install semgrep
semgrep --config security-testing/semgrep/sql-concat.yaml python
```

The rule flags string-built SQL. The secure labs should produce **no** matches.
