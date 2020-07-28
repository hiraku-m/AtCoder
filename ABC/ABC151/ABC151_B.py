import sys
from io import StringIO
import unittest

def resolve():
    n, k, m = map(int, input().split())
    a = sum(map(int, input().split()))
    s = n*m - a
    if s > k:
        print(-1)
    elif s < 0:
        print(0)
    else:
        print(s)


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
        input = """5 10 7
8 10 3 6"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 100 60
100 100 100"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 100 60
0 0 0"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
