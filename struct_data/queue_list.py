class StackMax:
    def __init__(self):
        self.items = []
        self.cnt = 0

    def put(self, x):
        self.items.append(x)
        self.cnt += 1

    def size(self):
        return self.cnt

    def get(self):
        if not self.items:
            return 'error'
        self.cnt -= 1
        return self.items.pop(0)


if __name__ == '__main__':
    n = int(input())
    i = 0
    stack = StackMax()
    while i < n:
        str_in = input().split()
        if str_in[0] == 'get':
            print(stack.get())
            i += 1
            continue
        if str_in[0] == 'put':
            stack.put(int(str_in[1]))
            i += 1
            continue
        if str_in[0] == 'size':
            print(stack.size())
            i += 1
            continue
        i += 1
