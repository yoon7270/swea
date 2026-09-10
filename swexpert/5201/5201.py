import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    weight = list(map(int, input().split()))
    payload = list(map(int, input().split()))
    weight.sort()
    payload.sort()
    