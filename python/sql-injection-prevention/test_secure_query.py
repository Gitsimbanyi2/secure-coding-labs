"""Prove quotes in input do not break the query (secure behaviour)."""
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from secure_query import connect, find_user


class TestSecureQuery(unittest.TestCase):
    def setUp(self):
        self.conn = connect()

    def test_known_user(self):
        row = find_user(self.conn, "labuser")
        self.assertIsNotNone(row)
        self.assertEqual(row[1], "labuser")

    def test_quote_in_username_does_not_error(self):
        row = find_user(self.conn, "labuser' OR username IS NOT NULL --")
        self.assertIsNone(row)

    def test_display_apostrophe_roundtrip(self):
        self.conn.execute(
            "INSERT INTO users (username, display) VALUES (?, ?)",
            ("obrien", "O'Brien"),
        )
        row = find_user(self.conn, "obrien")
        self.assertEqual(row[2], "O'Brien")


if __name__ == "__main__":
    unittest.main()
