import sys
import itertools

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
xys = [LI() for _ in range(N)]

for i, j ,k in itertools.permutations(range(N), 3):
    x1, y1 = xys[i][0], xys[i][1]
    x2, y2 = xys[j][0], xys[j][1]
    x3, y3 = xys[k][0], xys[k][1]

    if(x1 == x2 or x2 == x3 or x3 == x1):
        if(x1 == x2 == x3):
            print("Yes")
            exit()
        
        continue
    
    if((y1 - y2) / (x1 - x2) == (y2 - y3) / (x2 - x3)):
        if((y1 - x1 * ((y1 - y2) / (x1 - x2))) == (y3 - x3 * ((y3 - y2) / (x3 - x2)))):
            print("Yes")
            exit()
        
    
print("No")
