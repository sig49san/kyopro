import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

A,B,C,D = LI()

if(A == B + C + D):
    print("Yes")
    exit()

if(B == A + C + D):
    print("Yes")
    exit()

if(C == B + A + D):
    print("Yes")
    exit()
if(D == B + C + A):
    print("Yes")
    exit()
if(A + B == C + D):
    print("Yes")
    exit()
if(A + C ==  B + D):
    print("Yes")
    exit()
if(A + D == B + C):
    print("Yes")
    exit()

print("No")
