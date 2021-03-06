def resolve():
    s = list(str(input()))
    print(s[0]+str(len(s)-2)+s[-1])

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
        input = """internationalization"""
        output = """i18n"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """smiles"""
        output = """s4s"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """xyz"""
        output = """x1z"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()