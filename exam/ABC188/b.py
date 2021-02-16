import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()

As = LI()
Bs = LI()

naiseki = 0
for A, B in zip(As, Bs):
    naiseki += (A*B)

if naiseki == 0:
    print("Yes")

else:
    print("No")