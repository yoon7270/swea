import sys


sys.stdin = open("s_input.txt", "r")

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    stations = [0] * 5001

    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            stations[i] += 1

    p = int(input())

    locations = []
    for _ in range(p):
        c = int(input())
        locations.append(c)

    print(f'#{test_case} ', end='')

    for location in locations:
        print(stations[location], end=' ')

    print()