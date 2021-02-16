import itertools
import sys
import copy

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

Suujitati = S()
ketasuu = len(Suujitati)

if(ketasuu == 1):
    if(Suujitati == "8"):
        print("Yes")
            
    else:
        print("No")

    exit()

checker_1 = [0 for _ in range(10)]

for Suuji in Suujitati:
    num = int(Suuji)

    checker_1[num] += 1

eight_baisuu = [i for i in range(104, 1001, 8)]
eight_baisuu_2 = [i for i in range(16, 100, 8)]

#print(eight_baisuu)


if(ketasuu == 2):
    for baisuu in eight_baisuu_2:
        dc_checker1 = copy.deepcopy(checker_1)

        for s in str(baisuu):
            i = int(s)

            dc_checker1[i] -= 1

        #print(baisuu)

        if(min(dc_checker1) >= 0):
            print("Yes")
            exit()
    
    print("No")
    exit()



for baisuu in eight_baisuu:
    dc_checker1 = copy.deepcopy(checker_1)

    for s in str(baisuu):
        i = int(s)
        
        dc_checker1[i] -= 1
    #print(baisuu)
    
    if(min(dc_checker1) >= 0):
        print("Yes")
        exit()

print("No")
