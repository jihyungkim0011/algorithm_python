import sys


sys.stdin = open("input.txt")
###

input = sys.stdin.readline
N = int(input())
A = []
for i in range(N):
    A.append((int(input()), i))

sorted_A = sorted(A)
max_num = 0

for i in range(N):
    max_num = max(max_num, sorted_A[i][1] - i)

print(max_num + 1)




# 10 1 5 2 3
# 0  1 2 3 4
# 4  0 3 1 2
#
#
# 1 5 2 3 10
#
# 1 2 3 5 10

