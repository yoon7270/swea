# 25733. 단어 퍼즐의 교차점
import sys
sys.stdin = open("input.txt", "r")

import pprint
dxy = [[0, 1],[-1, 0],[0, -1],[1, 0]]
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    map_list = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if map_list[i][j] == 1:
                pm = []
                for dy, dx in dxy:
                    if 0 <= i + dy < N and 0 <= j + dx < N:
                        if map_list[i + dy][j + dx] == 1:
                            pm.append()
    pprint.pprint(map_list)
