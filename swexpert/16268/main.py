import sys

sys.stdin = open("input1.txt", "r")

x = [0,1,0,-1]
y = [1,0,-1,0]

T = int(input())
for test_case in range(1, T+1):
    height, width = list(map(int, input().split()))
    num_map = [list(map(int, input().split())) for _ in range(height)]
    li = []
    for i in range(height):
        o_l = []
        for j in range(width):
            f_d = []
            f_d.append(num_map[i][j])
            for k in range(4):
                dx = i + x[k]
                dy = j + y[k]
                if dx < 0:
                    continue
                if dy < 0:
                    continue
                if dx >= height:
                    continue
                if dy >= width:
                    continue
                f_d.append(num_map[dx][dy])
            o_l.append(sum(f_d))
        li.append(max(o_l))
    print(f"#{test_case} {max(li)}")