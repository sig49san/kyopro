import sys
import collections

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()

ABs = [LI() for _ in range(N-1)]

pathList = [[] for _ in range(N+1)]
for AB in ABs:
    pathList[AB[1]].append(AB[0])
    pathList[AB[0]].append(AB[1])
#print(ABs)
#print(pathList)

Q = I()
point = [0 for _ in range(N+1)]

for i in range(Q):
    t,e,x = LI()
    e = e - 1
    if(t == 1):
        start = ABs[e][0]
        ikidomari = ABs[e][1]
    else:
        start = ABs[e][1]
        ikidomari = ABs[e][0]

    deq = collections.deque(pathList[start])
    point[start] += x
    checker = [0 for _ in range(N+1)]
    checker[start] = 1
    while len(deq) != 0:
        genzaiti = deq.popleft()
        #print(genzaiti)
        if genzaiti == ikidomari:
            continue
        if checker[genzaiti] == 1:
            continue

        point[genzaiti] += x
        checker[genzaiti] = 1
        for path in pathList[genzaiti]:
            deq.append(path)

for ans in point[1:]:
    print(ans)