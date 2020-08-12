import sys
from io import StringIO
import unittest


def resolve():
    s = list(input())
    for i in range(len(s)):
        if s[i] == '9':
            s[i] = '1'
        elif s[i] == '1':
            s[i] = '9'
    print(''.join(s))


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
        input = """119"""
        output = """991"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """999"""
        output = """111"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
