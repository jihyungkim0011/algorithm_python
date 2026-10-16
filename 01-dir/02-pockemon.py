def solution(nums):
    answer = 0
    n = len(nums) / 2

    hash = {}

    for num in nums:
        if num in hash:
            hash[num] += 1
        else:
            hash[num] = 1

    for pick in range(0, int(n + 1)):
        if len(hash) == pick:
            answer = pick
            break
        elif len(hash) < pick:
            answer = len(hash)
            break
        else:
            answer = pick

    return answer


if __name__ == "__main__":
    nums = [3, 1, 2, 3]
    print(solution(nums))  # Expected output: 2
    nums = [3, 3, 3, 2, 2, 4]
    print(solution(nums))  # Expected output: 3
    nums = [3, 3, 3, 2, 2, 2]
    print(solution(nums))  # Expected output: 2
