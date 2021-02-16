import sys
import math
import decimal

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n = I()


k = str((1 + 4 * (2*n+2)) ** decimal.Decimal("0.5") - 1)
k = decimal.Decimal(k) // 2

print(n + 1 - k)


#for i in range(1,n+1, 10000000000000000):
#    print(i, int((-1 + math.sqrt(1 + 4 * (2*i+2))) // 2))