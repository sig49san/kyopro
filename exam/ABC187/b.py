import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
XYs = [LI() for _ in range(N)]

#print(XYs)

ans = 0
for i in range(N):
    for j in range(i+1,N):
        if(XYs[j][0] == XYs[i][0]):
            continue

        dif = (XYs[j][1] - XYs[i][1]) / (XYs[j][0] - XYs[i][0])
        if -1 <= dif  <= 1:
            ans += 1

print(ans)