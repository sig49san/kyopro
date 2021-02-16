import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n,s,d = LI()
XYs = [LI() for _ in range(n)]

for x, y in XYs:
    if x < s and y > d:
        print("Yes")
        exit()

print("No")