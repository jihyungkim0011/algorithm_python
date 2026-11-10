def solution(rows, columns, queries):
    answer = []

    def up(rc, rc_copy, x, y):
        rc_copy[x - 1][y] = rc[x][y]
        return rc_copy

    def down(rc, rc_copy, x, y):
        rc_copy[x + 1][y] = rc[x][y]
        return rc_copy

    def right(rc, rc_copy, x, y):
        rc_copy[x][y + 1] = rc[x][y]
        return rc_copy

    def left(rc, rc_copy, x, y):
        rc_copy[x][y - 1] = rc[x][y]
        return rc_copy

    # 행렬 초기화한다: 행을 채우면서 아래로 내려간다. 1부터 오름차순.
    mat = [[0] * columns for _ in range(rows)]

    num = 1
    for i in range(rows):
        for j in range(columns):
            mat[i][j] = num
            num += 1
    # print(mat)

    # queries를 반복한다.
    for query in queries:
        mat_copy = [[10_001] * columns for _ in range(rows)]
        # query에서 추출
        x1, y1, x2, y2 = query
        # print(x1, y1, x2, y2)

        # 모서리 부분: x1 y1, x1 y2, x2 y1, x2 y2
        # x1,y1 오른쪽
        # x1,y2 아래
        # x2,y1 위로
        # x2,y2 왼쪽
        mat_copy = right(mat, mat_copy, x1 - 1, y1 - 1)
        mat_copy = down(mat, mat_copy, x1 - 1, y2 - 1)
        mat_copy = up(mat, mat_copy, x2 - 1, y1 - 1)
        mat_copy = left(mat, mat_copy, x2 - 1, y2 - 1)
        # print(mat_copy)

        # x1: 오른쪽으로 이동 [y1, y2]
        # x2: 왼쪽으로 이동 [y1, y2]
        # y1: 위로 이동 [x1, x2]
        # y2: 아래로 이동 [x1, x2]
        for i in range(y1 - 1, y2 - 1):
            mat_copy = right(mat, mat_copy, x1 - 1, i)
        for i in range(y1, y2):
            mat_copy = left(mat, mat_copy, x2 - 1, i)
        for i in range(x1, x2):
            mat_copy = up(mat, mat_copy, i, y1 - 1)
        for i in range(x1 - 1, x2 - 1):
            mat_copy = down(mat, mat_copy, i, y2 - 1)
        # print(mat_copy)

        # 이동한 영역에서 최솟값 추출하여 리스트에 담는다.
        min_num = 10_001
        for i in range(rows):
            min_num = min(min_num, *mat_copy[i])
        answer.append(min_num)

        # 이동하면 행렬을 업데이트한다.
        for i in range(rows):
            for j in range(columns):
                if mat_copy[i][j] != 10_001:
                    mat[i][j] = mat_copy[i][j]
        # print(mat)

    return answer