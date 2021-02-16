import sys
import collections

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
s = S()

tmp = 0

dq = collections.deque(s)

word = ""
fox_count = 0
while dq:
    word += dq.popleft()

    if len(word) > 2 and word[-3:] == "fox":
        fox_count += 1
        word = word [:-3]

print(N - fox_count * 3)

