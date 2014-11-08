#!/usr/bin/env python3

def infix2rp(exp):
    sym = []
    res = []
    prio = {
            '(' : 0,
            '+' : 1,
            '-' : 1,
            '*' : 2,
            '/' : 2,
            '^' : 3,
            }
    exp = '(' + exp + ')'

    for char in exp:
        if char in '+-*/^':
            while sym and prio[char] <= prio[sym[-1]]:
                res.append(' ')
                res.append(sym.pop())
            sym.append(char)
            res.append(' ')
        elif char == '(':
            sym.append(char)
        elif char == ')':
            while sym[-1] != '(':
                res.append(' ')
                res.append(sym.pop())
            sym.pop()
        elif char.isalnum() or char == '.':
            res.append(char)

    return ''.join(res)


if __name__ == '__main__':
    exp = input()
    while exp:
        print(infix2rp(exp))
        exp = input()
