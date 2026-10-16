def solution(N, number):
    if N == number:
        return 1

    memo = [set() for _ in range(9)] # set은 중복없이 저장할 수 있다.

    for i in range(1, 9):
        memo[i].add(int(str(N) * i)) # set.add()는 원소를 추가할 수 있다.

        for j in range(1, i):
            for num1 in memo[j]:
                for num2 in memo[i - j]:
                    memo[i].add(num1 + num2)
                    memo[i].add(num1 - num2)
                    memo[i].add(num1 * num2)
                    if num2 != 0:
                        memo[i].add(num1 // num2)

        if number in memo[i]:
            return i

    return -1

print(solution(5, 12)) # 4
print(solution(2, 11)) # 3
