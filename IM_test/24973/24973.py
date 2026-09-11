import sys
sys.stdin = open("input.txt", "r")

# 1. 최댓값(시작점), 최솟값(목적지)의 좌표를 구한다.
# 2. 최댓값의 수만큼 반복하는 for문을 작성한다.
# 3. 최댓값의 좌표마다 출발하여 주변의 최솟값으로 이동한다.
# 4. 이동하다가 목적지에 도착하면 break를 걸어 멈춘다.
# 5. 최댓값의 수만큼 돌려서 어떤 이동거리가 가장 긴지 판별 후 출력한다.

from itertools import count
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def find_min_max(map_list, N):
    max_num, max_list = 0, []
    for i in range(N):
        for j in range(N):
            if map_list[i][j] > max_num:
                max_num = map_list[i][j]
    for i in range(N):
        for j in range(N):
            if map_list[i][j] == max_num:
                max_list.append([i, j])
    return max_list
def delta(map_list, N, start_list):
    for i in start_list:
        y, x = i
        step, max_step = 1, 0
        for _ in count():
            min_number = map_list[y][x]
            for dy, dx in dxy:
                if 0 <= x+dx < N and 0 <= y+dy < N:
                    if map_list[y+dy][x+dx] < min_number:
                        min_number = map_list[y+dy][x+dx]
                        sy, sx = y+dy, x+dx
            if x != sx or y != sy:
                x, y = sx, sy
                step += 1
            else:
                break
        max_step = max(step, max_step)
    return max_step
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    map_list = [list(map(int, input().split())) for _ in range(N)]
    start_list = find_min_max(map_list, N)
    result = delta(map_list, N, start_list)
    print(f"#{test_case} {result}")