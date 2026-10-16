import sys

###
sys.stdin = open("input.txt")
###

input = sys.stdin.readline
N = int(input())
a_subject = list(map(int, input().split()))
b_subject = list(map(int, input().split()))

c_group = []

for i in range(N):
    count = 0
    for j in range(N):
        if i == j:
            continue

        if a_subject[i] < a_subject[j]:
            if b_subject[i] < b_subject[j]:
                count += 1

    c_group.append(count)

print(" ".join(str(x) for x in c_group))