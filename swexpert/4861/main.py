import sys
sys.stdin = open("sample_input.txt", "r")
#////////////////////////////////////////////////////////////////////////////////////
    # N * N의 2차원 리스트에서 M의 길이의 회문을 뽑아내야함
    # 1. M의 길이만큼 슬라이싱 해서 문자열을 만들고 검사 후
    # 2-1. 맞으면 출력
    # 2-2. 아니면 다음 인덱스로 넘어가 다시 1번 실행
#////////////////////////////////////////////////////////////////////////////////////
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    texts = [list(input()) for _ in range(N)]
    L = []
    for i in range(N):
        for k in range(0, N-M+1):
            li, il = [], []
            for j in range(M):
                if j+k < N or i+k < N:
                    li.append(texts[j+k][i])
                    il.append(texts[i][j+k])
            if li:
                L.append(li)
            if il:
                L.append(il)
    for i in L:
        if i == i[::-1]:
            text = ''.join(i)
    print(f"#{test_case} {text}")