import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
Ss = [S() for _ in range(N)]
true_num = 0
false_num = 0

if(Ss[0] == "AND"):
    true_num += 1
    false_num += 3

else:
    true_num += 3
    false_num += 1


for word in Ss[1:]:
    tmp_true = 0
    tmp_false = 0
    if word == "AND":
        tmp_true = true_num
        tmp_false = false_num * 2 + true_num
    
    else:
        tmp_true = true_num * 2 + false_num
        tmp_false = false_num
    
    true_num = tmp_true
    false_num = tmp_false

print(true_num)