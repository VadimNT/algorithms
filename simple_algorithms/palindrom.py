import re


def main():
    line = (input()).lower()
    line = line.replace(' ', '')
    line = re.sub(r'[.,"\'-?:!;]', '', line)
    print(True if line == line[::-1] else False)


if __name__ == '__main__':
    main()
