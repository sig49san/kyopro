import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
H, W = LI()
Sarray = []

for _ in range(H):
    tmp = S()
    hoge = []
    for fuga in tmp:
        hoge.append(fuga)
    Sarray.append(hoge)

#print(Sarray)
ans = 4
i_range = [W+1,0]
j_range = [H+1,0]
for i in range(H):
    for j in range(W):
        if(Sarray[i][j] == "."):
            continue

        i_range[0] = min(i_range[0], i)
        i_range[1] = max(i_range[1], i)

        j_range[0] = min(j_range[0], j)
        j_range[1] = max(j_range[1], j)

#print(i_range,j_range)
#print(Sarray)
for i in range(i_range[0], i_range[1]+1):
    for j in range(j_range[0], j_range[1]+1):

        if(Sarray[i][j] == "#"):
            continue

        if(Sarray[i][j+1] == "." and Sarray[i][j-1] == "."):
            continue

        if(Sarray[i+1][j] == "." and Sarray[i-1][j] == "."):
            continue

        tmp = 0

        if(Sarray[i][j-1] == "#"):
            tmp += 1

        if(Sarray[i][j+1] == "#"):
            tmp += 1

        if(Sarray[i+1][j] == "#"):
            tmp += 1

        if(Sarray[i-1][j] == "#"):
            tmp += 1

        if(tmp == 2):
            ans+=2
        
        if(tmp == 3):
            ans+=4


#print(i_range, j_range)

print(ans)