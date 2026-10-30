# 3431. 준환이의 운동관리
import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    L, U, X = map(int, input().split())
    if (L-X) > 0:
        result = (L-X)
    elif U <= X:
        result = -1
    elif X >= L:
        result = 0

    print(f"#{test_case} {result}")