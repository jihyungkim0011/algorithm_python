def solution(brown, yellow):
    answer = []

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            a = yellow // i

            if a >= i:
                brown_a = a + 1
                brown_i = i + 1

                if (brown_a + brown_i) * 2 == brown:
                    answer = [brown_a + 1, brown_i + 1]

    return answer

print(solution(brown=10, yellow=2)) # [4,3]
print(solution(brown=8, yellow=1)) # [3,3]
print(solution(brown=24, yellow=24)) #[8,6]