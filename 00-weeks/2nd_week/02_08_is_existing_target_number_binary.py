finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    length = len(array)
    standard = length // 2

    while standard > 1:
        if array[standard-1] == target:
            return True
        if target in array[standard:]:
            array = array[standard:]
        else:
            array = array[:standard]
        standard = standard // 2


    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)