import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()

checker = []

sumX = 0
for _ in range(N):
    x , y = LI()
    sumX += x
    checker.append(2 * x + y)

#print(sumX)
#print(checker)

checker.sort(reverse=True)

tmp = 0
for index, count in enumerate(checker):
    tmp += count
    if tmp > sumX:
        print(index + 1)
        sys.exit()