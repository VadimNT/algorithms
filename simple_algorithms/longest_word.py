import sys


def main():
    n = int(input())
    line = map(str, sys.stdin.readline().split())
    max_len = len_words = 0
    result = ''
    for words in line:
        len_words = len(words)
        if len_words > max_len:
            max_len = len_words
            result = words
    return print(result, max_len, sep='\n')


if __name__ == '__main__':
    main()
