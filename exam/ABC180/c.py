#import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys

def I(): return int(sys.stdin.readline().rstrip())
#def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
#def S(): return sys.stdin.readline().rstrip()
#def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

yakusuu  = make_divisors(N)

for ans in yakusuu:
    print(ans)