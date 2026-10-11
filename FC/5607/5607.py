# 5607. [Professional] 조합
import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N, R = map(int, input().split())
    N_result = 0
    R_result = R
    cnt = 0
    for i in range(1, R_result):
        N_result = N * (N - i)
        N = N - i
        R = R * (R - i)
        R = R - i
    print(f"#{test_case} {int((N_result/R_result)%1234567891)}")