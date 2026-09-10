import sys
sys.stdin = open("input1.txt", "r")
#진 기 이 씨 발 개 미 친 새 끼
T = int(input())
for test_case in range(1, T+1):
    # N = people
    # M = sec
    # K = bread
    N, M, K = list(map(int, input().split()))
    li = list(map(int, input().split()))
    li.sort()
    bread, sec, sw = 0, 0, 1
    print(N,M,K,li)
    for i in li:
        if not (i//M):
            print(f"#{test_case} Impossible")
            sw = 0
            break
        else:
            if bread < 0:
                print(f"#{test_case} Impossible")
                sw = 0
                break
            if (i - sec)//M:
                bread += ((i - sec)//M) * K
                sec = M * (i//M)
                print(bread, sec, i)
            bread -= 1
    if bread >= 0 and sw:
        print(f"#{test_case} Possible")