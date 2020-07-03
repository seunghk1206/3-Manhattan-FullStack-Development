mazeL = []
coor = []
cooraround = []
anonymousNum = 0
answer = 0
firstX = 0
firstY = 0
N, M = map(int, input().split(' '))
for _ in range(N):
    Li = str(input())
    mazeL.append(Li)
print(N, M)
print(mazeL)
for eachL in mazeL:
    for eachNum in eachL:
        if eachNum == '1':
            coor.append([mazeL.index(eachL), eachL.index(eachNum)])
print(coor)
for each in coor:
    if [firstX+1, firstY] == each:
        cooraround.append([firstX+1, firstY])
    elif [firstX, firstY+1] == each:
        cooraround.append([firstX, firstY+1])
    elif [firstX-1, firstY] == each:
        cooraround.append([firstX-1, firstY])
    elif [firstX, firstY-1] == each:
        cooraround.append([firstX, firstY-1])
#for each in coor:

'''
1. 우선은 N, M을 인풋으로 받기
2. for loop 돌려서 2d 리스트 받기
3. 시작점 [0][0] 지점에서 상하좌우 확인하면서 1이 있으면 answer += 1 그리고 pop(1) + pop한 숫자의 좌표는 다른 리스트에 저장
4. [N][M]에 도착했을경우 리스트.append(answer)
5. print(min(리스트))
BFS
0101111
0101010
0101011
0111011
'''