from sys import stdin

import itertools
import operator
import ply.yacc as yacc
import ply.lex as lex

l = stdin.read().split("\n")


def solve(precedence_rules):

    precedence = precedence_rules

    tokens = (
        'NAME', 'NUMBER',
        'PLUS', 'TIMES', 'EQUALS',
        'LPAREN', 'RPAREN',
    )

    # Tokens
    t_PLUS    = r'\+'
    t_TIMES   = r'\*'
    t_EQUALS  = r'='
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

    def t_NUMBER(t):
        r'\d+'
        t.value = int(t.value)
        return t

    t_ignore = " \t"

    def t_error(t):
        print(f"Illegal character {t.value[0]!r}")
        t.lexer.skip(1)

    lex.lex()

    names = { }

    def p_statement_assign(p):
        'statement : NAME EQUALS expression'
        names[p[1]] = p[3]

    def p_expression_binop(p):
        '''expression : expression PLUS expression
                    | expression TIMES expression'''
        if p[2] == '+': 
            p[0] = p[1] + p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]

    def p_expression_group(p):
        'expression : LPAREN expression RPAREN'
        p[0] = p[2]

    def p_expression_number(p):
        'expression : NUMBER'
        p[0] = p[1]

    def p_expression_name(p):
        'expression : NAME'
        try:
            p[0] = names[p[1]]
        except LookupError:
            print(f"Undefined name {p[1]!r}")
            p[0] = 0

    def p_error(p):
        print(f"Syntax error at {p.value!r}")

    # Build the parser
    parser = yacc.yacc(debug=False, write_tables=False)

    for i, line in enumerate(l):
        parser.parse("R" + str(i) + " = (" + line + ")")

    return sum(names.values())


# Part One
precedence_p1 = (
    ('left','PLUS', 'TIMES'),
    ('left','EQUALS'),
)
print(solve(precedence_p1))

# Part Two
precedence_p2 = (
    ('left','EQUALS'),
    ('left', 'TIMES'),
    ('left','PLUS'),
)
print(solve(precedence_p2))
