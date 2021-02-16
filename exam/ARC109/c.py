import sys
import collections
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


n, k= LI()
s = S()
s = s + s

#print(s)

for i in range(k):
    tmp = ""
    for j in range(n):
        if(s[2*j] == s[2*j+1]):
            tmp += s[2*j]

        elif(s[2*j:2*j+2] == "RS" or s[2*j:2*j+2] == "SP" or s[2*j:2*j+2] == "PR"):
            tmp += s[2*j]

        elif(s[2*j:2*j+2] == "SR" or s[2*j:2*j+2] == "PS" or s[2*j:2*j+2] == "RP"):
            tmp += s[2*j+1]
    #print(tmp)
    s = tmp + tmp
    #print(s)

print(s[0])
