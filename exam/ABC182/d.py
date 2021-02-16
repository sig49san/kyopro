import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
As = LI()

max_move = -1 * 10**9
end_move = 0
max_iti = 0
now_iti = 0

for A in As:
    end_move += A

    if end_move > max_move:
        max_move = end_move
    
    if now_iti + max_move >= max_iti:
        max_iti = now_iti + max_move
    
    now_iti += end_move
    #print(max_move, end_move, max_iti, now_iti)

print(max_iti)