def solution(name):
    answer = 0
    alphabets = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
        "W", "X", "Y", "Z"
    ]

    length_name = len(name)
    count = 0

    for letter in name:
        i = alphabets.index(letter)
        i_back = i - 26

        if i != min(abs(i_back), i):
            i = abs(i_back)

        count += i
    # print(count)

    move = length_name - 1
    for k in range(length_name):
        next = k + 1
        while next < length_name and name[next] == "A":
            next += 1

        move = min(
            move,
            2 * k + length_name - next,
            (length_name - next) * 2 + k
        )

    answer = count + move

    return answer

print(solution("JEROEN")) # 56
print(solution("JAN")) # 23
