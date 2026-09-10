import sys
from collections import deque
sys.stdin = open("input.txt", "r")
T = 10
for test_case in range(1, T+1):
    test = int(input())
    queue = deque(map(int, input().split()))
    cnt = 1
    while queue[-1] > 0:
        num = queue.popleft()
        if num - cnt > 0:
            queue.append(num - cnt)
        else:
            queue.append(0)
            break
        if cnt == 5:
            cnt = 0
        cnt += 1
    li = queue
    text = " ".join(map(str, li))
    print(f"#{test_case} {text}")