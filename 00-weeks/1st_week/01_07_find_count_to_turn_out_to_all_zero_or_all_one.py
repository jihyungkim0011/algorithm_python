input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    zero_bundle = 0
    one_bundle = 0

    numbers = list(map(int, string))

    for index in range(1, len(numbers)):
        if numbers[index - 1] != numbers[index]:
            if numbers[index - 1] == 0:
                zero_bundle += 1
            else:
                one_bundle += 1

        if index == len(numbers) - 1:
            if numbers[index] == 0:
                zero_bundle += 1
            else:
                one_bundle += 1

    return min(zero_bundle, one_bundle)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)