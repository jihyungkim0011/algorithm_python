
def solution(answers):
    len_answers = len(answers)
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [[1, 0], [2, 0], [3, 0]]

    for i in range(len_answers):
        a = i % len(first)
        if first[a] == answers[i]:
            score[0][1] += 1
        b = i % len(second)
        if second[b] == answers[i]:
            score[1][1] += 1
        c = i % len(third)
        if third[c] == answers[i]:
            score[2][1] += 1

    max_score = max(score[i][1] for i in range(3))
    # print(max_score)

    answer = []
    for i in range(3):
        if score[i][1] == max_score:
            answer.append(i + 1)

    return answer


print(solution([1, 2, 3, 4, 5])) # [1]
print(solution([1,3,2,4,2])) # [1,2,3]
print(solution([4,4,4])) # [1,2,3]