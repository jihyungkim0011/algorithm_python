def solution(n, lost, reserve):
    answer = 0
    lost_s = set(lost) - set(reserve)  # 도난 당하고 여벌 없는 학생
    reserve_s = set(reserve) - set(lost)  # 체육복을 빌려줄 수 있는 학생

    # 도난 당한 학생들이 체육복 빌릴 수 있는지 검사
    for i in sorted(lost_s):
        # 앞번호 학생한테 빌리기
        if i - 1 in reserve_s:
            reserve_s.remove(i - 1)  # 체육복 빌리기
            lost_s.remove(i)  # 도난당한 리스트에서 제거
        # 뒷번호 학생한테 빌리기
        elif i + 1 in reserve_s:
            reserve_s.remove(i + 1)
            lost_s.remove(i)

    # 전체 학생 수 - 체육복 못 빌린 학생 수
    answer = n - len(lost_s)
    return answer


# print(solution(5, [3], [3]))  # 5
# print(solution(5, [2, 4], [1, 3, 5]))  # 5
# print(solution(5, [2, 3, 4], [3]))  # 3
# print(solution(5, [2, 4], [3]))  # 4
# print(solution(6, [1, 4, 6], [1, 5]))  # 5
