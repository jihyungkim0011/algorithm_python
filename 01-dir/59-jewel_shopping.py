from collections import defaultdict


def solution(gems):
    answer = []

    need = len(set(gems))
    gems_count = defaultdict(int)
    # print(gems_count)
    left = 0
    answer = [1, len(gems)]

    for right in range(len(gems)):
        gems_count[gems[right]] += 1

        while len(gems_count) == need:
            if right - left + 1 < answer[1] - answer[0] + 1:
                answer = [left + 1, right + 1]

            gems_count[gems[left]] -= 1

            if gems_count[gems[left]] == 0:
                del gems_count[gems[left]]

            left += 1

    return answer