N,M = map(int, input().split())
switches = [list(map(int,input().split())) for l in range(N)]
p = list(map(int, input().split()))

num_list = list(range(M))
print(num_list)
ans = 0
for bit in range(1<<len(num_list)):
    switch_on = []

    for i in num_list:
        mask = 1 << i
        if bit & mask:
            switch_on.append(i)
    print(switch_on)
    switch_on = list(map(lambda x: x+1, switch_on))
    print(switch_on)

    tmp = 0
    for i in range(len(switches)):
        on_flg = set(switches[i][1:]) & set(switch_on)
        print(on_flg)
        if len(on_flg) % 2 == p[i]:
           tmp += 1
    if(tmp == M):
        ans += 1

print(ans)
