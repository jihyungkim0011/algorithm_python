def solution(diffs, times, limit):
    answer = 0

    candidates = []

    left_level = 1
    right_level = max(diffs)

    while left_level <= right_level:
        mid_level = (left_level + right_level) // 2
        total = 0

        for i in range(len(diffs)):
            if mid_level >= diffs[i]:
                total += times[i]
            else:
                total += (times[i - 1] + times[i]) * (diffs[i] - mid_level) + times[i]

        if total > limit:
            left_level = mid_level + 1
        elif total <= limit:
            candidates.append(mid_level)
            right_level = mid_level - 1

    return min(candidates)


diffs, times, limit = [1, 5, 3], [2, 4, 7], 30
print(solution(diffs, times, limit)) # 3
diffs, times, limit = [1, 4, 4, 2], [6, 3, 8, 2], 59
print(solution(diffs, times, limit)) # 2
diffs, times, limit = [1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723
print(solution(diffs, times, limit)) # 294
diffs, times, limit = [1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012
print(solution(diffs, times, limit)) # 39354