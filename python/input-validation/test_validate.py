import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate import username_ok, upload_ok


class TestValidate(unittest.TestCase):
    def test_username_allow(self):
        self.assertTrue(username_ok("lab_user-01"))

    def test_username_reject_space_and_short(self):
        self.assertFalse(username_ok("ab"))
        self.assertFalse(username_ok("lab user"))

    def test_upload_allow_pdf(self):
        self.assertTrue(upload_ok("report.pdf", 100))

    def test_upload_reject_path_and_exe(self):
        self.assertFalse(upload_ok("../x.pdf", 100))
        self.assertFalse(upload_ok("tool.exe", 100))
        self.assertFalse(upload_ok("ok.pdf", 9_000_000))


if __name__ == "__main__":
    unittest.main()
