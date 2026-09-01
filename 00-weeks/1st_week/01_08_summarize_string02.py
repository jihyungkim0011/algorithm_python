def summarize_string(target_string):

    n = len(target_string)
    count = 0
    result_str = ''

    for i in range(n - 1): # 0 부터 n-2 까지 (a c c c d e e)
        if target_string[i] == target_string[i + 1]: # a a 같으면 카운트 ++
            count += 1
        else:
            result_str += target_string[i] + str(count + 1) + '/' # a c 다르면 스트링+개수+/
            count = 0                                             # 이때 개수는 카운트에서 +1
                                                                  # 카운트 다시 초기화 = 0
    result_str += target_string[n - 1] + str(count + 1) # 마지막 인덱스의 알파벳 + 개수(카운트+1)

    return result_str


input_str = "acccdeee"

print(summarize_string(input_str))