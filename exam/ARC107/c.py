import sys
import itertools
import math
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import defaultdict

class UnionFind:

    #節の数を引数にクラスを生成する
    def __init__(self, node):
        self.node = node
        self.par = [i for i in range(node)]
        self.size = [1 for _ in range(node)]

    #ノードxのrootを返却するメソッド
    #経路圧縮あり。
    def find(self, x):
        if(self.par[x] == x):
            return x
        else:
            self.par[x] = self.find(self.par[x]) #経路圧縮
            return(self.par[x])

    #ノードxとyが同じ木に含まれているか調査するメソッド
    def same(self, x, y):
        return self.find(x) == self.find(y)

    #ノードxとyを結合するメソッド
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
        for member in range(self.node):
            group_members[self.find(member)].append(member)
        return group_members

    #printメソッドで出力される内容の設定
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

N,K = LI()

aArray = [LI() for _ in range(N)]

row_list = []
col_list = []

for i, j in itertools.combinations(range(N), 2):
    tmp1 = 0
    tmp2 = 0
    tmp3 = 0
    tmp4 = 0
    if(i == j):
        continue
    
    for k in range(N):
        if(aArray[i][k] + aArray[j][k] <= K):
            tmp1 += 1

        if(aArray[k][i] + aArray[k][j] <= K):
            tmp3 +=1

        #同じ行があるかチェック
        if(aArray[i][k] == aArray[j][k]):
            tmp2 += 1

        if(aArray[k][i] == aArray[k][j]):
            tmp4 += 1
    
    if(tmp1 == N and tmp2 != N ):
        col_list.append((i, j))

    if(tmp3 == N and tmp4 != N ):
        row_list.append((i, j))

#print(row_list)
#print(col_list)

uf_row = UnionFind(N)
uf_col = UnionFind(N)

for i, j in row_list:
    #print(uf_row.par)
    uf_row.unite(i, j)

for i in range(N):
    uf_row.find(i)

for i, j in col_list:
    print(uf_col.par)
    uf_col.unite(i, j)

for i in range(N):
    uf_col.find(i)
print(uf_row)
print(uf_row.size)

row_com = 1
col_com = 1
for row in uf_row.size:
    if(row != 0):
        row_com *= math.factorial(row)

for col in uf_col.size:
    if(col != 0):
        row_com *= math.factorial(col)


print((row_com * col_com) % 998244353)
