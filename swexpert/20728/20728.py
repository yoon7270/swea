import sys
sys.stdin = open("sin.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    N, K = list(map(int, input().split()))
    candy = list(map(int, input().split()))
    if N == K:
        print(f"#{test_case} {max(candy) - min(candy)}")
        continue
    candy.sort(reverse=True)
    li = []
    for i in range(len(candy) - K + 1):
        li.append(candy[i] - candy[i+K-1])
    print(f"#{test_case} {min(li)}")