import sys
import bisect

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, M = LI()
Hs = LI()
Ws = LI()

Hs.sort()

sabun = [Hs[0]]
for index,H in enumerate(Hs[1:]):
    sabun.append(H - Hs[index])

sabun = sabun[1:]
kisuu = [sabun[0]]
guusuu = [sabun[1]]


for index, H in enumerate(sabun[2:]):
    if index % 2 == 0:
        kisuu.append(kisuu[-1] + H)
    
    else:
        guusuu.append(guusuu[-1] + H)

print(kisuu)
print(guusuu)

ans = 10**10
for W in Ws:
    tmp = 0
    iti = bisect.bisect_left(Hs, W)
    print(iti)

    if(iti == 0):
        tmp = Hs[0] - W + guusuu[-1]
        ans = min(ans, tmp)
        continue

    if(iti == N):
        tmp = kisuu[-1] + W - Hs[-1]
        ans = min(ans, tmp)
        continue

    if(iti % 2 == 1):
        checker = iti // 2


