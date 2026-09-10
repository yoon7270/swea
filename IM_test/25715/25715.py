import sys
sys.stdin = open("input6_sample.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    freight, top = list(map(int, input().split()))
    hl, pl, top_v, kya = [], [], [], []
    for _ in range(top):
        h, p = list(map(int, input().split()))
        hl.append(h)
        pl.append(p)
    li = list(map(int, input().split()))
    for i in range(top):
        for j in range(1, hl[i]+1):
            top_v.append(j * pl[i])
    top_v.sort()
    li.sort(reverse=True)
    for n in range(len(li)):
        kya.append(top_v[n] * li[n])
    result = sum(kya)
    print(f"#{test_case} {result}")