import sys
from collections import deque
###
sys.stdin = open("input.txt")
###

input = sys.stdin.readline
N, M = map(int, input().split())
game_map = [list(input().strip()) for _ in range(N)]

# 구멍에 빨간볼: 종료 / 파랑이 동시에 빠져도 실패

# 결과 : 턴 수 . 10번 초과시 -1
#     북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

#기울이면 벽까지 이동한다.
def straight_forward(r, c, direction, game_map):
    step = 0
    while game_map[r + dr[direction]][c + dc[direction]] != "#" and game_map[r][c] != "O":
        r += dr[direction]
        c += dc[direction]
        step += 1

    return r, c, step

def get_turn(game_map):
    n = len(game_map)
    m = len(game_map[0])

    visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    # print(visited)

    red_r, red_c, blue_r, blue_c = -1, -1, -1, -1
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_r, red_c = i, j
            elif game_map[i][j] == "B":
                blue_r, blue_c = i, j
    visited[red_r][red_c][blue_r][blue_c] = 1
    queue = deque([[red_r, red_c, blue_r, blue_c, 0]])

    while queue:
        red_r, red_c, blue_r, blue_c, turn = queue.popleft()

        if turn > 10:
            break
        if game_map[blue_r][blue_c] == "O":
            continue
        if game_map[red_r][red_c] == "O" and game_map[blue_r][blue_c] != "O":
            return turn

        for direction in range(4):
            next_red_r, next_red_c, red_step = straight_forward(red_r, red_c, direction, game_map)
            next_blue_r, next_blue_c, blue_step = straight_forward(blue_r, blue_c, direction, game_map)

            # 빨강과 파란 구슬은 같은 칸에 있을 수 없다.
            if next_red_r == next_blue_r and next_red_c == next_blue_c:
                if blue_step >= red_step:
                    next_blue_r -= dr[direction]
                    next_blue_c -= dc[direction]
                if red_step > blue_step:
                    next_red_r -= dr[direction]
                    next_red_c -= dc[direction]

            if 0 <= next_blue_r < len(game_map) and 0 <= next_blue_c < len(game_map[0]):
                if visited[next_red_r][next_red_c][next_blue_r][next_blue_c] != 1:
                    queue.append([next_red_r, next_red_c, next_blue_r, next_blue_c, turn + 1])
                    visited[next_red_r][next_red_c][next_blue_r][next_blue_c] = 1
    return -1


print(get_turn(game_map))


# 10 10
# ##########
# #R#...##B#
# #...#.##.#
# #####.##.#
# #......#.#
# #.######.#
# #.#....#.#
# #.#.##...#
# #O..#....#
# ##########