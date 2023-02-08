def main():
    n = int(input())
    x = int(input().replace(' ', ''))
    k = int(input())
    print(' '.join(list(map(str, list(str(x + k))))))


if __name__ == '__main__':
    main()
