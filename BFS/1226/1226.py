# 1226. [S/W 문제해결 기본] 7일차 - 미로1
from pprint import pprint
import sys
sys.stdin = open("input.txt", "r")

# T = int(input())
# for test_case in range(1, T + 1):

count = input()

grid = []

start = None

for i in range(16):
    temp = list(map(int,input().split()))
    if temp in 2:
        start = (i,temp.index(2))
    grid.append(temp)

pprint(grid)
print(start)       