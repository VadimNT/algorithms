class StackMax:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.items:
            return "error"
        self.items.pop()

    def get_max(self):
        if not self.items:
            return None
        return max(self.items)


if __name__ == '__main__':
    n = int(input())
    i = 0
    stack = StackMax()
    while i < n:
        str_in = input().split()
        if str_in[0] == 'get_max':
            print(stack.get_max())
        if str_in[0] == 'push':
            stack.push(int(str_in[1]))
        if str_in[0] == 'pop':
            result = stack.pop()
            if result == 'error':
                print(result)
        i += 1
