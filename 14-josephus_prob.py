import sys

sys.stdin = open("input.txt")
###

def josephus_problem(n, k):
    sequence = [i for i in range(1,n + 1)]
    result = []

    delete_index = k - 1
    len_sequence = len(sequence)

    while sequence:
        if len_sequence == 1:
            result.append(sequence[0])
            break

        delete_element = sequence[delete_index]
        sequence.remove(delete_element)
        result.append(delete_element)
        len_sequence = len(sequence)

        delete_index = (delete_index + k - 1) % len_sequence

    string = "<" + ", ".join("{}".format(x) for x in result) + ">"

    return print(string)

N, K = map(int,input().split())
josephus_problem(N, K)
