import sys

###
sys.stdin = open("../input.txt")
###

N = int(input())

# 5로 나누어서 나머지값을 구한다.
value, rest = divmod(N, 5)

# 나머지가 3으로 나눠떨어지는지 확인한다.
# 나누어 떨어지면 몫을 더한다.
# 나눠떨어지지 않으면 4의 몫 -1 의 나머지 값으로 3으로 떨어지는지 확인한다.
# 반복
while value >= 0:

    value_3, rest_3 = divmod(rest, 3)

    if rest_3 == 0:
        print(value + value_3)
        break
    else:
        value -= 1
        rest += 5

else:
    print(-1)