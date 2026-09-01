def solution(info, query):
    answer = []
    info_list = [[] for _ in range(len(info))]
    for i in range(len(info)):
        info_list[i] = list(info[i].split())

    query_list = [[] for _ in range(len(query))]
    for i in range(len(query)):
        query_list[i] = list(query[i].split())
        while "and" in query_list[i]:
            query_list[i].remove("and")

    stack  = []
    for query_index in range(len(query_list)):
        language, field, j_or_s, food, score = query_list[query_index]

        if language == "-":
            language = ["cpp", "java", "python"]
        if field == "-":
            field = ["backend", "frontend"]
        if j_or_s == "-":
            j_or_s = ["junior", "senior"]
        if food == "-":
            food = ["chicken", "pizza"]

        query_changed_list = [language, field, j_or_s, food, score]

        count = 0
        turn = 0
        for info_index in range(len(info_list)):
            info_language = info_list[info_index][turn]
            if info_language in query_changed_list[0]:
                stack.append([info_index, turn + 1])

        while stack:
            info_index, turn = stack.pop()
            turn_info = info_list[info_index][turn]
            print(turn_info)
            print(query_changed_list[turn])
            if turn == 4:
                if int(turn_info) >= int(query_changed_list[turn]):
                    count += 1

            if turn != 4 and turn_info in query_changed_list[turn]:
                stack.append([info_index, turn + 1])

        answer.append(count)
    return answer


# 언어, 직군, 경력, 소울푸드 // 코딩점수


a = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
b = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(a, b)) # [1,1,1,1,2,4]