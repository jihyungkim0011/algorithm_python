def is_correct_parenthesis(string):
    my_stack = []

    for index in range(len(string)):
        if string[index] == "(":
            my_stack.append(True)
        else:
            if not my_stack:
                return False
            my_stack.pop()

    if not my_stack:
        return True

    return False


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))
