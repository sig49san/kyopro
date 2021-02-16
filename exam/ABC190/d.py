import sys
import bisect

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
ruiseki = [0]

tmp = 0
ans = 0
for i in range(1,2*10**6+1):
    tmp += i
    tmp2 = N - tmp
    if(N - tmp < 0):
        break
    if tmp2 % i == 0:
        ans += 2
        #print(tmp2, i, tmp)
print(ans)
