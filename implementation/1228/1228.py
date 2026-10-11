# 1228. [S/W 문제해결 기본] 8일차 - 암호문1
import sys
sys.stdin = open("input.txt", "r")
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    PW = list(map(int, input().split()))
    CN = int(input())
    s = list(input().split())
    