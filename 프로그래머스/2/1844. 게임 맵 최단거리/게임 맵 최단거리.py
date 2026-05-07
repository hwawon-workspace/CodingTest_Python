from collections import deque
def solution(maps):
    answer = 0

    dx = [-1, 1, 0, 0] # 좌우 이동
    dy = [0, 0, -1, 1] # 상하 이동

    def bfs(x, y): # 0,1맵 -> 거리 맵으로 바꾸는 bfs
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()

            for i in range(4): # 현재 위치에서 상하좌우 이동했을 때
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): continue # 맵 밖일 때

                if maps[nx][ny] == 0:  continue # 벽일 때

                if maps[nx][ny] == 1: # 갈 수 있는데, 아직 방문X
                    maps[nx][ny] = maps[x][y] + 1 # maps에 이동 횟수 1 더하기
                    queue.append((nx, ny)) # queue에 현재 위치 추가
                    
        return maps[len(maps)-1][len(maps[0])-1] # 적 진영에서의 값

    answer = bfs(0, 0)
    return -1 if answer == 1 else answer