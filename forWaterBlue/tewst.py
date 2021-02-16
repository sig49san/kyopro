N,M,Q = list(map(int, input().split()))

QuestionScore = list(range(1,M+1))
PlayerAns = [[0] * M] * N

print(QuestionScore)
print(PlayerAns)

for _ in range(Q):
    Sx = list(map(int, input().split()))

    if(Sx[0] == 1):
        ans = 0
        for i, j in zip(PlayerAns[Sx[1]-1], QuestionScore):
            ans += i * j

        print(ans)
    elif(Sx[0] == 2):
        PlayerAns[Sx[1]-1][Sx[2]-1] = 1
        QuestionScore[Sx[2]-1] -= 1 #max(QuestionScore[Sx[2]-1] -1, 0)

        if(QuestionScore[Sx[2]-1] < 0):
            QuestionScore[Sx[2]-1] = 0
        print(QuestionScore)
        print(PlayerAns)