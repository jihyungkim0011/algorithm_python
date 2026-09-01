from itertools import combinations


def solution(numbers, target):
    count = 0
    minus_list = []
    temp = 0
    sum_numbers = sum(numbers)

    for i in range(0, len(numbers)):
        minus_list = list(combinations(numbers, i))

        for k in minus_list:
            temp = sum_numbers - 2 * sum(k)

            if temp == target:
                count += 1
            else:
                temp = 0

    return count


numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))  # 2

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))  # 3

