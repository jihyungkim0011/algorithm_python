from collections import defaultdict
import math


def solution(fees, records):
    answer = []
    len_records = len(records)

    logs = []
    for i in range(len_records):
        logs.append(list(records[i].split()))

    # print(logs)

    in_car = {}
    fee_dict = defaultdict(int)

    #     차량번호와 입차를 확인하고 시간을 확인한다.
    #     같은 차량번호의 출차를 확인하고 얼마동안 있었는지 계산한다.
    #     180 이내면 기본요금. 180 지나면 기본요금 + 10분당 600 계산한다.
    #     차량번호 딕셔너리 += 요금
    for i in range(len_records):
        time, car_num, io = logs[i]
        h, m = time.split(":")
        # print(h, m)
        minutes = int(h) * 60 + int(m)
        # print(minutes)

        if io == "IN":
            in_car[car_num] = minutes

        if io == "OUT" and car_num in in_car.keys():
            fee_dict[car_num] += minutes - in_car[car_num]
            in_car.pop(car_num)
    #     출차 기록이 없으면 23:59까지 주차한 것으로 간주한다.
    if in_car.keys():
        for k, v in in_car.items():
            fee_dict[k] += 23 * 60 + 59 - v

    for k, v in fee_dict.items():
        if v > fees[0]:
            answer.append([int(k), fees[1] + math.ceil((v - fees[0]) / fees[2]) * fees[3]])
        else:
            answer.append([int(k), fees[1]])

    #     차량번호 작은 순으로 정렬한다.
    #     정렬하여 주차요금만 리스트로 반환한다.
    answer = sorted(answer, key=lambda x: x[0])
    # print(answer)

    result = []
    for i in answer:
        result.append(i[1])

    return result