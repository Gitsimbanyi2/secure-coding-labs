import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from passwords import hash_password, verify_password


class TestPasswords(unittest.TestCase):
    def test_roundtrip(self):
        stored = hash_password("lab-correct-horse")
        self.assertTrue(verify_password("lab-correct-horse", stored))
        self.assertFalse(verify_password("wrong", stored))

    def test_unique_salts(self):
        a = hash_password("same-password")
        b = hash_password("same-password")
        self.assertNotEqual(a, b)

    def test_not_plaintext(self):
        stored = hash_password("lab-correct-horse")
        self.assertNotIn("lab-correct-horse", stored)


if __name__ == "__main__":
    unittest.main()
