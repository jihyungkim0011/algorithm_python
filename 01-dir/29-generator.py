import sys
from collections import deque
###
sys.stdin = open("input.txt")
###

input = sys.stdin.readline
N, K = map(int, input().split())
city_map = [list(map(int, input().split())) for _ in range(N)]

#    북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def solution(n, k, city_map):
    visited = [[False] * n for _ in range(n)]
    region_list = [0] * 31

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                queue = deque([[i, j]])
                visited[i][j] = True
                same_type_count = 1
                current_building_type = city_map[i][j]

                while queue:
                    r, c = queue.popleft()
                    for direction in range(4):
                        next_r, next_c = r + dr[direction], c + dc[direction]
                        if 0 <= next_r < n and 0 <= next_c < n and city_map[next_r][next_c] == current_building_type and not visited[next_r][next_c]:
                            visited[next_r][next_c] = True
                            queue.append([next_r, next_c])
                            same_type_count += 1

                if same_type_count >= k:
                    region_list[current_building_type] += 1

    max_value = 0
    result = 0
    for k,v in enumerate(region_list):
        if v > max_value:
            max_value = v
            result = k

    return result


print(solution(N, K, city_map))

# 10 3
# 6 8 8 4 2 6 5 9 4 5
# 10 9 9 10 10 10 10 10 4 5
# 6 9 3 10 10 10 10 10 10 10
# 4 4 4 4 10 10 10 7 7 7
# 9 4 4 2 10 10 10 7 1 2
# 9 2 4 1 1 5 8 5 5 5
# 4 4 4 4 6 5 8 8 6 5
# 6 4 4 9 9 7 8 8 6 5
# 9 4 4 2 9 9 8 8 8 5
# 8 4 7 9 5 9 8 3 10 10