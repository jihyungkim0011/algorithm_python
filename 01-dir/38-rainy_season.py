import sys

input = sys.stdin.readline
N, M = map(int, input().split())
k_list = list(map(int, input().split()))

rain_range = []
for i in range(M):
    rain_range.append(list(map(int, input().split())))
# print(rain_range)

for day in range(M):  # 0 ... M - 1
    for i in range(rain_range[day][0] - 1, rain_range[day][1]):
        k_list[i] += 1
    # print(k_list)

    if (day + 1) % 3 == 0:
        collect_set = set()
        for d in range(day - 2, day + 1):
            for i in range(rain_range[d][0] - 1, rain_range[d][1]):
                collect_set.add(i)
        # print(collect_set)

        for s in collect_set:
            k_list[s] -= 1

print(" ".join(map(str, k_list)))

# i 일에 s ~ e 집 위치까지 비가 내림
# +1
# 배수시스템 3배수 날 작동날짜 기준 2일 이내 -1
# 물의 높이만큼 땅높이