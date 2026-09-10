import sys
sys.stdin = open("GNS_test_input.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for _ in range(1, T+1):
    test_case, Num = input().split()
    numb_dict = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0}
    text_num = input().split()
    for i in text_num:
        if i in numb_dict:
            numb_dict[i] += 1
    print(test_case, end=" ")
    for k, v in numb_dict.items():
        print((k+" ") * v, end="")
