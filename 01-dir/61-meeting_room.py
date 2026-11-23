import sys

###
sys.stdin = open("../input.txt")
###


N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]
# print(meetings)

meetings.sort(key= lambda x: (x[1], x[0]))
print(meetings)

count = 0
end_time = 0
for start, end in meetings:
    if start >= end_time:
        end_time = end
        count += 1

print(count)