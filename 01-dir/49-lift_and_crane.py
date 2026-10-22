from collections import deque


def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    for i in range(n):
        storage[i] = list(storage[i])

    answer = 0

    picked = [[False] * m for _ in range(n)]
    stack = []

    def check_dir(storage, picked, i, j):
        visited = [[False] * m for _ in range(n)]
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        queue = deque()
        queue.append((i, j))
        visited[i][j] = True

        while queue:
            r, c = queue.popleft()

            if r == 0 or r == n - 1:
                return True
            elif c == 0 or c == m - 1:
                return True

            for k in range(4):
                next_r = r + dr[k]
                next_c = c + dc[k]

                if not visited[next_r][next_c] and picked[next_r][next_c]:
                    queue.append((next_r, next_c))
                    visited[next_r][next_c] = True

        return False

    def check_crane(storage, i, j, letter):
        if storage[i][j] == letter:
            return True
        return False

    for letter in requests:
        current_letter = letter

        for i in range(n):
            for j in range(m):

                if len(current_letter) == 1:
                    if storage[i][j] == current_letter:
                        if check_dir(storage, picked, i, j):
                            storage[i][j] = 0
                else:
                    if check_crane(storage, i, j, current_letter[0]):
                        storage[i][j] = 0

        for i in range(n):
            for j in range(m):
                if storage[i][j] == 0:
                    picked[i][j] = True
        # print(storage)
        # print(picked)

    count = 0
    for i in range(n):
        count += storage[i].count(0)
    answer = n * m - count

    return answer

storage, requests = ["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"]
print(solution(storage, requests)) # 11
storage, requests = ["HAH", "HBH", "HHH", "HAH", "HBH"], ["C", "B", "B", "B", "B", "H"]
print(solution(storage, requests)) # 4
