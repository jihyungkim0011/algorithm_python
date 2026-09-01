N = 5
arr = [[0] * N for _ in range(N)]

num = 0  # 배열에 넣을 숫자
row = 0  # 줄 위치
col = -1  # 칸 위치
size = N  # 배열 크기
step = 1  # 증가/감소 크기: 1, -1

while size > 0:
    for _ in range(size):  	# 가로로 이동
        col += step
        num += 1
        arr[row][col] = num
    size -= 1

    for _ in range(size):	# 세로로 이동
        row += step
        num += 1
        arr[row][col] = num
    step *= -1

for i in range(N):
    for j in range(N):
        print("%2d " % arr[i][j], end='')
    print()