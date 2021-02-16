import bisect
import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N =  I()
As = LI()

if(N == 1):
    print(As[0])
    exit()


#As.sort()
hoge = min(As)
tmp = [hoge]

for A in As:
    if(A % hoge != 0):
        tmp.append(A % hoge)

#print(tmp)

As = sorted(tmp)

if(len(As) == 1):
    print(As[0])
    exit()
#print(As)
#Aset = tuple(As)

for _ in range(200000):
#    print(As)
    max_num = As.pop()
    #max_num = max(Aset)
    if(max_num % As[0] == 1):
        print(1)
        exit()

    if(max_num % As[0] != 0):
        max_num = max_num % As[0]
        bisect.insort_left(As, max_num)
#    print(max_num)



    if(As[0] == As[-1]):
        break

print(As[0])
