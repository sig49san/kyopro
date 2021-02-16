import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def ST(): return sys.stdin.readline().rstrip()
def LST(): return list(sys.stdin.readline().rstrip().split())

T = I()
for _ in range(T):
    L,R = LI()

    tmp = R - L

    if(tmp < L):
        print(0)
        continue

    tmp = tmp - L + 1
    print(tmp * (tmp + 1) // 2)
        