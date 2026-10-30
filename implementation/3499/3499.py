# 3499. 퍼펙트 셔플
import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    leng = int(input())
    ch = list(input().split())
    result = []
    g = int(leng / 2)
    if leng % 2 == 1:
        g += 1
    frch = ch[0:g]
    bcch = ch[g::]
    for i in range(leng):
        if i % 2 == 0:
            result.append(frch[int(i/2)])
        else:
            result.append(bcch[int(i/2)])
    print(f"#{test_case} {' '.join(result)}")