N = int(input())
Ps = list(map(int, input().split()))

checker = [0 for _ in range(5 * 10**5 + 10)]
print(checker)
ans = 0
for P in Ps:
    checker[P] = 1

    for i in range(200100):
        if(checker[ans] == 0):
            print(ans)
#            print(checker[:20])
#            print(i)
            break

        else:
            ans+=1

