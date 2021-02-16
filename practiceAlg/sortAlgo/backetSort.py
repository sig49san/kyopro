
#fileからのデータ入力
path = 'sortedSequence.txt' 
with open (path, mode = 'r') as f:
    fileList = [s.strip() for s in f.readlines()]

N = int(fileList[0])
sequence = fileList[1].split(' ')
sequence = [int(s) for s in sequence]

#print(sequence)

backet = [0]*(N+1)

#print(backet)

for s in sequence:
    backet[s] += 1

#print(backet)

sortedSequence = []

i = 0
for s in backet:
    sortedSequence += ([i] * s)
    i +=1

#print(sortedSequence)

bobScore = sum(sortedSequence[0::2])
AliceScore = sum(sortedSequence[1::2])

print(AliceScore - bobScore)