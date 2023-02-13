class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max_item = []

    def push(self, x):
        if len(self.items) == 0:
            self.max_item.append(x)
        elif int(x) > self.max_item[-1]:
            self.max_item.append(x)
        else:
            self.max_item.append(self.max_item[-1])
        self.items.append(x)

    def pop(self):
        if not self.items:
            return 'error'
        self.items.pop()
        self.max_item.pop()

    def get_max(self):
        if not self.items:
            return None
        return self.max_item[-1]


if __name__ == '__main__':
    n = int(input())
    i = 0
    stack = StackMaxEffective()
    while i < n:
        str_in = input().split()
        if str_in[0] == 'get_max':
            print(stack.get_max())
        if str_in[0] == 'push':
            stack.push(int(str_in[1]))
        if str_in[0] == 'pop':
            if stack.pop() == 'error':
                print('error')
        i += 1
