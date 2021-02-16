import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
wordList = [S() for _ in range(N)]

wordList.sort()


if(wordList[0][0] == "!"):
    wordList2 = [wordList[0][1:]]
else:
    wordList2 = [wordList[0]]

for i in range(1, N):
    if wordList[i] != wordList[i-1]:
        if(wordList[i][0] == "!"):
            wordList2.append(wordList[i][1:])
        else:
            wordList2.append(wordList[i])        

#print(wordList2)

wordList2.sort()

loop_num = len(wordList2)

for i in range(loop_num-1):
    if(wordList2[i] == wordList2[i+1]):
        print(wordList2[i])
        exit()

print("satisfiable")