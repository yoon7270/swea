import sys
sys.stdin = open("input7_sample.txt", "r")
import itertools, sys
T = int(input())


def main(N, li, cl, step):
    for i in range(1, sys.maxsize):
        step[cl] += 1
        if cl == 0:
            cl += 1
        elif step[cl] % 2 == 1 and cl > 0:
            cl = back(li, cl, step)
        elif step[cl] % 2 == 0 and cl != 0:
            cl += 1
        if cl == N - 1:
            return sum(step)
    return None
def back(li, cl, step):
    cl = li[cl] - 1
    if cl != 0:
        step[cl] += 1
        if step[cl] % 2 == 1 and cl > 0:
            cl = back(li, cl, step)
    return cl
for test_case in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    cl, step = 0, [0] * N
    result = main(N, li, cl, step)
    print(f"#{test_case} {result}")