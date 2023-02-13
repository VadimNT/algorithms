def gen_parentheses(n1, n2, prefix):
    if n1 == 0 and n2 == 0:
        print(prefix)
    if n1 > 0:
        gen_parentheses(n1 - 1, n2, prefix + '(')
    if n2 > n1:
        gen_parentheses(n1, n2 - 1, prefix + ')')


if __name__ == '__main__':
    n = int(input())
    comb1 = comb2 = n
    gen_parentheses(comb1, comb2, prefix='')
