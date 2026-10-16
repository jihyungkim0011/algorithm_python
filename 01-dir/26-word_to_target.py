from collections import deque


def solution(begin, target, words):
    word_len = len(begin)

    queue = deque([(begin, 0)])

    while queue:
        word_now, change = queue.popleft()

        if word_now == target:
            return change

        for word in words:
            count = 0

            for i in range(word_len):
                if word_now[i] == word[i]:
                    count += 1
            if count == word_len - 1:
                queue.append((word, change + 1))
                words.remove(word)

    return 0


# begin = "hit"
# target = "hot"
# count = 0
# for i in range(len(begin)):
#     if begin[i] == target[i]:
#         count += 1
# if count == len(begin) - 1:
#     begin = target
#
# print(begin)

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])) # 0