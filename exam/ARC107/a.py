import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

A, B, C = LI()

Asum = A * (A +1) // 2
Bsum = B * (B +1) // 2
Csum = C * (C +1) // 2

ans = (Asum * Bsum * Csum) % 998244353

print(ans)