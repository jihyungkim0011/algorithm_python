# https://www.acmicpc.net/problem/1874
import sys

sys.stdin = open("input.txt")
###

def stack_sequence(n, sequence):
    stack = []
    num = 1
    sequence_idx = 0
    result = []

    while True:
        if len(stack) == 0:
            stack.append(num)
            result.append("+")
            num += 1

        elif sequence[sequence_idx] == stack[-1]:
            stack.pop()
            result.append("-")
            sequence_idx += 1
            if sequence_idx == n:
                break

        else:
            if n < num:
                print("NO")
                break
            stack.append(num)
            result.append("+")
            num += 1

    if len(stack) == 0:
        for char in result:
            print(char)

sequence = list()
n = int(input())
for _ in range(n):
    sequence.append(int(input()))
stack_sequence(n, sequence)
# + + + + - - + + - + + - - - - -
