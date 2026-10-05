import sys

input = sys.stdin.readline
N = int(input())
k_list = list(map(int, input().split()))

score = k_list[0]
sort_mode = True  # 오름차순 / False: 내림차순

for i in range(1, N):
    if k_list[i - 1] <= k_list[i] and sort_mode:
        score += k_list[i]
    elif k_list[i - 1] > k_list[i] and sort_mode:
        sort_mode = False
        score += k_list[i]
    elif k_list[i - 1] >= k_list[i] and not sort_mode:
        score += k_list[i]
    else:
        score = 0
        break

print(score)

# 5
# 1 2 3 3 1
#
# 10
#
#
# 7
# 1 2 3 5 2 3 1
#
# 0
