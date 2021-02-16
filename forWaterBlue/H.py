from collections import deque

N,M,K = list(map(int, input().split()))
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

Asdq = deque(As)
Bsdq = deque(Bs)

Asdq.append(10**10)
Bsdq.append(10**10)

#print(Asdq)
#print(Bsdq)

ans = 0
time = 0
A = Asdq.popleft()
B = Bsdq.popleft()

while True:
#    print(A)
#    print(B)

    if(A == 10 ** 10 and B == 10 ** 10):
        print(ans)
        break

    if(A >= B):
        time += B
        B = Bsdq.popleft()
        
    else:
        time += A
        A = Asdq.popleft()
    
    if(K >= time):
        ans += 1
    
    else:
        print(ans)
        break

