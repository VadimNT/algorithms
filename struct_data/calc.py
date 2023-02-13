# 79323479
class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[-1]

    def size(self):
        return len(self.__items)


def calculate(data):
    data = data.split()
    operation = {
        '+': lambda y, x: int(x) + int(y),
        '-': lambda y, x: int(x) - int(y),
        '*': lambda y, x: int(x) * int(y),
        '/': lambda y, x: int(int(x) // int(y)),
    }
    calc = Stack()
    for item in data:
        if item in operation:
            calc.push(operation[item](calc.pop(), calc.pop()))
        else:
            calc.push(item)
    return calc.peek()


if __name__ == '__main__':
    in_data = input()
    print(calculate(in_data))
