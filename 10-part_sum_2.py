import sys

input = sys.stdin.readline
array_size, no_prob = map(int, input().split())

A = [[0] * (array_size + 1)]
D = [[0] * (array_size + 1) for _ in range(array_size + 1)]

for i in range(0, array_size):
    A_row = [0] + list(map(int, input().split()))
    A.append(A_row)

for i in range(1, array_size + 1):
    for j in range(1, array_size + 1):
        D[i][j] = A[i][j] + D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1]

for i in range(0, no_prob):
    x1, y1, x2, y2 = map(int, input().split())

    print(D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1])
