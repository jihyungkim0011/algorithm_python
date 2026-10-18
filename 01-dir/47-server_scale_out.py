def solution(players, m, k):
    answer = 0

    server_on = [0] * 24

    for i in range(0, 24):
        need = players[i] // m

        if need >= 1:
            if server_on[i] < need:
                add_server = need - server_on[i]
                answer += add_server

                for j in range(i, i + k):
                    if j < 24:
                        server_on[j] += add_server

    return answer


