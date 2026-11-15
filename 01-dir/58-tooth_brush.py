from collections import defaultdict


def solution(enroll, referral, seller, amount):
    answer = []
    total = defaultdict(int)

    connection = {}
    for i in range(len(enroll)):
        connection[enroll[i]] = referral[i]

    # seller를 반복한다
    for i in range(len(seller)):
        # 이름을 enroll에서 찾는다.
        # print(name)
        # amount * 100 을 한다
        init = amount[i] * 100
        rest = init // 10
        total[seller[i]] += init - rest
        # print(init)

        # refferal에서 "-"가 나올때까지 반복한다.
        # 0.9*를 하여 갖는다 = 리스트에 저장한다.
        # 같은 인덱스의 referral을 찾는다.
        # 추천인에게 0.1을 갖는다.

        next_person = seller[i]
        while rest > 0:
            next_person = connection[next_person]
            # print(next_person)

            if next_person == "-":
                break
            all_rest = rest
            rest = rest // 10
            cost = all_rest - rest
            total[next_person] += cost

            # print(next_person)

    # print(total)

    for name in enroll:
        answer.append(total[name])
    print(answer)

    return answer