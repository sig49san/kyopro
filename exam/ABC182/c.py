import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

Ns = S()

one_bi = 0
two_bi = 0
three_bi = 0

sum_num = 0

if(len(Ns) == 1):
    if int(Ns) % 3 == 0:
        print(0)
    
    else:
        print(-1)

    exit()

if(len(Ns) == 2):
    if(int(Ns) % 3 == 0):
        print(0)
        exit()
    
    else:
        for N in Ns:
            if int(N) % 3 == 0:
                print(1)
                exit()
        
        print(-1)
        exit()


for N in Ns:
    sum_num += int(N)

    if(int(N) % 3 == 1):
        one_bi += 1
    
    elif(int(N) % 3 == 2):
        two_bi += 1
    
    else:
        three_bi += 1

sum_num = sum_num % 3
#print(sum_num)

if(sum_num == 0):
    print(0)
    exit()

#rint(one_bi, two_bi, three_bi)

if(sum_num == 1):
    if(one_bi >= 1):
        print(1)
        exit()
    
    elif(two_bi >= 2):
        print(2)
        exit()
    
    else:
        print(-1)
        exit()

if(sum_num == 2):
    if(two_bi >= 1):
        print(1)
    
    elif(one_bi >= 2):
        print(2)
    
    else:
        print(-1)
    exit()