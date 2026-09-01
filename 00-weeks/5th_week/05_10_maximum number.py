from itertools import permutations
import re

def solution(expression):
    answer = 0

    operation_list = []
    if "*" in expression:
        operation_list.append("*")
    if "+" in expression:
        operation_list.append("+")
    if "-" in expression:
        operation_list.append("-")
    operation_permutations = list(permutations(operation_list))
    expression = re.split("([^0-9])", expression)

    for operation_permutation in operation_permutations:
        copied_expression = expression.copy()
        for operator in operation_permutation:
            while operator in copied_expression:
                operator_index = copied_expression.index(operator)

                cal = str(eval(
                    copied_expression[operator_index - 1] + copied_expression[operator_index] + copied_expression[operator_index + 1]
                ))
                copied_expression[operator_index - 1] = cal
                copied_expression = copied_expression[:operator_index] + copied_expression[operator_index + 2:]
        answer = max(answer, abs(int(copied_expression[0])))

    return answer


print(solution("100-200*300-500+20")) # 60420

