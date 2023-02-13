# 79328580
class Deque:
    def __init__(self, max_size):
        self.__items = [None] * max_size
        self.__max_size = max_size
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def __is_empty(self):
        return self.__size == 0

    def __is_full(self):
        return True if self.__size != self.__max_size else False

    def __get_idx(self, idx, sign: bool):
        idx = (idx + (2 * sign - 1) * 1) % self.__max_size
        return idx

    def push_back(self, x):
        if self.__size != self.__max_size:
            self.__items[self.__tail] = x
            self.__tail = self.__get_idx(self.__tail, True)
            self.__size += 1
        else:
            raise BufferError

    def push_front(self, x):
        if self.__size != self.__max_size:
            self.__items[self.__head - 1] = x
            self.__head = self.__get_idx(self.__head, False)
            self.__size += 1
        else:
            raise BufferError

    def pop_front(self):
        if self.__is_empty():
            raise IndexError
        x = self.__items[self.__head]
        self.__items[self.__head] = None
        self.__head = self.__get_idx(self.__head, True)
        self.__size -= 1
        return x

    def pop_back(self):
        if self.__is_empty():
            raise IndexError
        x = self.__items[self.__tail - 1]
        self.__items[self.__tail - 1] = None
        self.__tail = self.__get_idx(self.__tail, False)
        self.__size -= 1
        return x


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    d = Deque(m)
    for item in range(n):
        method, *value = input().split()
        if value:
            try:
                result = getattr(d, method)(int(*value))
                if result is not None:
                    print(result)
            except BufferError:
                print('error')
        else:
            try:
                result = getattr(d, method)()
                print(result)
            except IndexError:
                print('error')
