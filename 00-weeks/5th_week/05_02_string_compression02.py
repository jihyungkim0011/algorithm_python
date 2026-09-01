input = "abcabcabcabcdededededede"


def string_compression(target_string: str) -> int:
    min_length = len(target_string)

    for chunk_size in range(1, len(target_string) // 2 + 1):
        split_chunks = [target_string[i:i + chunk_size] for i in range(0, len(target_string), chunk_size)]
        compressed_string, match_count = "", 1

        for i in range(1, len(split_chunks) + 1):
            if i < len(split_chunks) and split_chunks[i] == split_chunks[i - 1]:
                match_count += 1
            else:
                compressed_string += (
                    str(match_count) + split_chunks[i - 1] if match_count > 1 else split_chunks[i - 1])
                match_count = 1

        print(compressed_string)
        min_length = min(min_length, len(compressed_string))

    return min_length


print(string_compression(input))  # 14 가 출력되어야 합니다! 2abcabc2dedede

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA")) # J3A
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA")) # AZ3AZDW3A
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))



