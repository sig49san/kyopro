import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N,K = LI()
As = LI()

backet = [0 for _ in range(N+1)]

for a in As:
    backet[a] += 1

#print(backet)

kazu = [[] for _ in range(N+1)]

for index,num in enumerate(backet):
    kazu[num].append(index)

kazu[0].append(max(As)+1)
#print(kazu)
ans = 0

tmp = kazu[0][0]
ans += tmp

for i in range(1,K):
    if(len(kazu[i]) != 0):
        tmp = min(tmp, kazu[i][0])
    
    ans += tmp

    if(tmp == 0):
        break

print(ans)