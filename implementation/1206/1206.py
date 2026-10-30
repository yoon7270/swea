# 1206. [S/W 문제해결 기본] 1일차 - View
import sys
sys.stdin = open("input.txt", "r")
T = 10
for test_case in range(1, T + 1):
    target_text = input()
    long_text = input()
    cnt = 0
    for i in long_text:
        if i in target_text:     
            s_cnt = 0
            for j in target_text:
                if i == j:
                    s_cnt += 1
                    break
                
