import sys

input = sys.stdin.readline

N = int(input())
r_g, c_g = map(int, input().split())
r_p, c_p = map(int, input().split())

grid = []
for i in range(N):
    grid.append(list(input().split()))

def play_game(rinput, cinput):
    r, c = rinput - 1, cinput - 1
    r_next, c_next = r, c
    visited = [[False] * N for _ in range(N)]

    score = 1
    visited[r][c] = True

    while True:

        text = grid[r_next][c_next]
        count, command = int(text[:-1]), text[-1]

        for i in range(count):
            if command == 'U':
                r_next -= 1
            elif command == 'D':
                r_next += 1
            elif command == 'L':
                c_next -= 1
            else:
                c_next += 1

            r_next %= N
            c_next %= N

            if visited[r_next][c_next]:
                return score

            # print(r_next, c_next)

            visited[r_next][c_next] = True
            score += 1


goorm_score = play_game(r_g, c_g)
player_score = play_game(r_p, c_p)

if goorm_score > player_score:
    print('goorm', goorm_score)
else:
    print('player', player_score)

# 밖으로 나가면 반대쪽 칸으로 이동.
# 방문한 칸에 다시 지나가면 게임 종료

# 4
# 4 2
# 2 4
# 1L 3D 3L 1U
# 2D 2L 4U 1U
# 2D 2L 4U 3L
# 4D 4D 1R 4R
#
# player 6
