import sys
sys.stdin = open("input.txt", "r")
b = {'*' : 2, '+' : 1}
T = 10
for test_case in range(1, T+1):
    leng = int(input())
    calc = list(input().split())
    num = []
    bi = []
    for i in calc:
        if bi and i in b.keys():
            
    print(calc)