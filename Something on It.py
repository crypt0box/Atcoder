def resolve():
    s = list(str(input()))
    cnt = 0
    if s[0] == 'o':
        cnt += 1
    if s[1] == 'o':
        cnt += 1
    if s[2] == 'o':
        cnt += 1
    print(700+cnt*100)

import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """oxo"""
        output = """900"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """ooo"""
        output = """1000"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """xxx"""
        output = """700"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()