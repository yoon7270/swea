# 27736. 모든 수 방문하기 - IM
import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    n, s = list(map(int, input().split()))
    li = list(map(int, input().split()))
    sm, bi = min(li), max(li)
    if sm <= s <= bi:
        result = min((abs(bi - s) + (bi - sm)), (abs(sm - s) + (bi - sm)))
    elif s < sm :
        result = bi - s
    elif bi < s:
        result = s - sm
    print(f"#{test_case} {result}")