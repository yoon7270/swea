class Stack:
    def __init__(self, capacity = 10):
        # 생성자 메서드, 인스턴스가 만들어질 때 초기화
        self.capacity = capacity
        self.items = [None] * capacity
        self.top = -1

    #가득 찼는지 확인하는 메서드
    #top 포인터 +1이 스택의 용량과 같다면 => 가득찬 것
    def is_full(self):
        return self.top + 1 == self.capacity

    def is_empty(self):
        return self.top == -1

    def pop(self):
        if self.is_empty():
            raise  IndexError("Stack is empty")
        data = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return data


    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        return self.items[self.top]


    stack = Stack(3)

    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
