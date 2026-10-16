# https://www.acmicpc.net/problem/10807
import sys

sys.stdin = open("input.txt")
###

N = int(input())
numbers = list(map(int,input().split()))
target = int(input())

def count_same_number(numbers, target):
    result = 0

    for number in numbers:
        if number == target:
            result += 1

    return result

print(count_same_number(numbers, target))