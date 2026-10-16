
#

def solution(number, target):
    memo = { 1: [number]}

    for i in range(1,9):
        if i not in memo.keys():
            memo[i] = []
        if i != 1:
            memo[i].append(int(str(number) * i))

        for j in range(1, i):

            for num1 in memo[i - j]:
                for num2 in memo[j]:

                    plus = num1 + num2
                    minus = num1 - num2 if num1 >= num2 else 0
                    times = num1 * num2
                    div = num1 // num2 if num2 != 0 else 0

                    for calculated in [plus, minus, times, div]:
                        memo[i].append(calculated)
        print(memo)
        if target in memo[i]:
            return i

    return -1

print(solution(5, 12)) # 4
print(solution(2, 11)) # 3


# i       1         2           2
# j       1         1           2
# num1    memo[0]   memo[1]
# num2    memo[1]   memo[1]