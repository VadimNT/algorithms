def get_out_word(s, t):
    for word in s:
        t.remove(word)
    return t[0]


if __name__ == '__main__':
    in_s = list(input())
    in_t = list(input())
    print(get_out_word(in_s, in_t))
