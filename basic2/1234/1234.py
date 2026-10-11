# 1234. [S/W 문제해결 기본] 10일차 - 비밀번호
import sys
sys.stdin = open("input.txt", "r")
T = 10
for test_case in range(1, T + 1):
    N, num_list = input().split()
    num = []
    for i in num_list:
        if num and num[-1] == i:
            num.pop()
        else:
            num.append(i)
    print(f"#{test_case} {''.join(num)}")