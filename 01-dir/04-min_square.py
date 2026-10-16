def solution(sizes):
    answer = 0

    w = 0
    h = 0

    for i in sizes:
        a = max(i)
        b = min(i)

        if a > w:
            w = a

        if h == 0:
            h = b
        elif b > h:
            h = b
        else:
            pass
        # breakpoint()

    answer = w * h
    return answer


if __name__ == "__main__":
    sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
    print(solution(sizes))
    sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
    print(solution(sizes))
    sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
    print(solution(sizes))
