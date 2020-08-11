import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    s = 0
    for _ in range(n):
        x, u = input().split()
        if u == 'BTC':
            s += float(x) * 380000
        else:
            s += float(x) * 1
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
        input = """2
10000 JPY
0.10000000 BTC"""
        output = """48000.0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
100000000 JPY
100.00000000 BTC
0.00000001 BTC"""
        output = """138000000.0038"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
