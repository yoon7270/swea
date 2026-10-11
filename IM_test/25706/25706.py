# 25706. 차르붐바2
import sys
sys.stdin = open("input.txt", "r")
plus_dxy = [[0,1],[-1,0],[0,-1],[1,0]]
cross_dxy = [[1,1],[-1,1],[-1,-1],[1,-1]]
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    map_list = [list(map(int, input().split())) for _ in range(N)]
    pp_max = 0
    for i in range(N):
        for j in range(M):
            dist = map_list[i][j]
            p_max, c_max = dist, dist  
            for d in range(1, dist+1):
                for pdy, pdx in plus_dxy:
                    dpdy, dpdx = pdy * d, pdx * d
                    if 0 <= i + dpdy < N and 0 <= j + dpdx < M:
                        p_max = p_max + map_list[i + dpdy][j + dpdx]
                for cdy, cdx in cross_dxy:
                    dcdy, dcdx = cdy * d, cdx * d
                    if 0 <= i + dcdy < N and 0 <= j + dcdx < M:
                        c_max = c_max + map_list[i + dcdy][j + dcdx]
                pp_max = max(pp_max, p_max, c_max)
    print(f"#{test_case} {pp_max}")