import sys
import bisect
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N , C = LI()


imosu = [0]
imosu_zahyou = [0, 10**9 + 1]

imosu_ = [[0, 0], [10**9+1, 0]]

for _ in range(N):
    a,b, c = LI()
    imosu_.append([a, c])
    imosu_.append([b+1, -c])

imosu_ = sorted(imosu_)

#print(imosu_)
"""
for _ in range(N):
    a, b, c = LI()
    bi = bisect.bisect_right(imosu_zahyou, a)
    imosu.insert(bi, c)
    imosu_zahyou.insert(bi, a)

    bi2 = bisect.bisect_right(imosu_zahyou, b+1)

    imosu.insert(bi2, -c)
    imosu_zahyou.insert(bi2, b+1)
"""


ans = 0
tmp = 0
for index, value in enumerate(imosu_[:-1]):
    tmp += value[1]
    daikin = min(tmp, C)
    ans += (imosu_[index+1][0] - imosu_[index][0]) * daikin
    #print(ans)

print(ans)
