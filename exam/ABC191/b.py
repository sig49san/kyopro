import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N,X = LI()
As = LI()

ans = []

for A in As:
    if(A != X):
        ans.append(str(A))

ans = " ".join(ans)
print(ans)