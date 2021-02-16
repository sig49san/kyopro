import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
tree_baisuu = []
for i in range(1, 40):
    tree_baisuu.append(3**i)


for B in range(1,30):
    if 5 ** B > 10 ** 18:
        break

    tmp = N
    checker = N - 5 ** B

    if(checker in tree_baisuu):
        print(tree_baisuu.index(checker)+1, B)
        exit()

print(-1)