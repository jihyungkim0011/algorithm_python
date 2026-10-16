from collections import deque

def solution(node, computers):
    queue = deque([])
    visited = set()
    network_count = 0

    for i in range(node):
        if i not in visited:
            network_count += 1
            queue.append(i)

            while queue:
                trace_index = queue.popleft()
                for j, connection in enumerate(computers[trace_index]):
                    if j not in visited and connection == 1:
                        queue.append(j)
                        visited.add(j)
    return network_count


print(solution(3, [[1,1,0],[1,1,0],[0,0,1]])) # 2
print(solution(3, [[1,1,0],[1,1,1],[0,1,1]])) # 1
print(solution(4, [[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1]])) # 2
print(solution(3, [[1, 0, 1], [0, 1, 1], [1, 1, 1]])) # 1

