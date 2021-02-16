import bisect,collections,copy,heapq,itertools,math,string
import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

Si = input()
T = input()

if(Si == "Y"):
    print(T.upper())

else:
    print(T)