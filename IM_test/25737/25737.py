import sys
sys.stdin = open("input11_sample.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    leng = int(input())
    li = list(map(int, input().split()))
    high = 1
    low = 1
    L = []
    for i in range(len(li)-1):
        if li[i+1] == li[i]:
            L.append(high)
            L.append(low)
            high, low = 1, 1
        elif li[i+1] < li[i]:
            low += 1
            L.append(low)
            high = 1
        elif li[i+1] > li[i]:
            high += 1
            L.append(high)
            low = 1
    print(f"#{test_case} {max(L)}")