input = "abcabcabcabcdededededede"

def string_compression(string):
    length = len(string)
    div = length // 2
    result_list = []

    while div > 0:
        array = []
        result = length
        chunk_1 = 0
        chunk_2 = div

        while chunk_2 < length:
            array.append(string[chunk_1 : chunk_2])
            chunk_1 += div
            chunk_2 += div
            if chunk_2 >= length:
                array.append(string[chunk_2 - div :])

        count = 0
        for i in range(1, len(array)):
            if array[i - 1] == array[i]:
                result -= div
                count += 1

                if i == len(array) - 1:
                    result += 1
            else:
                if count != 0:
                    result += 1
                count = 0

        result_list.append(result)
        div = div - 1

    return min(result_list)


print(string_compression(input))  # 14 가 출력되어야 합니다! 2abcabc2dedede

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA")) # J3A
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA")) # AZ3AZDW3A
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))



