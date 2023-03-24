import re


def check_palindrome(data: str) -> bool:
    data = data.lower().replace(' ', '')
    data = re.sub(r'[.,;:?!"\']', '', data)
    return True if data == data[::-1] else False


if __name__ == '__main__':
    in_str = input()
    print(check_palindrome(in_str))
