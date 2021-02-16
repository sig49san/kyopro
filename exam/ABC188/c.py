import sys
import collections
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
As = LI()

    

dq = collections.deque()

for i in range(2 ** N):
    dq.append((i+1, As[i]))

while len(dq) != 2:
    left_player = dq.popleft()
    right_player = dq.popleft()

    if left_player[1] > right_player[1]:
        dq.append(left_player)
    
    else:
        dq.append(right_player)
    #print(list(dq))

lef = dq.popleft()
ri = dq.popleft()

if(lef[1] > ri[1]):
    print(ri[0])

else:
    print(lef[0])
