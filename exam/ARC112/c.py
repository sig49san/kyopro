import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def ST(): return sys.stdin.readline().rstrip()
def LST(): return list(sys.stdin.readline().rstrip().split())

N = I()
pv = LI()

hukasa = [0] * N
hukasa[0] = 1
for index,p in enumerate(pv):
    hukasa[index+1] = hukasa[p-1] + 1

print(hukasa)