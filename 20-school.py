def solution(m, n, puddles):
    mod_value = 1_000_000_007

    memo = [[0] * m for _ in range(n)]
    memo[0][0] = 1

    for i in range(n):
        for j in range(m):

            if [j + 1, i + 1] in puddles:
                memo[i][j] = 0
                continue

            if i == 0 and j == 0:
                continue
            elif i == 0 and j != 0:
                memo[0][j] = memo[0][j - 1]
            elif i != 0 and j == 0:
                memo[i][0] = memo[i - 1][0]
            else:
                memo[i][j] = (memo[i][j - 1] + memo[i -1][j]) % mod_value


    return memo[n - 1][m - 1] % mod_value

print(solution(4, 3, [[2, 2]])) # 4
print(solution(3, 3, [[2, 1]])) # 3
print(solution(3, 3, [[2, 3]])) # 3
print(solution(3, 3, [[2, 2]])) # 2
print(solution(2, 1, [])) # 1


  # m, n     m + 1, n
  # m, n + 1
