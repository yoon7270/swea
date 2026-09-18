# 9367. 점점 커지는 당근의 개수
import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))
    cnt = 1
    li = []
    for i in range(1, N):
        if (C[i-1]) < C[i]:
            cnt += 1
        else:
            li.append(cnt)
            cnt = 1
    li.append(cnt)
    print(f"#{test_case} {max(li)}")