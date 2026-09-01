from curses.ascii import isalpha


def find_max_occurred_alphabet(string):
    array = [0] * 26
    answer = ""

    for char in string:
        if not isalpha(char):
            continue
        else:
            index = ord(char) - ord("a")
            array[index] += 1

    maximum = max(array)
    for index in range(0,len(array)):
        if array[index] == maximum:
            answer = chr(index + ord("a"))
            break

    return answer


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))


def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not isalpha(char):
            continue
        else:
            index = ord(char) - ord("a")
            alphabet_occurrence_array[index] += 1

    return alphabet_occurrence_array


print("정답 = [1, 0, 2, 2, 2, 0, 2, 1, 3, 0, 0, 2, 2, 3, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0] \n현재 풀이 값 =",
      find_alphabet_occurrence_array("hello my name is dingcodingco"))
print("정답 = [1, 0, 0, 0, 2, 0, 1, 1, 1, 0, 0, 2, 1, 0, 2, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0] \n현재 풀이 값 =",
      find_alphabet_occurrence_array("we love algorithm"))
print("정답 = [0, 3, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 3, 2, 0, 0, 0, 1, 0] \n현재 풀이 값 =",
      find_alphabet_occurrence_array("best of best youtube"))