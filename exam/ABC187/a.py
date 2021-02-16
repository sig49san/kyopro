import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

A,B = LS()

sumA = 0
sumB = 0
for a in A:
    sumA += int(a)

for b in B:
    sumB += int(b)

print(max(sumA,sumB))