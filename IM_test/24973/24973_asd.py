import sys
sys.stdin = open("input.txt", "r")

from itertools import count
dxy = [[0,1],[1,0],[0,-1],[-1,0]]
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    map_list = [list(map(int, input().split())) for _ in range(N)]
    max_num, max_step, max_list = 0, 0, []
    for i in range(N):
        for j in range(N):
            if map_list[i][j] > max_num:
                max_num = map_list[i][j]
    for i in range(N):
        for j in range(N):
            if map_list[i][j] == max_num:
                max_list.append([i, j])
    for i in max_list:
        y, x = i
        for _ in count():
            step = 1
            min_cl = map_list[y][x]
            sy, sx = -1, -1
            for dx, dy in dxy:
                if 0 <= y+dy < N and 0 <= x+dx < N:
                    if map_list[y+dy][x+dx] < min_cl:
                        min_cl = map_list[y + dy][x + dx]
                        sy, sx = y + dy,x + dx
            if sy != -1:
                y, x = sy, sx
                step += 1
            else:
                break
        max_step = max(step, max_step)
    print(f"#{test_case} {max_step}")