import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    tri = int(input())
    m = [1]
    n = [1]
    print(f"#{test_case}")
    for i in range(tri//2+tri%2):
        print(' '.join(map(str, m)))
        m.append(m[i] + n[-1])
        m.extend(n)
        n.append(m[-1])





