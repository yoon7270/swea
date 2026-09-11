import sys
sys.stdin = open("input4_sample.txt", "r")
import itertools
T = int(input())
for test_case in range(1, T+1):
    #학생 수 N, 문항 수 M, 콤보 기준 K
    N, M, K = list(map(int, input().split()))
    #M개 문항의 정답
    awn = list(map(int, input().split()))
    #N줄에 걸쳐 각 학생의 답안
    li = [list(map(int, input().split())) for _ in range(N)]
    #학생별 점수 리스트
    ch= []
    for i in range(N):
        sch, cb = [], 1
        for j in range(M):
            if li[i][j] == awn[j] and cb == K:
                sch.append(50)
                cb = 1
            elif li[i][j] == awn[j] and cb != K:
                sch.append(10)
                cb += 1
            else:
                cb = 1
        ch.append(sch)
    print(f"#{test_case} {sum(max(ch))}")