import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    l = list(map(int,input().split()))
    out = 0
    if n >= 3:
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if l[i] != l[j] and l[j] != l[k] and l[i] != l[k]:
                        if l[i] + l[j] > l[k] and l[i] + l[k] > l[j] and l[k] + l[j] > l[i]:
                            out += 1
    print(out)


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
        input = """5
4 4 9 7 5"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
4 5 4 3 3 5"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
9 4 6 1 9 6 10 6 6 8"""
        output = """39"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2
1 1"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
