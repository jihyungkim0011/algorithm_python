import sys

input = sys.stdin.readline

n, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for _ in range(q):
    coords = list(map(int, input().split()))

    # 세 꼭짓점 (행, 열) 추출
    points = [
        (coords[i] - 1, coords[i + 1] - 1)
        for i in range(0, 6, 2)
    ]

    rows = [r for r, c in points]
    cols = [c for r, c in points]

    min_r, max_r = min(rows), max(rows)
    min_c, max_c = min(cols), max(cols)

    size = max_r - min_r + 1

    # 직각 꼭짓점의 행과 열
    right_r = next(r for r in rows if rows.count(r) == 2)
    right_c = next(c for c in cols if cols.count(c) == 2)

    total = 0

    for i in range(size):
        # 왼쪽 위
        if right_r == min_r and right_c == min_c:
            start, end = 0, size - i

        # 오른쪽 위
        elif right_r == min_r and right_c == max_c:
            start, end = i, size

        # 왼쪽 아래
        elif right_r == max_r and right_c == min_c:
            start, end = 0, i + 1

        # 오른쪽 아래
        else:
            start, end = size - 1 - i, size

        for j in range(start, end):
            total += arr[min_r + i][min_c + j]

    print(total)


