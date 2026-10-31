import tempfile
import unittest
from pathlib import Path

from file_organizer.organizer import organize_directory


class OrganizerTest(unittest.TestCase):

    def test_organizes_files_recursively(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)

            (root / "old_folder").mkdir()
            (root / "photo.jpg").write_text("image")
            (root / "old_folder" / "report.pdf").write_text("pdf")

            organize_directory(root)

            self.assertTrue((root / "images" / "photo.jpg").exists())
            self.assertTrue((root / "pdfs" / "report.pdf").exists())

    def test_does_not_overwrite_duplicate_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)

            (root / "old_folder").mkdir()
            (root / "images").mkdir()

            (root / "photo.jpg").write_text("new")
            (root / "old_folder" / "photo.jpg").write_text("old")

            organize_directory(root)

            self.assertTrue((root / "images" / "photo.jpg").exists())
            self.assertTrue((root / "images" / "photo_1.jpg").exists())

    def test_dry_run_does_not_move_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "photo.jpg"
            source.write_text("image")

            organize_directory(root, dry_run=True)

            self.assertTrue(source.exists())
            self.assertFalse((root / "images").exists())


if __name__ == "__main__":
    unittest.main()