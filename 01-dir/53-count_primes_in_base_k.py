from collections import deque


def solution(n, k):
    answer = 0

    #     소수 여부 판단 함수 작성한다.
    def is_prime(number):
        if number in [0, 1]:
            return False
        if number in [2, 3]:
            return True
        if number % 2 == 0:
            return False

        for i in range(2, int(number ** (1 / 2) + 1)):
            if number % i == 0:
                return False
        return True

    def convert(number, k):
        value = number
        result = deque()
        while value:
            value, rest = value // k, value % k
            result.appendleft(rest)

        return "".join(map(str, result))

    #     n을 k 진수로 변환한다. 변환된 수를 저장한다. converted
    converted = convert(n, k)
    # print(converted)

    #     converted에서 0을 기준으로 파싱한다.
    #     0이 없는 경우 덩어리 하나로 간주한다.
    #     파싱한 값들을 리스트에 저장해놓는다
    number_list = converted.split("0")
    # print(number_list)

    #     리스트 내에서 소수 여부 판단해서 소수의 개수를 반환한다.
    for num in number_list:
        if num != "" and is_prime(int(num)):
            answer += 1

    return answer