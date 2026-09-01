top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    result = []

    for i in range(len(heights)):
        stack_position = []

        for compare_index in range(i):
            if heights[i] <= heights[compare_index]:
                stack_position.append(compare_index + 1)

        if not stack_position:
            result.append(0)
        else:
            result.append(stack_position.pop())

    return result


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 2, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))