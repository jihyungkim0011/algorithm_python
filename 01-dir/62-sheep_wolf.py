def solution(info, edges):
    answer = 0

    children = [[] for _ in range(len(info))]
    for parent, child in edges:
        children[parent].append(child)

    stack = [(1, 0, children[0])]

    while stack:
        sheep, wolf, nodes = stack.pop()
        answer = max(answer, sheep)

        for i, node in enumerate(nodes):
            next_sheep = sheep + (1 if info[node] == 0 else 0)
            next_wolf = wolf + (1 if info[node] == 1 else 0)

            if next_wolf >= next_sheep:
                continue

            next_nodes = nodes[:i] + nodes[i + 1:] + children[node]
            stack.append((next_sheep, next_wolf, next_nodes))

    return answer