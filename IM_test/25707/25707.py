import sys
sys.stdin = open("input3_sample.txt", "r")
import itertools
T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    awn = list(map(int, input().split()))
    li = [list(map(int, input().split()))for _ in range(N)]
    ch, sc = [], 0
    for i in range(N):
        sch = []
        for j in range(M):
            if li[i][j] == awn[j]:
                sc += 1
                sch.append(sc)
            else:
                sc = 0
        sc = 0
        ch.append(sch)
    print(f"#{test_case} {sum(max(ch)) - sum(min(ch))}")