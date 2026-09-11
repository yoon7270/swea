import pprint
import sys
sys.stdin = open("input.txt", "r")
dxy = [[0,1],[1,0],[0,-1],[-1,0]]
T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    li = [list(map(int, input().split())) for _ in range(N)]






