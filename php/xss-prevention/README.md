# PHP — XSS prevention

Untrusted data in HTML must be encoded for that context (`htmlspecialchars` for element text/attributes). Encoding is not a substitute for Content-Security-Policy, but it is the default output rule.

Do not store a “test XSS string” in this repo. The unit of proof is: encoded output contains `&lt;` when the input contained `<`.
