seat_count = 9
vip_seat_array = [4, 7]

seat_memo = {
    1: 1,
    2: 2
}

# 1 2 3 4 5  4일때 경우의수
# 1 2 3 5 4  3일때 경우의수
# n번째: n-1 일때 경우의수
# n-2일때 경우의 수


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    count_seat_list = []
    result = 1

    for i in range(len(fixed_seat_array) + 1):
        if i == 0:
            temp = fixed_seat_array[0] - 1
            count_seat_list.append(temp)
        elif i == len(fixed_seat_array):
            temp = total_count - fixed_seat_array[i - 1]
            count_seat_list.append(temp)
        else:
            temp = fixed_seat_array[i] - fixed_seat_array[i - 1] - 1
            count_seat_list.append(temp)

    while count_seat_list:
        count = count_seat_list.pop()
        result *= count_case_dp(count, seat_memo)
    return result

def count_case_dp(n, memo):
    if n in memo:
        return memo[n]

    result = count_case_dp(n - 1, memo) + count_case_dp(n - 2, memo)
    memo[n] = result
    return result


print("정답 = 12 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(seat_count, vip_seat_array))
print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))