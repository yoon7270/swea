import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    K, N, M = list(map(int,input().split()))
    C_station = list(map(int, input().split()))
    sta_idx = 0
#/////////////////////////////////////////////////////////////////////////
#    1. 맵을 리스트로 시각화한 후 정거장을 표시한다.
#    2. 이동 거리 또한 리스트로 만든다.
#    3. 맵과 곂쳐 정거장을 확인한다.
#    4. 정거장이 있다면 출발 위치를 그 곳으로 바꾸고 다시 3번으로 간다.
#/////////////////////////////////////////////////////////////////////////
    run_map = [0] * (N + 1)
    run_m = [0] * (K + 1)
    for i in C_station:
        run_map[i] = "S"
    while sta_idx > 10:

    print(run_map, run_m)

    #print(f"#{test_case} {cnt}")