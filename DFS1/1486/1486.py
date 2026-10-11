# 1486. 장훈이의 높은 선반
import sys
sys.stdin = open("input.txt", "r")



import itertools
T = int(input())
for test_case in range(1, T + 1):
    N, B = list(map(int, input().split()))
    S = list(map(int, input().split()))
    li = []
    for i in range(1, len(S)+1):
        H = itertools.combinations(S, i)
        for j in H:
            k = sum(j)
            if k >= B:
                li.append(k)
    print(f"#{test_case} {min(li) - B}")
