import sys
from collections import defaultdict

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N,M = LI()
As = LI()
Bs = LI()
cds = [LI() for _ in range(M)]

class UnionFind:

    #節の数を引数にクラスを生成する
    def __init__(self, node):
        self.node = node
        self.par = [i for i in range(node+1)]
        self.size = [1 for _ in range(node+1)]

    def find(self, x):
        if(self.par[x] == x):
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return(self.par[x])

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if(x == y):
            return 0

        if(y > x): x, y = y, x
        self.par[x] = y
        self.size[y] = self.size[x] + self.size[y]
        self.size[x] = 0

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.node + 1):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

uf = UnionFind(N)

for c, d in cds:
    uf.unite(c, d)

for i in range(0,N):
    uf.find(i)

print(uf)
print(uf.par)
print(uf.size)
checker_1 = [0 for _ in range(N+1)]
checker_2 = [0 for _ in range(N+1)]

group = []

tmp = 0
for index, p in enumerate(uf.par):
    if(checker_1[p] == 0):
        checker_2[p] = tmp
        tmp += 1
        checker_1[p] = 1
        group.append([index])

    else:
        group[checker_2[p]].append(index)
    #print(checker_2)
    #print(group)

for group_s in group[1:]:
    sum_a = 0
    sum_b = 0

    for i in group_s:
        sum_a += As[i-1]
        sum_b += Bs[i-1]
        print(As[i-1], Bs[i-1])

    if(sum_a != sum_b):
        print("No")
        exit()

print("Yes")