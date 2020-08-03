#dx[0], dy[0] -> 오른쪽
#dx[1], dy[1] -> 오른쪽
#dx[2], dy[2] -> 오른쪽
#dx[3], dy[3] -> 오른쪽

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())

a = [list(map(int, list(input()))) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
distance = [[0] * M for _ in range(N)]

queue = []
queue.append((0,0))
visit[0][0]
distance[0][0] = 1

while queue:
    x, y = queue.pop(0)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visit[nx][ny] == False and a[nx][ny] == 1:
                queue.append((nx, ny))
                distance[nx][ny] = distance[x][y]+1
                visit[nx][ny] = True

print(distance[N-1][M-1])