import bisect,collections,copy,heapq,itertools,math,string
import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
zahyou = [LI() for _ in range(N)]

rinsetu_array = [[0] * N for _ in range(N)]

for i, XYZ1 in enumerate(zahyou):
    for j, XYZ2 in enumerate(zahyou):
        rinsetu_array[i][j] = abs(XYZ2[0] - XYZ1[0]) + abs(XYZ2[1] - XYZ1[1]) + max(0, XYZ2[2] - XYZ1[2])
            
#print(rinsetu_array)

def tsp(d):
    n = len(d)
    # DP[A] = {v: value}
    DP = dict()
    
    for A in range(1, 1 << n):
        if A & 1 << 0 == 0:# 集合Aが0を含まない
            continue
        if A not in DP:
            DP[A] = dict()

        # main
        for v in range(n):
            if A & 1 << v == 0:
                if A == 1 << 0:
                    DP[A][v] = d[0][v] if d[0][v] > 0 else float('inf')
                else:
                    DP[A][v] = min([DP[A ^ 1 << u][u] + d[u][v] for u in range(n) 
                                    if u != 0 and A & 1 << u != 0 and d[u][v] > 0]
                                  + [float('inf')])
    # 最後だけ例外処理
    V = 1 << n
    DP[V] = dict()
    DP[V][0] = min([DP[A ^ 1 << u][u] + d[u][0] for u in range(n) 
                    if u != 0 and A & 1 << u != 0 and d[u][0] > 0]
                    + [float('inf')]) 


    return DP[V][0]

print(tsp(rinsetu_array))