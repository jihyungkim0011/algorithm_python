def solution(participant, completion):
    answer = ""
    part_dict = {}

    for i in participant:
        part_dict[i] = 0
    # print(part_dict)

    for i in participant:
        part_dict[i] += 1
    # print(part_dict)

    for i in completion:
        if part_dict[i] != 0:
            part_dict[i] -= 1
    # print(part_dict)

    for i in part_dict:
        if part_dict[i] != 0:
            answer = i

    return answer


if __name__ == "__main__":
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    print(solution(participant, completion))  # Expected output: "leo"
    participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
    completion = ["josipa", "filipa", "marina", "nikola"]
    print(solution(participant, completion))  # Expected output: "vinko"
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    print(solution(participant, completion))  # Expected output: "mislav"
