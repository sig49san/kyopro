import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
As = LI()
Bs = LI()

ans = [0]

a_max = 0
b_max = 0

for a, b in zip(As, Bs):
    temp = 0
    ans.append(max(ans[-1], a_max * b, a*b))

    a_max = max(a_max, a)
    b_max = max(b_max, b)
    temp+=1

for word in ans[1:]:
    print(word)