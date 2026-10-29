"""Allow-list validation. Reject anything not in the contract."""
import re

USERNAME = re.compile(r"^[a-z0-9._-]{3,32}$")
MAX_UPLOAD_BYTES = 1_048_576
ALLOWED_EXT = {".png", ".jpg", ".pdf"}


def username_ok(value: str) -> bool:
    return bool(USERNAME.fullmatch(value or ""))


def upload_ok(filename: str, size: int) -> bool:
    if size < 1 or size > MAX_UPLOAD_BYTES:
        return False
    name = filename.lower()
    return any(name.endswith(ext) for ext in ALLOWED_EXT) and ".." not in name and "/" not in name and "\\" not in name
