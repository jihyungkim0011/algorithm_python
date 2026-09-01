numbers = [1, 1, 1, 1, 1]
target_number = 3

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    cases =[]

    def get_all_case(array, current_index, current_sum):
        if current_index == len(array):
            cases.append(current_sum)
            return

        get_all_case(array, current_index + 1, current_sum + array[current_index])
        get_all_case(array, current_index + 1, current_sum - array[current_index])

    get_all_case(array, 0, 0)

    return cases.count(3)

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!
