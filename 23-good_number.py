import sys
sys.stdin = open("input.txt")
###
input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
numbers.sort(reverse= True)

count = 0

for target_index in range(len(numbers)):
    pointer1 = 0
    pointer2 = N - 1

    while pointer1 < pointer2:
        sum_result = numbers[pointer1] + numbers[pointer2]
        if numbers[target_index] > sum_result:
            pointer2 -= 1
        elif numbers[target_index] < sum_result:
            pointer1 += 1
        else:
            if pointer1 != target_index and pointer2 != target_index:
                count += 1
                break
            elif pointer1 == target_index:
                pointer1 += 1
            elif pointer2 == target_index:
                pointer2 -= 1
print(count)

# 1 1 3 4 5 6 7 8 9 10
#       o o o o o o  o  : 7