from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []

    dict_course = {}
    # 코스 개수를 반복
    for c in course:
        dict_case = defaultdict(int)
        # 손님 주문들 반복
        for menus in orders:
            # 코스의 개수만큼 뽑아서 딕셔너리에 저장한다
            if len(menus) >= c:
                for j in combinations(sorted(menus), c):
                    dict_case["".join(j)] += 1
                    # print(dict_case)

        dict_course[c] = dict_case
    # print(dict_course)

    # 개수별 최댓값을 구한다
    # 최댓값과 같은 코스를 뽑는다.
    # 결과 리스트에 담아서 오름차순 정렬한다.
    result = []
    max_count = 0
    for k, v_dict in dict_course.items():
        values_sorted = sorted(v_dict.values(), reverse=-1)

        if values_sorted:
            max_count = values_sorted[0]

        for k2, v2 in v_dict.items():
            if v2 == max_count and max_count > 1:
                result.append(k2)

    # print(result)

    answer = sorted(result)
    print(answer)

    return answer