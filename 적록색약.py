from collections import deque

n=int(input())
a=[list(input())for i in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

c1 = 0
c2 = 0

def bfs(v1,v2):
    de=deque()
    de.append([v1,v2])
    ch[v1][v2] = 1

    while de:
        x,y = de.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <=nx < n and 0 <= ny < n:
                if ch[nx][ny] == 0 and a[x][y] == a[nx][ny]:
                    ch[nx][ny] = 1
                    de.append([nx,ny])

ch = [[0]*n for i in range(n_)]
for i in range(n):
    for j in range(n):
        if ch[i][j] == 0;
        c1 += 1
        bfs(i,j)

for i in range(n):
    for j in range(n):
        if a[i][j] == 'R':
            a[i][j] = 'G'

ch= [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if ch[i][j] == 0;
        c2 += 1
        bfs(i,j)

print(c1,c2)
