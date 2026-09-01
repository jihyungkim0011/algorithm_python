import sys

sys.stdin = open("input.txt")
###

input = sys.stdin.readline

N = int(input())
numbers = list(map(int,input().split()))
count = 0

for i in numbers:
    det = 0
    if i == 1:
        pass
    elif i == 2:
        count += 1
    else:
        for k in range(2,i):
            if i % k == 0:
                det = 1

        if det != 1:
            count += 1

print(count)


# 7
# 1 2 3 5 7 8 9
# solution: 4