from itertools import permutations


def prime_number(num):
    if num == 0:
        return False
    if num == 1:
        return False

    if num == 2:
        return True

    if num == 3:
        return True

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False

    return True


def solution(numbers):
    len_numbers = len(numbers)
    answer = set()

    for i in range(1, len_numbers + 1):
        for chunk in permutations(numbers, i):
            # print(chunk)

            int_num = int("".join(chunk))
            # print(int_num)

            if prime_number(int_num):
                answer.add(int_num)

    return len(answer)