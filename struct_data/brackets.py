def is_correct_bracket_seq(text) -> bool:
    if not text:
        return True
    while '()' in text or '[]' in text or '{}' in text:
        text = text.replace('()', '')
        text = text.replace('[]', '')
        text = text.replace('{}', '')
    return not text


if __name__ == '__main__':
    data = input()
    print(is_correct_bracket_seq(data))
