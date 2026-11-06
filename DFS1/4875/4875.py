# 4875. [S/W 문제해결 기본] 5일차 - 미로
import sys
sys.stdin = open("input.txt", "r")

dxy = [[0,1],[1,0],[0,-1],[-1,0]]

def excape(i,j):
    pass
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    map_list = [list(input().split()) for _ in range(N)]
    print(map_list)
    