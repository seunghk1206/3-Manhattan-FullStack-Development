mazeL = []
coor = []
cooraround = []
lenL = []
path = []
answer = 0
N, M = map(int, input().split(' '))
for _ in range(N):
    Li = str(input())
    mazeL.append(Li)
for eachL in range(N):
    for eachNum in range(M):
        if mazeL[eachL][eachNum] == '1':
            coor.append([eachL, eachNum])
cooraround.append([0, 0])
coor.remove([0, 0])
for each in cooraround:
    path.append(each)
    if each == [N-1, M-1]:
        answer += 1
        lenL.append(answer)
    else:
        if [each[0]+1, each[1]] in coor:
            cooraround.append([each[0]+1, each[1]])
            coor.remove([each[0]+1, each[1]])
        elif [each[0], each[1]+1] in coor:
            cooraround.append([each[0], each[1]+1])
            coor.remove([each[0], each[1]+1])
        elif [each[0]-1, each[1]] in coor:
            cooraround.append([each[0]-1, each[1]])
            coor.remove([each[0]-1, each[1]])
        elif [each[0], each[1]-1] in coor:
            cooraround.append([each[0], each[1]-1])
            coor.remove([each[0], each[1]-1])
        answer += 1
print(min(lenL))
print(path)