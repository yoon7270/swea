import sys


sys.stdin = open("s_input.txt", "r")
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    substation = [0 for _ in range(1, 5000 + 1)]
    result = []

    for _ in range(N):
        start, end = map(int, input().split())
        for number in range(start, end + 1):
            substation[number] += 1

    P = int(input())
    for _ in range(P):
        num = int(input())
        result.append(substation[num])

    answer = " ".join(map(str, result))
    print(f'#{test_case} {answer}')