from collections import deque
from itertools import product


def solution(queue1, queue2):
    len_queue = len(queue1)
    deque1 = deque(queue1)
    deque2 = deque(queue2)

    purpose, rest = divmod(sum(queue1) + sum(queue2), 2)
    if rest:
        return -1

    # print(purpose)

    # 두 큐의 원소합 / 2 이 되도록 맞춘다.

    def move_element(from_deque, to_deque):
        element = from_deque.popleft()
        to_deque.append(element)
        return element

    count = 0
    sum1 = sum(deque1)
    while count < 4 * len_queue:
        if sum1 == purpose:
            return count

        elif sum1 > purpose:
            element = move_element(deque1, deque2)
            sum1 -= element

        elif sum1 < purpose:
            element = move_element(deque2, deque1)
            sum1 += element

        count += 1

    return -1