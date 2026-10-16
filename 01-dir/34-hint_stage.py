from itertools import product

def solution(cost, hint):
    n = len(cost)
    answer = float('inf')

    for choices in product((0, 1), repeat = n -1):
        counts = [0] * n
        total = 0

        for buy, bundle in zip(choices, hint):
            if buy:
                total += bundle[0]
                for stage in bundle[1:]:
                    counts[stage - 1] += 1

        for i in range(n):
            total += cost[i][min(counts[i], n - 1)]

        answer = min(answer, total)

    return answer


cost = [
    [160, 140, 120, 110, 60],
    [290, 270, 260, 120, 10],
    [160, 130, 120, 60, 20],
    [160, 120, 80, 70, 20],
    [110, 70, 60, 30, 20]
]
hint = [
    [40, 2, 3],
    [40, 5, 3],
    [20, 5, 4],
    [50, 5, 5]
]
print(solution(cost, hint)) # 810