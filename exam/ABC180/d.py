import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

X,Y,A,B = LI()

keikennti = 0

while X < B:
    X *= A
    if(X >= Y):
        print(keikennti)
        sys.exit()
    keikennti += 1
    #print(X, keikennti)

B_keiken = (Y - 1 - X) // B
print(B_keiken + keikennti)