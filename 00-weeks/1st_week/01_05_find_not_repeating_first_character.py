def find_not_repeating_first_character(string):
    array = [0] * 26

    for char in string:
        array_index = ord(char) - ord("a")
        array[array_index] += 1

    non_repeated_number_array = []
    for index in range(len(array)):
        if array[index] == 1:
            non_repeated_number = chr(index + ord("a"))
            non_repeated_number_array.append(non_repeated_number)

    for char in string:
        if char in non_repeated_number_array:
            return char

    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))

