import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
As = LI()

ans = 0
for i in range(N):
    tmp = 10**6
    for j in range(i, N):
        tmp = min(tmp, As[j])
        ans = max(ans, tmp*(j-i+1))
        #print(ans)
print(ans)