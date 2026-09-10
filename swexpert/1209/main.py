import sys

sys.stdin = open("input.txt", "r")

def max_num(num_list):
    max_number = 0
    for i in num_list:
        if max_number < sum(i):
            max_number = sum(i)
    return max_number

def make_list_1dim(num_list):
    t_d = []
    for i in range(len(num_list)):
        dim = []
        for j in range (100):
            dim.append(num_list[j][i])
        t_d.append(dim)
    return t_d

def dia(num_list):
    dia_d = []
    dia_u = []
    for i in range(len(num_list)):
        for j in range(100):
            if i == j:
                dia_d.append(num_list[j][i])
            if (100 - i) == j:
                dia_u.append(num_list[j][i])
    return dia_d, dia_u

for _ in range(10):
    y = []
    test_case = int(input())
    li = [list(map(int, input().split())) for _ in range(100)]
    x_result = max_num(li)
    dim = make_list_1dim(li)
    y_result = max_num(dim)
    dia_d, dia_u = dia(li)

    print(f"#{test_case} {max(x_result, y_result, sum(dia_d), sum(dia_u))}")
    #print(f'#{test_case} {max_number}')
