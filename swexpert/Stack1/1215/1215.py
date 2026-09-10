import sys
sys.stdin = open("input.txt", "r")
T = 10
for test_case in range(1, T+1):
    length = int(input())
    text_map = [list(input()) for _ in range(8)]
    cnt = 0
    for i in range(0, 8):
        for j in range(0, 8):
            text = []
            for k in range(0, length):
                if j+k < 8:
                    text.append(text_map[i][j+k])
                else:
                    continue
            if text == text[::-1] and len(text) == length:
                cnt += 1
            text = []
            for k in range(length):
                if i + k < 8:
                    text.append(text_map[i+k][j])
                else:
                    continue
            if text == text[::-1] and len(text) == length:
                cnt += 1
    print(f"#{test_case} {cnt}")