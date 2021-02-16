import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()

ABs = [LI() for _ in range(N)]

ans = 0
for A, B in ABs:
    ans += ((A + B) * (B-A+1)) // 2

print(ans)

