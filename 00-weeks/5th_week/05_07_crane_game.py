

def solution(board, moves):
    n = len(board)
    answer = 0
    stack = [[] for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(n):
            if board[i][j] == 0:
                continue
            stack[j].append(board[i][j])

    bucket = []
    last_bucket_item = 0
    current_bucket_item = 0
    for move in moves:
        if not stack[move - 1]:
            continue
        current_bucket_item = stack[move - 1].pop()
        bucket.append(current_bucket_item)

        if last_bucket_item == current_bucket_item:
            answer += 2
            bucket.pop()
            bucket.pop()
            if not bucket:
                last_bucket_item = 0
            else:
                last_bucket_item = bucket[-1]
        else:
            last_bucket_item = current_bucket_item

    return answer



board = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves)) # 4 가 출력되어야 합니다.