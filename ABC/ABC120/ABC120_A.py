import sys
from io import StringIO
import unittest

def resolve():
    a, b, c = map(int, input().split())
    print(min(b//a, c))

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
        input = """2 11 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 9 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 1 10"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
