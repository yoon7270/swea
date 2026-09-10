import sys
sys.stdin = open("input.txt", "r")
T = 10
for test_case in range(1, T+1):
    length = int(input())
    li = list(input())
    num = []
    code = []
    for i in li:
        if i.isdigit():
            num.append(i)
        elif i == '+' or i == '*':
            if code and code[-1] ==
    print(''.join(map(str, num)))