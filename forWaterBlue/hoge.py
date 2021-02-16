import itertools
import copy
def bitsuuretu(n):
    tmp = []
    for i in range(2**n):
        ls = [0] * n
        for j in range(len(ls)):
            if (i >> j) & 1:
                ls[j] += 1
        tmp.append(ls)
    
    return tmp

H,W,K = list(map(int, input().split()))

Carray = [input() for _ in range(H)]

CintArray = []
for cs in Carray:
    tmp = []
    for c in cs:
        if(c == "."):
            tmp.append(0)
        else:
            tmp.append(1)
        
    CintArray.append(tmp)

forHbitArray = bitsuuretu(H)
forWbitArray = bitsuuretu(W)

#print(forHbitArray)
#print(forWbitArray)

for Hindex, Hhoge in enumerate(forHbitArray):
    for Windex, Whoge in enumerate(forWbitArray)i:
        CarrayChecker = copy.copy(CintArray)
        print(Hhoge, Whoge)

        if(Hhoge == 1 or Whoge == 1):
            CarrayChecker[Windex][Hindex] = 0
        
        print(CarrayChecker)
        

        sumCintArray = 0
        for Cints in CarrayChecker:
            sumCintArray += sum(Cints)

        print(sumCintArray)