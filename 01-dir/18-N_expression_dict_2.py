def solution(N, number):
    if N == number:
        return 1

    memo = {i: {int(str(N) * i): True} for i in range(1, 9)}

    for i in range(2, 9):
        for j in range(1, i):
            for num1 in memo[j]:
                for num2 in memo[i - j]:
                    memo[i][num1 + num2] = True
                    memo[i][num1 - num2] = True
                    memo[i][num1 * num2] = True
                    if num2 != 0:
                        memo[i][num1 // num2] = True

        if number in memo[i]:
            return i

    return -1

print(solution(5, 12)) # 4
print(solution(2, 11)) # 3
