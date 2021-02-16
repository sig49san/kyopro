N = int(input())
Sequence = [int(input()) for _ in range(N)]


moti = list(set(Sequence))

print(len(moti))