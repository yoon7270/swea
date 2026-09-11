import sys
sys.stdin = open("input.txt", "r")

# 강사님 지분 120%
# 나는 아무것도 안했따.
# 강사님이 다 풀어줬다.


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
    max_step = 0
    for i in start_list:
        y, x = i
        step = 1
        for _ in count():
            min_number = map_list[y][x]  # 시작 지점
            sy, sx = -1, -1  # 나보다 작은 값의 좌표 (초기값 -1로 놓는다.)
            for dy, dx in dxy:
                if 0 <= x+dx < N and 0 <= y+dy < N:  # 범위 안에 들어가면
                    if map_list[y+dy][x+dx] < min_number:  # 주변 좌표가 현재 좌표보다 작으면
                        min_number = map_list[y+dy][x+dx]  # 작은 값으로 갱신
                        sy, sx = y+dy, x+dx  # 작은 값의 좌표 갱신

            # 4방향을 다 봤음
            if sy != -1:  # 현재 나보다 낮은 값을 가진 좌표를 찾았다!
                x, y = sx, sy
                step += 1
            else:  # 못 찾아서 sy 가 갱신이 안돼서, 그대로 -1 값을 가지고 있는 경우 ==> 포문 나간다 => 브레이크
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