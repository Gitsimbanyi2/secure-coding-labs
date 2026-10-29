# Bandit (SAST for Python)

```bash
pip install bandit
bandit -r python
```

Use this on the **secure** helpers. Dependency scanning (pip-audit / npm audit / OWASP DC) is a separate pipeline step — do not commit lockfiles with known-critical CVEs untracked.
