import sys
from collections import deque
sys.stdin = open("sample_input.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    N,M = list(map(int, input().split()))
    queue = deque(map(int, input().split()))
    for _ in range(M):
        queue.append(queue.popleft())
    print(f"#{test_case} {queue[0]}")