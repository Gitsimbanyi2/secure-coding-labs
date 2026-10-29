/**
 * Lab API guard: allow-list fields, integer bounds, caller id from session not from body.
 * Insecure: trust req.body.userId for an account lookup.
 */
function requireSessionUser(req) {
  if (!req.session || !req.session.userId) {
    const err = new Error("unauthorized");
    err.status = 401;
    throw err;
  }
  return req.session.userId;
}

function parseAmount(raw) {
  const n = Number(raw);
  if (!Number.isInteger(n) || n < 1 || n > 1_000_000) {
    const err = new Error("invalid amount");
    err.status = 400;
    throw err;
  }
  return n;
}

module.exports = { requireSessionUser, parseAmount };
