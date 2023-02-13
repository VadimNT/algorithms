def isSubsequence(s: str, t: str) -> bool:
    n, m = len(s), len(t)
    i = 0
    for j in range(m):
        if s[i] == t[j]:
            i += 1
            if i == n:
                return True
    return False


if __name__ == '__main__':
    first_str = input()
    second_str = input()
    print(isSubsequence(first_str, second_str))
