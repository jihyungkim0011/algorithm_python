def solution(participant, completion):

    part_dict = {}
    temp = 0

    for i in participant:
        part_dict[hash(i)] = i
        temp += hash(i)
    for i in completion:
        temp -= hash(i)

    answer = part_dict[temp]

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
