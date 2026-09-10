import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    A = int(input())
    time = [list(map(int, input().split())) for _ in range(A)]
    time.sort(key=lambda x: x[1])
    cnt = 1
    std = time[0][1]
    for i in time:
        if std > i[0]: continue
        std = i[1]
        cnt += 1
    print(f"#{test_case} {cnt}")