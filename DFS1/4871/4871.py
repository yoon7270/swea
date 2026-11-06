# 4871. [S/W 문제해결 기본] 4일차 - 그래프 경로
import sys
sys.stdin = open("input.txt", "r")

def num_find(S, G, li):
    if S == G:
        return 1
    
    for i, j in li:
        if i == S:
            if num_find(j, G, li):
                return 1

    return 0

    

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    result = num_find(S, G, li)
    print(f"#{test_case} {result}")