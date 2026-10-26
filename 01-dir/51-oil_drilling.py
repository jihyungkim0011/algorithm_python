from collections import deque


def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])

    visited = [[False] * m for _ in range(n)]

    group_map = [[0] * m for _ in range(n)]
    group_num = 1

    def bfs(i, j, group_num):

        queue = deque([(i, j)])
        visited[i][j] = True
        group_map[i][j] = group_num
        count = 1

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while queue:
            r, c = queue.popleft()

            for k in range(4):
                next_r, next_c = r + dr[k], c + dc[k]
                if 0 <= next_r < n and 0 <= next_c < m and not visited[next_r][next_c] and land[next_r][next_c] == 1:
                    queue.append([next_r, next_c])
                    visited[next_r][next_c] = True
                    group_map[next_r][next_c] = group_num
                    count += 1

        return count

    # 행렬을 탐색하면서 석유가 있는 곳을 찾는다.
    # 석유가 있는 곳에서 석유덩어리 크기를 구한다.
    # 해당 위치에 석유덩어리와 맞는 넘버를 부여하고 매핑한다.

    sizes = []

    for i in range(n):
        for j in range(m):
            size = 0
            if land[i][j] == 1 and not visited[i][j]:
                size = bfs(i, j, group_num)
                sizes.append(size)
                group_num += 1

    # print(sizes)
    # print(group_map)

    #     열마다 탐색한다.
    #     열 중 석유가 있는 곳을 찾으면 몇 칸인지 확인한다.
    #     얻을 수 있는 총 석유량을 합한다.
    totals = []
    for j in range(m):

        set_num = set()

        for i in range(n):
            if land[i][j] == 1:
                set_num.add(group_map[i][j])

        total = 0
        for k in set_num:
            total += sizes[k - 1]
            totals.append(total)

    #     열 중 가장 큰 총 석유량을 구한다.

    return max(totals)







