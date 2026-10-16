
def solution(node, computers):
    stack = []
    visited = set()
    network_count = 0

    for i in range(node):
        if i not in visited:
            network_count += 1
            stack.append(i)

            while stack:
                trace_index = stack.pop()
                for j in range(len(computers[trace_index])):
                    if j not in visited and computers[trace_index][j] == 1:
                        stack.append(j)
                        visited.add(j)
    return network_count


print(solution(3, [[1,1,0],[1,1,0],[0,0,1]])) # 2
print(solution(3, [[1,1,0],[1,1,1],[0,1,1]])) # 1
print(solution(4, [[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1]])) # 2
print(solution(3, [[1, 0, 1], [0, 1, 1], [1, 1, 1]])) # 1

