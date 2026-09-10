import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    text = input()
    li = []
    for i in text:
        if li and li[-1] == i:
            li.pop()
        else:
            li.append(i)
    print(f"#{test_case} {len(li)}")