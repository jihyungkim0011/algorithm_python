
def solution(n, times):
    min_time = 1
    max_time = max(times) * n


    while min_time <= max_time:
        mid_time = (max_time + min_time) // 2

        pass_ppl = 0

        for i in range(len(times)):
            pass_ppl += mid_time // times[i]

        if pass_ppl >= n:
            max_time = mid_time - 1
        else:
            min_time = mid_time + 1

    return min_time


print(solution(6, [7, 10])) # 28