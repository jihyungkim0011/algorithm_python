def solution(tickets):
    answer = []
    visited = [False] * len(tickets)

    def dfs(start, path):
        if (len(path) == len(tickets) + 1):
            answer.append(path)
            return

        for index, ticket in enumerate(tickets):
            if (ticket[0] == start) and not visited[index]:
                visited[index] = True
                dfs(ticket[1], path + [ticket[1]])
                visited[index] = False

    dfs("ICN", ["ICN"])

    answer.sort()

    return answer[0]

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

print(solution(tickets))
# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]