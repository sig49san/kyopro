import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def ST(): return sys.stdin.readline().rstrip()
def LST(): return list(sys.stdin.readline().rstrip().split())

B, C = LI()

if(B > 0 ):
    if(C >= 2 * B):
        print(2*B + max(C-1, 1))
        exit()
    else:
        print(1 + max(C-1, 0) + max(C-1, 1))
        exit()
else:
    if(C >= 2*abs(B)+1):
        print(2*abs(B) + C)
        exit()
    else:
        print(max(C-2, 0) + C)
        exit()
