import sys

def validate_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, n-1, 2):
        if n % i == 0:
            return False
    return True

def count_prime(numbers):
    return sum(1 for i in numbers if validate_prime(i))

def main():
    N, numbers = input()

    result = count_prime(numbers)

    print(result)


def input() -> list[int]:
    sys.stdin = open("input.txt")

    input = sys.stdin.readline
    N = int(input())
    numbers = list(map(int, input().split()))
    return [N, numbers]


if __name__ == "__main__":
    main()

# 7
# 1 2 3 5 7 8 9
# solution: 4