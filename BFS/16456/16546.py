import sys
sys.stdin = open("input.txt", "r")
import itertools
T = int(input())
for test_case in range(1, T+1):
    li = list(map(int, input().strip()))
    Tu = tuple(itertools.permutations(li))
    for pram in Tu:
        fr, ba = 0, 0
        if not fr and pram[0]+1 == pram[1] and pram[1]+1 == pram[2]:
            fr = 1
        if not ba and pram[3]+1 == pram[4] and pram[4]+1 == pram[5]:
            ba = 1
        if not fr and pram[0] == pram[1] == pram[2]:
            fr = 1
        if not ba and pram[3] == pram[4] == pram[5]:
            ba = 1
        if fr == 1 and ba == 1:
            print(f"#{test_case} true")
            break
    if fr == 0 and ba == 0:
        print(f"#{test_case} false")
