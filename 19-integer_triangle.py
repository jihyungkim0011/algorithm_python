import heapq

def solution(triangle):
    depth = len(triangle)
    sum_list = [[0] * (i + 1) for i in range(depth)]

    for i in range(depth): # 0
        for j in range(0, i + 1): # 0
            if i == 0 and j == 0:
                sum_list[i] = triangle[0]
            elif i != 0 and j == 0:
                sum_list[i][j] = triangle[i][j] + sum_list[i-1][j]
            elif j == i:
                sum_list[i][j] = triangle[i][j] + sum_list[i-1][j-1]
            else:
                sum_list[i][j] = triangle[i][j] + max(sum_list[i-1][j-1], sum_list[i-1][j])

    heap = []
    for i in sum_list[depth - 1]:
        heapq.heappush(heap, -1 * i)
    return -1 * heapq.heappop(heap)


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])) # 30