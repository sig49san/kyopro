import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

a, b, x, y = LI()

if a == b:
    print(x)
    exit()

if a < b:
    print(min(2*x, y) * (b - a) + x)
    exit()

if a > b:
    print(min(2*x, y) * (a - b - 1) + x)