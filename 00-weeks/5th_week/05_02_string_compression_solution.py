input = "abcabcabcabcdededededede"

def string_compression(string):
    n = len(string)
    result = n

    for split_size in range(1, n // 2 + 1):
        splited = [
            string[i: i + split_size] for i in range(0, n, split_size)
        ]

        count = 1
        compressed = ""
        for i in range(len(splited) - 1):
            cur, next = splited[i], splited[i + 1]

            if cur == next:
                count += 1
            else:
                if count == 1:
                    compressed += f"{cur}"
                else:
                    compressed += f"{count}{cur}"
                count = 1

        if count > 1:
            compressed += f"{count}{splited[-1]}"
        else:
            compressed += f"{splited[-1]}"
        result = min(len(compressed), result)

    return result


print(string_compression(input))  # 14 가 출력되어야 합니다! 2abcabc2dedede

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA")) # J3A
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA")) # AZ3AZDW3A
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))



