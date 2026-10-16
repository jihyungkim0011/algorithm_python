from collections import deque


def solution(node, computers):
    network_count = 0
    queue = deque()
    visited = [0] * node

    for i in range(node):
        if visited[i] != 1:
            network_count += 1

            queue.append(i)
            visited[i] = 1 # 큐에 넣었으면 방문했으므로 1로 바꾼다.

            while queue:
                current = queue.popleft()

                for k in range(node): # 기존에 range(k, node) 로 탐색했지만,
                                      # if에서 어차피 방문한 것을 확인하므로 전체를 탐색해도 된다.
                                      # 노드 순서로 연결돼있는 것이 아니라 2에서 1로 연결될 수 있기 때문이다.
                    if visited[k] != 1 and computers[current][k] == 1:
                        queue.append(k)
                        visited[k] = 1

    return network_count


print(solution(3, [[1,1,0],[1,1,0],[0,0,1]])) # 2
print(solution(3, [[1,1,0],[1,1,1],[0,1,1]])) # 1
print(solution(4, [[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1]])) # 2
print(solution(3, [[1, 0, 1], [0, 1, 1], [1, 1, 1]])) # 1

