# # 아래 함수를 수정하시오.
# def count_character(message: str, character: str):
#     count = 0
#     for temp_character in message:
#         count = count+1 if temp_character == character else count
#     return count
#
#
# result = count_character("Hello, World!", "o")
# print(result)  # 2

# # 아래 함수를 수정하시오.
# def find_min_max(number_list: list) -> tuple:
#     return min(number_list), max(number_list)
#
#
# result = find_min_max([3, 1, 7, 2, 5])
# print(result)  # (1, 7)

# N = 9
# data_1 = '123456789'
# arr_1 = []
# # 아래에 코드를 작성하시오.
# for index_1 in range(N):
#     arr_1.append(data_1[index_1])
# else:
#     print(arr_1)
#
# M = 15
# data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
# # 아래에 코드를 작성하시오.
# arr_2 = map(int, data_2.split())
# for number in arr_2:
#     if number % 2 == 1:
#         print(number)

# data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
# '''
# 예시코드
# arr = [1, 2, 3, 4, 5]
# for num in arr:
#     print(num, end='')
# 출력결과 : 12345
# '''
# # 아래에 코드를 작성하시오.
# message = []
# for character in data_1:
#     if character.isupper() or character == ' ':
#         message.append(character)
# else:
#     print(''.join(message))
#
# data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
# arr = []
# arr.append(data_2.find('내'))
# arr.append(data_2.find('힘'))
# arr.append(data_2.find('들'))
# arr.append(data_2.find('다'))
# print(arr)
# arr.sort()
# print(arr)
#
# message.clear()
# for index in arr:
#     message.append(data_2[index])
# else:
#     print(''.join(message))

# def restructure_word(word: str, arr: list):
#     for character in word:
#         if character.isdigit():
#             list(arr.pop() for _ in range(int(character)))
#         else:
#             arr.remove(character)
#     else:
#         return arr
#
# original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
# word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
# arr = []
#
# arr.extend(original_word)
# print(arr)
#
# result = restructure_word(word, arr)
# print(result)
# print(''.join(result))

# # 아래 함수를 수정하시오.
# def reverse_string(word: str):
#     arr = []
#     arr.extend(word)
#     arr.reverse()
#     return ''.join(arr)
#
# result = reverse_string("Hello, World!")
# print(result)  # !dlroW ,olleH

# # 아래 함수를 수정하시오.
# def remove_duplicates(lst):
#     new_lst = list(set(lst))
#     return new_lst
#
# result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# print(result)

# # 아래 함수를 수정하시오.
# def sort_tuple(origin_tuple: tuple):
#     new_list = list(origin_tuple)
#     new_list.sort()
#     new_tuple = tuple(new_list)
#     return new_tuple
#
#
# result = sort_tuple((5, 2, 8, 1, 3))
# print(result)

# 아래 함수를 수정하시오.
def even_elements(input_list):
    new_list = []
    output_list = []
    index = 0
    while index < len(input_list):
        if input_list[index] % 2 == 0:
            new_list.append(input_list.pop(index))
            continue

        index += 1
    output_list.extend(new_list)
    return output_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)

