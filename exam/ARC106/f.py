import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

X, K, D = LI()

if abs(X) >= D * K:
    print(abs(X) - D * K)
    exit()

checker = X // D

if (K - checker) % 2 == 0:
    print(X % D)

else:
    print(abs(X % D - D))