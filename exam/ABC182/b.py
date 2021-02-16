import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
As = LI()

ans = 0
warikireru = [0 for _ in range(1001)]

for i in range(2, max(As)+1):
    for A in As:
        if(A % i == 0):
            warikireru[i] += 1
        

#print(warikireru[:max(As)+1])

tmp = 0
ans = 0
for i, num in enumerate(warikireru):
    if num > tmp:
        tmp = num
        ans = i

print(ans)