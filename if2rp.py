#!/usr/bin/env python3

class IllegalExprError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return 'Illegal Expression: {}'.format(self.value)

def infix2rp(exp):
    sym = []
    res = []
    lastchar = ""
    prio = {
            '(' : 0,
            '+' : 1,
            '-' : 1,
            '*' : 2,
            '/' : 2,
            '^' : 3,
            }

    if not exp:
        raise EOFError

    exp = '(' + exp + ')'

    for char in exp:
        if char in '+-*/^':
            if lastchar in '+-*/^(':
                raise IllegalExprError('Illegal symbol usage.')
            lastchar = char
            while sym and prio[char] <= prio[sym[-1]]:
                res.append(' ')
                res.append(sym.pop())
            sym.append(char)
            res.append(' ')
        elif char == '(':
            sym.append(char)
        elif char == ')':
            if lastchar in '+-*/^':
                raise IllegalExprError('Illegal symbol usage.')
            try:
                while sym[-1] != '(':
                    res.append(' ')
                    res.append(sym.pop())
                sym.pop()
            except IndexError:
                raise IllegalExprError("Missing '('.")
        elif char.isalnum() or char == '.':
            res.append(char)
            lastchar = char
        elif char != ' ':
            raise IllegalExprError('Invalid character.')

    if sym:
        raise IllegalExprError("Missing ')'.")

    return ''.join(res)


if __name__ == '__main__':
    exp = input()
    while exp:
        print(infix2rp(exp))
        exp = input()
