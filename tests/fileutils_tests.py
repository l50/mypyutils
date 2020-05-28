import unittest
import platform
import os
from mypyutils import fileutils

__auth__ = 'jayson.e.grace@gmail.com'


class FileUtilsTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        # Create test file
        os.system('echo "user1\nuser2\nuser3\nuser4\nuser5" > /tmp/test.txt')

    def test_file_exists(self):
        self.assertEqual(fileutils.file_exists('/tmp/test.txt'), True)
        self.assertEqual(fileutils.file_exists('/tmp/test2.txt'), False)

    def test_file_to_list(self):
        self.assertEqual(fileutils.file_to_list('/tmp/test.txt'),
                         ['user1\n', 'user2\n', 'user3\n', 'user4\n', 'user5\n'])

    @classmethod
    def tearDown(self):
        # Remove test file
        os.remove('/tmp/test.txt')
