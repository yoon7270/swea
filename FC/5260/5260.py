# # 5260. [S/W 문제해결 최적화] 3일차 - 부분 집합의 합
# import sys
# sys.stdin = open("input.txt", "r")

# def make_m(depth, I):
#     global M
#     if I == K:
#         M += 1
#         return M
#     if depth == N + 1:
#         return
#     make_m(depth+1, I)
#     make_m(depth+1, I-depth)

# T = int(input())
# for test_case in range(1, T + 1):
#     N, K = map(int, input().split())
#     M = 0
#     make_m(1, sum(range(1, N+1)))
#     print(f"#{test_case} {M}") 

print(2**100)