
n = int(input())

arr = [[0] * n for _ in range(n)]
# print(arr)

count = 0

for i in range(n):
	for j in range(n):
		count += 1
		arr[i][j] = count

	print(" ".join(str(arr[i][k]) for k in range(n)))




