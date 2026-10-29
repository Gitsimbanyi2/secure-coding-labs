# JavaScript — API security (lab)

- Authenticate the session, then authorize the resource.
- Validate types and ranges before hitting the database.
- JSON.parse only on trusted size-limited bodies.
- Do not reflect raw query strings into HTML (see PHP XSS lab for encoding).

`validateRequest.js` is framework-agnostic so it can sit in front of Express or a similar lab server.
