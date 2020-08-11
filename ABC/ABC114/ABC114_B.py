import sys
from io import StringIO
import unittest


def resolve():
    s = input()
    a = 753
    for i in range(len(s)-2):
        b = abs(int(s[i:i+3]) - 753)
        if b < a:
            a = b
    print(a)


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
        input = """1234567876"""
        output = """34"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """35753"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1111111111"""
        output = """642"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
