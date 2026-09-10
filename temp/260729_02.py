# # 아래 함수를 수정하시오.
# def check_number():
#     while True:
#         print("숫자를 입력하세요")
#         try:
#             number = int(input())
#             if number > 0:
#                 print("양수입니다.")
#             elif number == 0:
#                 print("0입니다.")
#             else:
#                 print("음수입니다.")
#         except ValueError:
#             print("잘못된 입력입니다.")
#
# check_number()

# class UserInfo:
#     def __init__(self):
#         self.user_data = {}
#         self.name = None
#         self.age = None
#
#     def get_user_info(self):
#         """
#         사용자로부터 이름과 나이를 입력받습니다.
#         - 이름이 없거나 공백이면 None을 반환합니다.
#         - 나이가 숫자가 아니거나 입력되지 않으면 ValueError를 처리하고 False를 반환합니다.
#         - 올바르게 입력되면 사용자 정보를 저장하고 True를 반환합니다.
#         """
#         # TODO: 아래 코드를 문제 요구사항에 맞게 완성하세요.
#         try:
#             name = input('이름을 입력하세요 :')
#             if not(name.strip()):
#                 return None
#             age = int(input('나이를 입력하세요 :'))
#         except ValueError:
#             print('나이는 숫자로 입력해야 합니다.')
#             return False
#         else:
#             self.name = name
#             self.age = age
#             return True
#
#     def display_user_info(self):
#         """
#         저장된 사용자 정보를 출력합니다.
#         - 정보가 없으면 "사용자 정보가 입력되지 않았습니다."를 출력합니다.
#         """
#         # TODO: 아래 코드를 문제 요구사항에 맞게 완성하세요.
#         if self.name and self.age:
#             print('사용자 정보 :', f'이름 : {self.name}', f'나이 : {self.age}', sep='\n')
#         else:
#             print('사용자 정보가 입력되지 않았습니다.')
#
#
# # 아래 코드는 수정하지 마세요.
# user = UserInfo()
# result = user.get_user_info()
#
# if result is True:
#     user.display_user_info()
# elif result is None:
#     # 이름이 입력되지 않은 경우, display_user_info()가 적절한 메시지를 출력해야 합니다.
#     user.display_user_info()
# # 나이가 잘못 입력된 경우 (result is False), get_user_info()에서 이미 메시지를 출력했으므로
# # 추가적인 동작이 필요 없습니다.

# data = {'name': '홍길동'}
# try:
#     if not data['age']:
#         print(data['age'])
#     else:
#         print('data에는 age라는 키가 없습니다.')
#         data['age'] = 30
#         print(data)
# except KeyError:
#     print('data에는 age라는 키가 없습니다.')
#     data.setdefault('age', 30)
#     print(data)
# # 아래에 코드를 작성하시오.
#
#
#
# arr = ['반갑', '하세요', '안녕']
# try:
#     for i in range(4):
#         print(arr.pop())
#     print(arr)
# except IndexError:
#     print(arr)
#     print('더 이상 pop 할 수 없습니다.')
#
# # 아래에 코드를 작성하시오.
#
#
# try:
#     word = '3.15'
#     print(int(word))
# except ValueError:
#     print('정수로 변환 가능한 값을 입력해 주세요.')
#
# # 아래에 코드를 작성하시오.

# class BaseModel:
#     PK = 1
#     TYPE = 'Basic Model'
#
#     def __init__(self, data_type, title, content, created_at, updated_at):
#         self.PK = BaseModel.PK
#         self.data_type = data_type
#         self.title = title
#         self.content = content
#         self.created_at = created_at
#         self.updated_at = updated_at
#         BaseModel.PK += 1
#
#     def save(self):
#         print('데이터를 저장합니다.')
#
#
# class Novel(BaseModel):
#
#     def __init__(self, data_type, title, content, created_at, updated_at, author):
#         super().__init__(data_type, title, content, created_at, updated_at)
#         self.author = author
#
#
# class Other(BaseModel):
#     TYPE = 'Other Model'
#
#     def save(self):
#         print('데이터를 다른 장소에 저장합니다.')
#
#
# class ExtendModel(Novel, Other):
#
#     def __init__(self):
#         self.Extended_Type = 'Extended Type'
#
#     def display_info(self):
#         print("ExtendedModel 인스턴스의 정보 출력 및 메서드 호출")
#         print(f'PK: {self.PK}, TYPE: {self.TYPE}, Extended Type: {self.Extended_Type}')
#
#     def save(self):
#         print("데이터를 확장해서 저장합니다.")
#
#
# extended_instance = ExtendModel()
# extended_instance.display_info()
# extended_instance.save()

# 아래 클래스를 수정하시오.
# class Animal:
#     num_of_animal = 0
#
#     def __init__(self):
#         Animal.increase_animal()
#         pass
#
#     @classmethod
#     def increase_animal(cls):
#         cls.num_of_animal += 1
#

class Dog():

    def __init__(self):
        self.sound = "멍멍"


class Cat():

    def __init__(self):
        self.sound = "야옹"


class Pet(Dog, Cat):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return f'애완동물은 {self.sound}소리를 냅니다.'


pet = Pet()
print(pet)


