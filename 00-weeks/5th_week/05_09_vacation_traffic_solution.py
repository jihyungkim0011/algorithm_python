

def get_request_count_during_one_second(time, start_and_end_times):
    request_count = 0
    start_time = time
    end_time = time + 1000

    for start_and_end_time in start_and_end_times:
        if start_and_end_time[1] >= start_time and start_and_end_time[0] < end_time:
            request_count += 1
    return request_count


def solution(lines):
    answer = 0
    n = len(lines)
    start_and_end_times = []

    for i in range(n):
        organized = lines[i].split()
        time = organized[1]
        duration = int(float(organized[2][:-1]) * 1000)

        end_time = int((int(time[:2]) * 3600 + int(time[3:5]) * 60 + float(time[6:])) * 1000)
        start_time = end_time - duration + 1
        start_and_end_times.append([start_time, end_time])

        for start_and_end_time in start_and_end_times:
            answer = max(get_request_count_during_one_second(start_and_end_time[0], start_and_end_times),
                         get_request_count_during_one_second(start_and_end_time[1], start_and_end_times),
                         answer)

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
