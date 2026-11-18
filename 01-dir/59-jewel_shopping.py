def solution(gems):
    answer = []
    candidate = []

    # 투포인터

    # set으로 중복 거르기
    original = set(gems)
    count_original = len(original)
    # print(count_original)
    # set의 크기에 따라 윈도우 크기 결정된다. 크기 이상으로.
    # left
    # right
    # 포인터 위치 설정. 곂쳐도 됨
    left = 0
    right = left + count_original

    while left < len(gems) - count_original:

        # 포인터까지 내부 set 추출
        window_gems = set(gems[left:right])

        # 원본가 동일한가
        #     동일하면 출력
        #     아니면 다음 포인터 이동
        if len(window_gems.intersection(original)) == count_original:
            candidate.append([left, right, right - left])

        if right >= len(gems):
            left += 1
            right = left + count_original
        else:
            right += 1

    candidate = sorted(candidate, key=lambda x: x[2])
    print(candidate)
    answer.append(candidate[0][0] + 1)
    answer.append(candidate[0][1])

    return answer