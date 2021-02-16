import sys

#嘘解答
dayDream = input()

while len(dayDream) != 0:
    if dayDream.startswith('eraser'):
        dayDream = dayDream[6:]
    elif dayDream.startswith('erase'): 
        dayDream = dayDream[5:]
    elif dayDream.startswith('dreamer'):
        dayDream = dayDream[7:]
    elif dayDream.startswith('dream'):
        dayDream = dayDream[5:]
    elif dayDream.startswith('aser'):
        dayDream = dayDream[4:]
    elif dayDream.startswith('ase'):
        dayDream = dayDream[3:]
    else:
        print("NO")
        sys.exit()

print("YES")