from collections import deque


# maps 1: 길. 0 : 못감
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for i in range(n)]

    queue = deque()

    #    북 동 남 서
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]

    visited[0][0] = 1
    queue.append([0, 0, 1])

    while queue:
        current_c, current_r, count = queue.popleft()

        if current_c == n - 1 and current_r == m - 1:
            return count

        for i in range(4):
            next_c, next_r = current_c + dc[i], current_r + dr[i]

            if 0 <= next_c < n and 0 <= next_r < m and maps[next_c][next_r] == 1 and visited[next_c][next_r] == 0:
                queue.append([next_c, next_r, count + 1])
                visited[next_c][next_r] = 1

    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])) # 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])) # -1