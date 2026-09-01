# https://www.acmicpc.net/problem/1929
from math import sqrt

a, b = list(map(int, input().split()))

def is_prime_number(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(sqrt(number))+1):
        if number % i == 0:
            return False

    return True

def find_prime_list_under_number(start, end):

    if end <= 1:
        return []

    numbers = [i for i in range(start, end + 1)]
    prime_numbers = [i for i in numbers if is_prime_number(i) is True]

    return prime_numbers


result = find_prime_list_under_number(a, b)
for i in result:
    print(i)