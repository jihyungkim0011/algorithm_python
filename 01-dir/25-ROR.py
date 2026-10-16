from collections import deque


def solution(maps):
    m = len(maps)
    n = len(maps[0])
    #              북, 서, 동, 남
    directions_r = [-1, 0, 0, 1]
    directions_c = [0, -1, 1, 0]

    queue = deque([[0, 0, 1]])
    maps[0][0] = 0

    while queue:
        r, c, distance = queue.popleft()

        if r == m - 1 and c == n - 1:
            return distance

        for index in range(4):
            next_r, next_c = r + directions_r[index], c + directions_c[index]
            if 0 <= next_r <= m - 1 and 0 <= next_c <= n - 1 and maps[next_r][next_c] == 1:
                queue.append([next_r, next_c, distance + 1])
                maps[next_r][next_c] = 0
    return -1






print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])) # 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])) # -1

            #             m-1 n
            # m n-1       [m][n]    m n+1
            #             m+1 n