import sys

l = (input().split(' '))

N = int(l[0])
Y = int(l[1])

for x in range(0, N+1):
  for y in range(0, N+1-x):
    if Y == 10000 * x + 5000 * y + 1000 * (N-x-y):
      print(x, y, N-x-y)
      sys.exit()
    

print(-1, -1, -1)