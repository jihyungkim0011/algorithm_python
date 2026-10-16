# https://www.acmicpc.net/problem/1874
import sys

sys.stdin = open("input.txt")
###

def stack_sequence(n, sequence):
    my_stack = []
    numbers = list(range(1, n + 1))
    result = []
    index_sequence = 0
    index_numbers = 0

    while index_sequence <= n - 1:
        if not my_stack:
            my_stack.append(numbers[index_numbers])
            result.append("+")
            index_numbers += 1

        while my_stack and my_stack[-1] < sequence[index_sequence]:
            my_stack.append(numbers[index_numbers])
            result.append("+")
            index_numbers += 1

        if my_stack[-1] == sequence[index_sequence]:
            my_stack.pop()
            result.append("-")
        elif my_stack[-1] > sequence[index_sequence]:
            return print("NO")

        index_sequence += 1

    for l in result:
        print(l)



sequence = list()
n = int(input())
for _ in range(n):
    sequence.append(int(input()))
stack_sequence(n, sequence)
# + + + + - - + + - + + - - - - -
