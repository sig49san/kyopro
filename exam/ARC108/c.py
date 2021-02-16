import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N,M = LI()

rinsetu_list = [[] for _ in range(N+10)]
for _ in range(M):
    u, v, c = LI()
    rinsetu_list[u].append([v, c])
    rinsetu_list[v].append([u, c])


ans = [0 for _ in range(N+1)]


def dfs(i):
    for rinsetu in rinsetu_list[i]:
        if(ans[rinsetu[0]] != 0):
            continue

        if rinsetu[1] != ans[i]:
            ans[rinsetu[0]] = rinsetu[1]
            dfs(rinsetu[0])
        elif rinsetu[1] == 1:
            ans[rinsetu[0]] = 1
            dfs(rinsetu[0])
        
        else:
            ans[rinsetu[0]] = 2
            dfs(rinsetu[0])

ans[1] = 1
dfs(1)


for i in ans[1:]:
    print(i)