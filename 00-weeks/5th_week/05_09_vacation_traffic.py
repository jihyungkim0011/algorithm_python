import sys


def solution(lines):
    n = len(lines)
    times = []
    min_time = sys.maxsize
    max_time = 0

    for i in range(n):
        organized = lines[i].split()
        time = organized[1]
        duration = int(float(organized[2][:-1]) * 1000)

        end_time = int((int(time[:2]) * 3600 + int(time[3:5]) * 60 + float(time[6:])) * 1000)
        start_time = end_time - duration + 1
        times.append([start_time, end_time])

    counts = []
    for window_index in range(len(times)):
        window_i_start, window_j_start = times[window_index][0], times[window_index][0] + 1000 - 1
        count = 0
        for i in range(n):
            if times[i][0] <= window_j_start and times[i][1] >= window_i_start:
                count += 1
        counts.append(count)

        window_i_end, window_j_end = times[window_index][1], times[window_index][1] + 1000 - 1
        count = 0
        for i in range(n):
            if times[i][0] <= window_j_end and times[i][1] >= window_i_end:
                count += 1
        counts.append(count)

    answer = max(counts)
    return answer


lines = [
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]
print(solution(lines))# 7 이 출력되어야 합니다.

lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
print(solution(lines))# 2 이 출력되어야 합니다.

lines = ["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]
print(solution(lines)) # 1 이 출력되어야 합니다.
