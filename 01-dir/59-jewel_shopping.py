
from collections import defaultdict

def solution(gems):
    # 1. 전체 보석 종류 수
    need = len(set(gems))

    # 2. 현재 구간의 보석 개수
    gems_count = defaultdict(int)

    # 3. 포인터 및 정답 초기화
    left = 0
    answer = [1, len(gems)]

    # 4. 오른쪽 포인터를 이동하면서 구간 확장
    for right in range(len(gems)):
        gems_count[gems[right]] += 1

        # 5. 모든 종류를 포함하면 구간 축소
        while len(gems_count) == need:

            # 6. 정답 갱신
            if right - left + 1 < answer[1] - answer[0] + 1:
                answer = [left + 1, right + 1]

            # 7. 왼쪽 보석 제거
            gems_count[gems[left]] -= 1

            if gems_count[gems[left]] == 0:
                del gems_count[gems[left]]

            # 8. 왼쪽 포인터 이동
            left += 1

    return answer
