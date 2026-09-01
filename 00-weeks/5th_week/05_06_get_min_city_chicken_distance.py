import heapq
import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


def get_min_city_chicken_distance(n, m, city_map):
    house_location_list = []
    chicken_list = []
    result = []
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                house_location_list.append((i, j))
            elif city_map[i][j] == 2:
                chicken_list.append((i, j))

    # 최댓값에 맞춰 치킨집 선정하기
    chicken_selection_array = list(itertools.combinations(chicken_list, m))
    for chicken_selection_case in chicken_selection_array:

        # 치킨거리 구하기
        house_chicken_distance_array = []
        for house_location in house_location_list:
            distance_heap = []
            for chicken_location in chicken_selection_case:
                house_r, house_c = house_location
                chicken_r, chicken_c = chicken_location

                chicken_distance = abs(house_r - chicken_r) + abs(house_c - chicken_c)
                heapq.heappush(distance_heap, chicken_distance)

            house_chicken_distance_array.append(heapq.heappop(distance_heap))
        result.append(sum(house_chicken_distance_array))

    return min(result)



# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!

city_map = [
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0]
]
print("정답 = 11 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,1,city_map))

city_map = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2, 2, 0, 1, 2]
]
print("정답 = 10 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,2,city_map))