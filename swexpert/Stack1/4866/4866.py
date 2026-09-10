import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
pairs = {'}':'{', ']':'[', ')':'('}
for test_case in range(1, T+1):
    stack = []
    line = input()
    for i in line:
        if i in pairs.values(): stack.append(i)
        elif i in pairs.keys():
            if stack and stack[-1] == pairs.get(i): stack.pop()
            else: stack.append(i)
    if not stack: print(f"#{test_case} 1")
    else: print(f"#{test_case} 0")