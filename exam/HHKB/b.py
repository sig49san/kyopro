H,W = list(map(int, input().split()))

hoge = ["#" for _ in range(W)]
Sarray = [hoge]
for i in range(H):
    Sarray.append(list(input()))

Sarray.append(hoge)


for S in Sarray[:-1]:
    S.append("#")
    S.insert(0, "#")
    


ans = 0

for i in range(H+1):
    for j in range(W+1):
        if(Sarray[i][j] == "." and Sarray[i][j+1] == "."):
            ans += 1
        
        if(Sarray[i][j] == "." and Sarray[i+1][j] == "."):
            ans += 1

print(ans)