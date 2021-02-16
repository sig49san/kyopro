import sys
import itertools

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N,M = LI()
ABs = [LI() for _ in range(M)]
K = I()
CDs = [LI() for _ in range(K)]


kumi = itertools.product([0,1], repeat=K)

ans = 0
for kumiawase in kumi:
    checker = [0] * 110
    
    for index, num in enumerate(kumiawase):
        #print(CDs)
        checker[CDs[index][num]] += 1
        #print(checker)
    
    tmp = 0
    for a, b in ABs:
        if checker[a] > 0 and checker[b] > 0:
            tmp += 1
    
    ans = max(ans, tmp)

print(ans)
