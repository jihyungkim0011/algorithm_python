input = 2


def find_prime_list_under_number(number):
    prime_list = []

    for n in range(2, number + 1): # 2부터 number까지 반복
        for i in prime_list: # 소수만으로 나눈다.(개선)
            if i * i <= n and n % i == 0: # 제곱근 밑으로만 나눈다. & 나누어 떨어지면
                break                     # for문 멈추기
        else:
            prime_list.append(n)          # for문에서 break 되지 않으면 리스트에 추가하기

    return prime_list


result = find_prime_list_under_number(input)
print(result)