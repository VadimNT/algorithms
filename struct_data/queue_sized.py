class MyQueueSized:
    def __init__(self):
        self.items = []
        self.cnt = 0
        self.max_size = None

    def is_empty(self):
        return True if not self.items else False

    def push(self, x):
        self.cnt += 1
        if self.cnt > self.max_size:
            self.cnt -= 1
            return print('error')
        self.items.append(x)

    def size(self):
        return self.cnt

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def pop(self):
        if self.is_empty():
            return None
        self.cnt -= 1
        return self.items.pop(0)


if __name__ == '__main__':
    n = int(input())
    stack = MyQueueSized()
    stack.max_size = int(input())
    i = 0
    while i < n:
        str_in = input().split()
        if str_in[0] == 'pop':
            print(stack.pop())
            i += 1
            continue
        if str_in[0] == 'push':
            stack.push(int(str_in[1]))
            i += 1
            continue
        if str_in[0] == 'size':
            print(stack.size())
            i += 1
            continue
        if str_in[0] == 'peek':
            print(stack.peek())
            i += 1
            continue
        i += 1
