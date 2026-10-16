import sys

input = sys.stdin.readline
count, quiz_count = map(int, input().split())
numbers = list(map(int, input().split()))

sum_list = [0]
temp = 0

for i in numbers:
    temp = temp + i
    sum_list.append(temp)

for i in range(0, quiz_count):
    start, end = map(int, input().split())
    print(sum_list[end] - sum_list[start - 1])
