def solution(sizes):
    w, h = 0, 0
    w_list = [size[0] for size in sizes]
    h_list = [size[1] for size in sizes]

    while True:
        max_w = max(w_list)
        max_h = max(h_list)

        current_index = h_list.index(max_h)

        if w_list[current_index] < h_list[current_index]:
            w_list[current_index], h_list[current_index] = h_list[current_index], w_list[current_index]
        else:
            break

    w = max(w_list)
    h = max(h_list)

    answer = w * h
    return answer


if __name__ == "__main__":
    sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
    print(solution(sizes))
    sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
    print(solution(sizes))
    sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
    print(solution(sizes))
