from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    queue = deque([])
    queue.append([cony_loc, brown_loc, 0])
    visited = [set() for _ in range(200001)] # visited[위치] -> (시간 ... )

    while queue:
        cony_location, brown_location, time = queue.popleft()

        if cony_location == brown_location:
            return time
        elif cony_location > 200_000:
            return time

        next_cony = cony_location + time + 1
        for i in [brown_location - 1, brown_location + 1, 2 * brown_location]:
            next_brown = i

            if 0 <= next_brown <= 200_000 and time + 1 not in visited[next_brown]:
                queue.append([next_cony, next_brown, time + 1])
                visited[next_brown].add(time + 1)



print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))