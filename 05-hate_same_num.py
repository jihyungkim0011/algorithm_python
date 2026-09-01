def solution(arr):
    answer = []

    for i in arr:
        print(answer[-1:])
        if answer[-1:] == [i]:
            continue
        answer.append(i)

        # breakpoint()

    return answer


if __name__ == "__main__":
    arr = [1, 1, 3, 3, 0, 1, 1]
    print(solution(arr))  # Expected output: [1, 3, 0, 1]

    arr = [4, 4, 4, 3, 3]
    print(solution(arr))  # Expected output: [4, 3]
