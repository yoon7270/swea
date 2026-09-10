import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    text = input()
    li = []
    text = text[::-1]
    for i in range(len(text)):
        if text[i] == 'b':
            li.append('d')
        if text[i] == 'd':
            li.append('b')
        if text[i] == 'p':
            li.append('q')
        if text[i] == 'q':
            li.append('p')
    print(f"#{test_case} {''.join(li)}")

