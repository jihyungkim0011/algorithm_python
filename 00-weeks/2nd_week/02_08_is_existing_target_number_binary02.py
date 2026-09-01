finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# N -> N/2 -> N/4 -> ... -> N/2^k : 1개 도달까지라면 N/2^k = 1 -> k = log2(N)
# 이진탐색은 O(logN)이다
def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_guess <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

    return False



result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)