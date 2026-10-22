from itertools import combinations


def solution(n, q, ans):
    answer = 0

    # 뽑는 경우의 수
    for k in combinations([i for i in range(1, n + 1)], 5):

        counts = []

        # q에서 입력한 정수 묶음 가져오기
        for i in range(len(q)):
            cur_nums = k

            count = 0
            # 입력한 정수 중에 답과 똑같은 것은 저장한다.
            for j in range(5):
                if q[i][j] in cur_nums:
                    count += 1

            counts.append(count)

        if ans == counts:
            answer += 1

    # print('q ', q)
    # print('counts ', counts)

    return answer

# 입력한 정수의 길이는 항상 5
# dfs


