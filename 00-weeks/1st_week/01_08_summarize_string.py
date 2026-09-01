def summarize_string(string):
    count_list = [0] * 26
    result = ""

    for char in string:
        index = ord(char) - ord("a")
        count_list[index] += 1

    for index, element in enumerate(count_list):
        if element != 0:
            result += "{}{}/".format(chr(index + ord("a")), element)

    result = result[:-1]
    return result


input_str = "acccdeee"

print(summarize_string(input_str))