def main():
    str1 = input()
    str2 = input()
    m = len(str2)
    for i in range(m):
        s = str2[i]
        if s in str1:
            str1 = str1.replace(s, '', 1)
        else:
            print(s)
            break


if __name__ == '__main__':
    main()
