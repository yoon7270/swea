import pprint
import sys

sys.stdin = open("input1.txt", "r")

dxy = [[0,1],[1,0],[0,-1],[-1,0]]

T = int(input())
for test_case in range(1, T + 1):
    h, w = list(map(int, input().split()))
    files_map = [list(map(int, input().split())) for _ in range(h)]
    #pprint.pprint(files_map)
    for i in range(h):
        for j in range(w):
            dist = files_map[i][j]
            for dx, dy in dxy:
                if 0 < i < h or 0 < j < w:
                    break
                dist += files_map[i + dy * dist][j + dx * dist]
            print(dist)

