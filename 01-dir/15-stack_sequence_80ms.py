# https://www.acmicpc.net/problem/1874
import sys

sys.stdin = open("input.txt")
###

def solve():
    n = int(sys.stdin.readline())
    # 우리가 만들어야 하는 목표 수열을 그대로 저장 (0번 인덱스부터 목표임)
    targets = [int(sys.stdin.readline()) for _ in range(n)]

    stack = []
    results = []
    current = 1  # 1부터 n까지 오름차순으로 넣을 숫자

    for target in targets:
        # 1. 목표 숫자가 나올 때까지 계속 push (+)
        while current <= target:
            stack.append(current)
            results.append("+")
            current += 1

        # 2. 스택 맨 위(stack[-1])가 내가 찾던 숫자(target)인가?
        if stack[-1] == target:
            stack.pop()
            results.append("-")
        else:
            # 3. 스택 맨 위가 target이 아닌데 current는 이미 넘었다면?
            # 이건 절대 못 만드는 수열!
            print("NO")
            return

    # 4. 루프를 다 돌았다면 성공! 한꺼번에 출력
    print("\n".join(results))

solve()
