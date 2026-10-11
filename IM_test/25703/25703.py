import pprint
import sys
sys.stdin = open("input.txt", "r")
dxy = [[0,1],[1,0],[0,-1],[-1,0]]
T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    li = [list(map(int, input().split())) for _ in range(N)]
    sum_li = []
    for i in range(N):
        for j in range(M):
            plus_dist = li[i][j]
            sum_num = plus_dist
            for pd in range(1, plus_dist + 1):
                for dx, dy in dxy:
                    if 0 <= j + dx * pd < M and 0 <= i + dy * pd < N:
                        sum_num += li[i + dy * pd][j + dx * pd]
            sum_li.append(sum_num)
    print(f"#{test_case} {max(sum_li)}")








