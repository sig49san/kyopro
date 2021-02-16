import itertools
import collections


H, W = list(map(int, input().split()))
sArray = [input() for _ in range(H)]

bfs_map = [[-1] * (W+2) for _ in range(H+2)]

for i,j in itertools.product(range(1, H+1), range(1,W+1)):
    if sArray[i-1][j-1] == ".":
        bfs_map[i][j] = 10000

dq = collections.deque()
dq.append([1,1])
bfs_map[1][1] = 0

#print(list(dq))

dxys = [[1, 0], [0, 1], [-1, 0], [0, -1]]

while dq:
    nx, ny = dq.popleft()

    for dx, dy in dxys:
        if(bfs_map[nx+dx][ny+dy] > bfs_map[nx][ny] + 1):
            bfs_map[nx+dx][ny+dy] = bfs_map[nx][ny] + 1
            dq.append([nx+dx, ny+dy])

#print(np.array(bfs_map))
if(bfs_map[H][W] == 10000):
    print(-1)
    exit()


ans = 0
checker_list = [0 for _ in range(10010)]
#print(checker_list)

for i in range(H+2):
    for j in range(W+2):
        if(bfs_map[i][j] == -1):
            continue
    
        if(bfs_map[i][j] > bfs_map[H][W]):
            ans += 1
            continue
        

        tmp = bfs_map[i][j]

        if(checker_list[tmp] == 0):
            checker_list[tmp] = 1
            continue

        else:
            ans += 1

print(ans)