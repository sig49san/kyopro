import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, K = LI()

checker = [i for i in range(1, 2*N+1)]

ans = 0
for ab in range(2, 2* N + 1):
    cd  = ab - K
    if(2 <= cd <= 2*N):
        ans += min(ab-1, 2*N+1-ab) * min(cd - 1, 2*N+1-cd)
    #print(ans)

print(ans)