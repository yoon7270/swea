import sys
sys.stdin = open("input5_sample.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    N, w1, w2 = list(map(int, input().split()))
    li = list(map(int, input().split()))
    wl1, wl2 = [], []
    switch = 1
    result = 0
    li.sort()
    for i in li[::-1]:
        if not switch and len(wl1) < w1:
            wl1.append(i)
            if len(wl2) != w2:
                switch = 1
            continue
        if switch and len(wl2) < w2:
            wl2.append(i)
            if len(wl1) != w1:
                switch = 0
            continue
    for idx, v in enumerate(wl1):
        result += (idx+1) * v
    for idx, v in enumerate(wl2):
        result += (idx+1) * v
    print(f"#{test_case} {result}")