import sys
from collections import Counter

###
sys.stdin = open("input.txt")
###

input = sys.stdin.readline
N, K = map(int, input().split())
distances = list(map(int, input().split()))

# 누적합(사람들의 위치) 미리 저장
person_position = [0] * N
for index in range(1, N):
    person_position[index] = person_position[index - 1] + distances[index - 1]
#원의 둘레
total_circle_distance = person_position[N - 1] + distances[N - 1]

# 카운터 생성 - 리스트 안에 요소와 그의 개수를 키:값으로 저장한다.
behind_group_remainders = Counter()
ahead_group_remainders = Counter()
# 각 위치에서 보폭을 나눴을 때 나머지가 같은 것들을 카운트한다.
for position in person_position:
    remainder_value = position % K
    ahead_group_remainders[remainder_value] += 1

results = []
for current_position in person_position:
    # 특정 위치 기준, 앞에 있는 사람들 중 같은 나머지값을 가지는 것을 찾는다(본인 제외)
    current_remainder = current_position % K
    ahead_group_remainders[current_remainder] -= 1
    valid_target_ahead = ahead_group_remainders[current_remainder]

    # 특정 위치 기준, 뒤에 있는 사람들 중 같은 나머지 값을 가지는 것을 찾는다
    needed_remainder_for_two_wrap_around = (current_position - total_circle_distance) % K
    valid_target_behind = behind_group_remainders[needed_remainder_for_two_wrap_around]

    # 앞
    results.append(valid_target_ahead + valid_target_behind)
    print(valid_target_ahead + valid_target_behind)

    behind_group_remainders[current_remainder] += 1


# 1 2 3 4
# 1 3 6
#   2 5 9
#     3 7 8
#       4 5 7

# 2 1 1 0