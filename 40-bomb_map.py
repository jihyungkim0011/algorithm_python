import sys

input = sys.stdin.readline

N, K = map(int, input().split())

map_list = [[] for _ in range(N)]

for i in range(N):
    map_list[i] = list(input().split())

bombs = []
for i in range(K):
    bombs.append(list(map(int, input().split())))

map_copy = [[0] * N for _ in range(N)]


# print(map_copy)
# print(map_list)

def check(i, j, map_copy, map_list):
    if 0 < i <= N and 0 < j <= N:
        if map_list[i - 1][j - 1] == '#':
            map_copy[i - 1][j - 1] = 0
        elif map_list[i - 1][j - 1] == '@':
            map_copy[i - 1][j - 1] += 2
        else:
            map_copy[i - 1][j - 1] += 1
    return map_copy


for bomb in bombs:
    map_copy = check(bomb[0], bomb[1], map_copy, map_list)
    map_copy = check(bomb[0] - 1, bomb[1], map_copy, map_list)
    map_copy = check(bomb[0] + 1, bomb[1], map_copy, map_list)
    map_copy = check(bomb[0], bomb[1] - 1, map_copy, map_list)
    map_copy = check(bomb[0], bomb[1] + 1, map_copy, map_list)
# print(map_copy)

max_list = []
for i in range(N):
    number = max(map_copy[i])
    max_list.append(number)
print(max(max_list))

# 인접 상하좌우에 영향.
# 0 -> +1
# @ -> +2
# # 변화 없음.
# 			r-1, c
# r, c-1     r, c      r, c+1
# 			r+1, c