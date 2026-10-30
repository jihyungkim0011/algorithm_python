from collections import defaultdict


def solution(points, routes):
    answer = 0
    visited = defaultdict(int)

    len_route = len(routes[0])

    # 로봇들을 동시에 시작점에서 출발시킨다.
    # 이동시킨다.
    # 로봇의 위치를 저장한다.
    # 독립적으로 로봇의 위치를 초, r, c로 저장한다.
    # 딕셔너리에 저장해서 += 1한다.
    # 위치가 겹쳤다면 카운트+1 한다.
    # 최종적으로 카운트를 반환한다.
    # 최종 딕셔너리에서 2 이상인 곳의 count += 1한다.
    # count를 반환한다.
    for route in routes:
        time = 0
        for spot in range(1, len_route):
            r, c = points[route[spot - 1] - 1]
            # print(r, c)

            if spot - 1 == 0:
                visited[(0, r, c)] += 1

            next_r, next_c = points[route[spot] - 1]

            while next_r != r:
                if next_r > r:
                    r += 1
                else:
                    r -= 1
                time += 1
                visited[(time, r, c)] += 1

            while next_c != c:
                if next_c > c:
                    c += 1
                else:
                    c -= 1
                time += 1
                visited[(time, r, c)] += 1

    total = 0
    for value in visited.values():
        if value >= 2:
            total += 1

    return total

