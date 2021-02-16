import sys

N = int(input ())
timeGrid = [input() for _ in range(N)]
timeGrid = [timeGrid[n].split(' ') for n in range(2)]

intTimeGrid = [[0,0,0]]

for gridlist in timeGrid:
	gridlist = list(map(int, gridlist))
	intTimeGrid.append(gridlist)

for i in range(len(intTimeGrid) - 1):
    gridNow = intTimeGrid[i]
    gridNext = intTimeGrid[i + 1]

    deltaTime = gridNext[0] - gridNow[0]
    deltaX = abs(gridNext[1] - gridNow[1])
    deltaY = abs(gridNext[2] - gridNow[2])
    moving = deltaX + deltaY

    #距離判定
    if(deltaTime < moving):
        print("No")
        sys.exit()
    
    if(deltaTime % 2 != moving % 2):
        print("No")
        sys.exit()

print("Yes")
