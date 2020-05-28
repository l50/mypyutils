import unittest
import platform
import subprocess
from mypyutils import sysutils

class SysUtilsTests(unittest.TestCase):
    def test_chomp(self):
        test_str = 'blablabla\r\n'
        self.assertEqual(sysutils.chomp(test_str), 'blablabla')
    
    def test_run_cmd(self):
        cmd = 'uname'
        self.assertEqual(sysutils.chomp(sysutils.run_cmd(cmd)), platform.system())
