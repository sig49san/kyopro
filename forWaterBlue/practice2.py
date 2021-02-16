#105という数は, 非常に特殊な性質を持つ - 奇数なのに, 約数が 8個もある.
#さて, 1以上 N以下の奇数のうち, 正の約数を ちょうど 8個持つようなものの個数を求めよ.
#1<=N<=200

N = int(input())

Nlist = list(range(1,N+1, 2))
#print(Nlist)
ans = 0
for n in Nlist:
    tmp = 1
    for i in range(1, (N+1)//2):
        if n % i == 0:
            tmp += 1
    if tmp == 8:
        ans += 1

print(ans)