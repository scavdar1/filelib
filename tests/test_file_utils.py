import unittest
import os
from myfilelib.file_utils import get_files

class TestFileUtils(unittest.TestCase):
    def test_get_files_returns_list(self):
        # Dosya dizini kim olursa olsun doğru çalışması için geçici bir dizin kullanmak iyi bir fikirdir.
        directory = "/path/to/existing/directory"
        files = get_files(directory)
        self.assertIsInstance(files, list)

    def test_get_files_filter_extension(self):
        import tempfile

        with tempfile.TemporaryDirectory() as temp_dir:
            # Geçici dizinde bazı örnek dosyalar oluşturun
            open(os.path.join(temp_dir, 'test.txt'), 'a').close()
            open(os.path.join(temp_dir, 'test.jpg'), 'a').close()
            open(os.path.join(temp_dir, 'test.pdf'), 'a').close()

            # Sadece .txt dosyalarını filtreleyerek bir kontrol yap
            files = get_files(temp_dir, extension_filter=".txt")
            self.assertEqual(len(files), 1)
            self.assertTrue(files[0].endswith("test.txt"))

if __name__ == '__main__':
    unittest.main()

