import sys
from collections import deque
def bfs(array,y,x,val): # 너비우선 탐색
    dx = [0,1,0,-1] # 북, 동, 남, 서
    dy = [-1,0,1,0]
    q = deque()
    q.append((y,x))
    while q:
        now = q.popleft()
        for i in range(4): # 4방면 확인
            h = now[0] + dx[i]
            w = now[1] + dy[i]
            if 0 <= h < n and 0 <= w < n:
                if array[h][w] == val: # 같은 색이면 방문표시 = 0
                    array[h][w] = 0
                    q.append((h,w))

if __name__ == "__main__":
    read = sys.stdin.readline
    n = int(read())
    board = [list(read()) for _ in range(n)] # 일반
    board_rg = [[0]*n for _ in range(n)] # 적록색약
    for i in range(n): # 적록색약용 보드 만들기
        for j in range(n):
            if board[i][j] == 'R' or board[i][j] == 'G':
                board_rg[i][j] = 1
            else:
                board_rg[i][j] = 2
    cnt = 0
    cnt_rg = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0: # 일반 확인
                cnt += 1
                bfs(board,i,j,board[i][j])
            if board_rg[i][j] != 0: # 적록색약 확인
                cnt_rg += 1
                bfs(board_rg,i,j,board_rg[i][j])
    print(cnt,cnt_rg)