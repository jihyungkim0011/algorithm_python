import heapq


def solution(scoville, K):
    answer = 0
    temp = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) >= 2:
            answer += 1

            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            temp = a + b * 2
            heapq.heappush(scoville, temp)
        else:
            return -1
    return answer
