mazeL = []
coor = []
cooraround = []
anonymousNum = 0
answer = 0
firstX = 0
firstY = 0
run = True
N, M = map(int, input().split(' '))
for _ in range(N):
    Li = str(input())
    mazeL.append(Li)
print(N, M)
print(mazeL)
for eachL in mazeL:
    for eachNum in range(len(eachL)):
        if eachL[eachNum] == '1':
            coor.append([mazeL.index(eachL), eachNum])
print(coor)
if coor[firstX][firstY] in coor:   
    if [firstX+1, firstY] in coor:
        cooraround.append([firstX+1, firstY])
    elif [firstX, firstY+1] in coor:
        cooraround.append([firstX, firstY+1])
    elif [firstX-1, firstY] in coor:
        cooraround.append([firstX-1, firstY])
    elif [firstX, firstY-1] in coor:
        cooraround.append([firstX, firstY-1])
    answer += 1
    coor.remove(coor[firstX][firstY])
while run:
    if [N, M]:
    else:
        if [each[0]+1, each[1]] in coor:
            cooraround.append([each[0]+1, each[1]])
            coor.remove(coor[each[0]+1][each[1]])
        elif [each[0], each[1]+1] in coor:
            cooraround.append([each[0], each[1]+1])
            coor.remove(coor[each[0]][each[1]+1])
        elif [each[0]-1, each[1]] in coor:
            cooraround.append([each[0]-1, each[1]])
            coor.remove(coor[each[0]-1][each[1]])
        elif [each[0], each[1]-1] in coor:
            cooraround.append([each[0], each[1]-1])
            coor.remove(coor[each[0]][each[1]-1])
        answer += 1

'''
1. 우선은 N, M을 인풋으로 받기
2. for loop 돌려서 2d 리스트 받기
3. 시작점 [0][0] 지점에서 상하좌우 확인하면서 1이 있으면 answer += 1 그리고 pop(1) + pop한 숫자의 좌표는 다른 리스트에 저장
4. [N][M]에 도착했을경우 리스트.append(answer)
5. print(min(리스트))
BFS
101111
101010
101011
111011
'''