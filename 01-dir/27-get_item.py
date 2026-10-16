from collections import deque

#         북0      서1     남2      동3
move = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def solution(rectangles, characterX, characterY, itemX, itemY):
    board = [[0] * 102 for _ in range(102)] # 외부 0

    for x1, y1, x2, y2 in rectangles:
        for i in range(2 * x1, 2 * x2 + 1):
            for j in range(2 * y1, 2 * y2 + 1):
                if 2 * x1 < i < 2 * x2 and 2 * y1 < j < 2 * y2:
                    board[i][j] = -1 # 내부 -1
                elif board[i][j] != -1:
                    board[i][j] = 1 # 직선 상 1

    queue = deque([(characterX * 2, characterY * 2, 0)])
    board[characterX * 2][characterY * 2] = 0

    while queue:
        x, y, distance = queue.popleft()

        if x == itemX * 2 and y == itemY * 2:
            return distance // 2

        for i in range(4):
            next_x, next_y = x + move[i][0], y + move[i][1]

            if 0 <= next_x < 102 and 0 <= next_y < 102 and board[next_x][next_y] == 1:
                queue.append((next_x, next_y, distance + 1))
                board[next_x][next_y] = 0
    return None



input_rectangle = [
    [1,1,7,4],
    [3,2,5,5],
    [4,3,6,9],
    [2,6,8,8]
]
print(solution(input_rectangle, 1, 3, 7, 8)) # 17

input_rectangle = [
    [1, 1, 8, 4],
    [2, 2, 4, 9],
    [3, 6, 9, 8],
    [6, 3, 7, 7]
]
print(solution(input_rectangle, 9, 7, 6, 1)) # 11

input_rectangle = [
    [1, 1, 5, 7]
]
print(solution(input_rectangle, 1, 1, 4, 7)) # 9

input_rectangle = [
    [2, 1, 7, 5],
    [6, 4, 10, 10]
]
print(solution(input_rectangle, 3, 1, 7, 10)) # 15

input_rectangle = [
    [2, 2, 5, 5],
    [1, 3, 6, 4],
    [3, 1, 4, 6]
]
print(solution(input_rectangle, 1, 4, 6, 3)) # 10