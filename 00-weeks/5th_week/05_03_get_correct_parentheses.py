from collections import deque

balanced_parentheses_string = "()))((()"


def get_correct_parentheses(balanced_parentheses_string):
    if balanced_parentheses_string == "": return ""
    count = 0
    stack = []
    state = True
    result = ""

    for i in range(len(balanced_parentheses_string)):
        if balanced_parentheses_string[i] == "(":
            count += 1
            stack.append(True)
        else:
            count -= 1
            if len(stack) == 0:
                state = False # 올바르지 않다
            else:
                stack.pop()

        if count == 0:
            u =  balanced_parentheses_string[:i + 1]
            v = balanced_parentheses_string[i + 1:]

            if state:
                result += u
                return result + get_correct_parentheses(v)
            else:
                u = u[1:]
                u = u[:-1]
                queue = deque(u)
                changed_u = ""
                while queue:
                    if queue.popleft() == "(":
                        changed_u += ")"
                    else:
                        changed_u += "("

                empty = "(" + get_correct_parentheses(v) + ")" + changed_u

                return result + empty




print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))




