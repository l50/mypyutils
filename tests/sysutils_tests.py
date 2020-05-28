import unittest
import platform
from mypyutils import sysutils

__auth__ = 'jayson.e.grace@gmail.com'


class SysUtilsTests(unittest.TestCase):
    def test_run_cmd(self):
        cmd = 'uname'
        self.assertEqual(sysutils.run_cmd(cmd).strip(), platform.system())
