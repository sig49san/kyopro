import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
xs = LI()

man, yuku, chebi = 0, 0,0 

for x in xs:
    man += abs(x)
    yuku += x**2
    chebi = max(chebi, abs(x))

print(man)
print(yuku**0.5)
print(chebi)