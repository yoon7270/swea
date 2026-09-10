import sys
sys.stdin = open("input.txt", "r")
dxy = [[0,1],[1,0],[0,-1],[-1,0]]
T = int(input())
for test_case in range(1, T+1):
    ms = int(input())
    map_list = [list(map(int, input().split())) for _ in range(ms)]
    max_num = max(max(map_list))
    goal = min(min(map_list))
    start = []
    cnt = 0
    for i in range(ms):
        for j in range(ms):
            if map_list[i][j] == max_num:
                start.append([i,j])
    for k in start:
        i, j = k
        cl = map_list[i][j]
        while cl != goal:
            th = []
            for xy in dxy:
                x, y = xy
                th.append(map_list[i+x][j+y])
            x, y = dxy[th.index(min(th))]
            i, j = i+x, j+y
            cnt += 1
        print(cnt)