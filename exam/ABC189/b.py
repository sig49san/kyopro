import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, X = LI()

VPs = [LI() for _ in range(N)]

alc = 0
for index, VP in enumerate(VPs):
    alc += VP[0] * VP[1]
    if alc > X * 100:
        print(index+1)
        exit()

print(-1)
