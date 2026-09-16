# 4837. [S/W 문제해결 기본] 2일차 - 부분집합의 합
import sys
sys.stdin = open("input.txt", "r")
import itertools
T = int(input())
o2t = [1,2,3,4,5,6,7,8,9,10,11,12]
for test_case in range(1, T + 1):
    N, K = list(map(int, input().split()))
    li = itertools.combinations(o2t, N)
    result = []
    for i in li:
        if sum(i) == K:
            result.append(i)
    print(f"#{test_case} {len(result)}")