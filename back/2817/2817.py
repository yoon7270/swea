# 2817. 부분 수열의 합
import sys
sys.stdin = open("input.txt", "r")

import itertools
T = int(input())
for test_case in range(1, T + 1):
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(1, N+1):
        H = itertools.combinations(A, i)
        for j in H:
            sum_j = sum(j)
            if sum_j == K:
                cnt += 1
    print(f"#{test_case} {cnt}")