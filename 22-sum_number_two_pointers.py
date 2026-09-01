import sys

sys.stdin = open("input.txt")

N = int(input())

pointer1 = 0
pointer2 = 1
count = 0
sum_result = 1

while pointer2 <= N:
    if sum_result == N:
        count += 1
        pointer2 += 1
        sum_result += pointer2
    elif sum_result < N:
        pointer2 += 1
        sum_result += pointer2
    else:
        pointer1 += 1
        sum_result -= pointer1


print(count)




# 1+2+3+4+5 15
# 카운트 ++
#
# 타겟 > 합 -> 뒤 포인터 ++
#
# 1 2 3 4 5 6 -> 21
# 타겟 < 합 -> 앞 포인터 ++


# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

