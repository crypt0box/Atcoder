def resolve():
    s = list(map(str, input()))
    cnt = 0
    ans = []
    for i in s:
        cnt += 1
        if cnt % 2 == 1:
            ans.append(i)
    print(''.join(ans))

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
        input = """atcoder"""
        output = """acdr"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """aaaa"""
        output = """aa"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """z"""
        output = """z"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """fukuokayamaguchi"""
        output = """fkoaaauh"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()