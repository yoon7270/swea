# 1220. [S/W 문제해결 기본] 5일차 - Magnetic
import sys
sys.stdin = open("input.txt", "r")


T = 10
for test_case in range(1, T + 1):
    leng = int(input())
    NS_table = [list(map(int, input().split())) for _ in range(leng)]
    G = []
    cnt = 0
    for i in range(leng):
        for j in range(leng-1):
            if NS_table[j][i] == 1 and not NS_table[j+1][i] == 2:
                
                

    print(f"#{test_case} {cnt}")
