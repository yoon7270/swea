# 10726. 이진수 표현
import sys
sys.stdin = open("input.txt", "r")
from itertools import count
T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    li = []
    for i in range(N):
        if M == 0:
            break
        for j in count():
            if 2**j >= M:
                li.append(1)
                M = M - 2**(j-1)
    if 0 in li:
        result = "OFF"
    else:
        result = "ON"
    print(f"#{test_case} {result}")
