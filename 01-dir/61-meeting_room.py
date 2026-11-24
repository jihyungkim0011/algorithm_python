import sys

###
sys.stdin = open("../input.txt")
###

N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]
# print(meetings)

# 끝나는 시간이 짧은 것을 먼저 찾으면 최대 회의의 수를 찾을 수 있다.
# 끝나는 시간으로 회의를 정렬한다.
meetings.sort(key= lambda x: (x[1], x[0]))
# print(meetings)

# 반복한다.
# if 끝나는 시간 <= 시작시간:
#     커서 = 끝나는 시간
#     회의 수 ++
end_cursor = 0
count = 0
for start, end in meetings:
    if end_cursor <= start:
        end_cursor = end
        count += 1

print(count)