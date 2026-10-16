import sys
sys.stdin = open("input.txt")

###
input = sys.stdin.readline

n, horse_count = map(int, input().split())
game_map = list(list(map(int, input().split())) for _ in range(n))
horse_location_and_directions = list(list(map(int, input().split())) for _ in range(horse_count))

# 0,      1,2,3,4
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

def get_back_direction(d):
    if d % 2 == 0:
        d = d - 1
    else:
        d = d + 1
    return d

def get_game_turn(horse_count, game_map, horse_location_and_directions):
    turn_count = 1

    horse_stacked_map = [[ [] for _ in range(n)] for _ in range(n)]
    for i in range(horse_count):
        r, c, d = horse_location_and_directions[i]
        horse_stacked_map[r - 1][c - 1].append(i)

    while turn_count <= 1000:
        for horse_index in range(horse_count):
            r, c, d = horse_location_and_directions[horse_index]
            new_r, new_c = r - 1 + dr[d], c - 1 + dc[d]

            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = get_back_direction(d)
                new_r, new_c = r - 1 + dr[new_d], c - 1 + dc[new_d]
                horse_location_and_directions[horse_index][2] = new_d

                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue

            moving_horse_stacked_array = []
            for i in range(len(horse_stacked_map[r - 1][c - 1])):
                horse_stacked_index = horse_stacked_map[r - 1][c - 1][i]
                if horse_stacked_index == horse_index:
                    moving_horse_stacked_array = horse_stacked_map[r - 1][c- 1][i:]
                    horse_stacked_map[r - 1][c - 1] = horse_stacked_map[r - 1][c - 1][:i]
                    break

            if game_map[new_r][new_c] == 1:
                moving_horse_stacked_array = reversed(moving_horse_stacked_array)

            for moving_horse_index in moving_horse_stacked_array:
                horse_location_and_directions[moving_horse_index][0] = new_r + 1
                horse_location_and_directions[moving_horse_index][1] = new_c + 1
                horse_stacked_map[new_r][new_c].append(moving_horse_index)

            if len(horse_stacked_map[new_r][new_c]) >= 4: # 말이 네개이상 쌓였을때 종료다.!!#!#@
                return turn_count

        turn_count += 1
    return -1

print(get_game_turn(horse_count, game_map, horse_location_and_directions)) # 7
# 6 10
# 0 1 2 0 1 1
# 1 2 0 1 1 0
# 2 1 0 1 1 0
# 1 0 1 1 0 2
# 2 0 1 2 0 1
# 0 2 1 0 2 1
# 1 1 1
# 2 2 2
# 3 3 4
# 4 4 1
# 5 5 3
# 6 6 2
# 1 6 3
# 6 1 2
# 2 4 3
# 4 2 1
