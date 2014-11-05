#!/usr/bin/env python3

import ply.yacc as yacc
import lexer
tokens = lexer.tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS')
)

vars = {}
def p_statement_assign(p):
    'statement : NAME EQUALS expr'
    vars[p[1]] = p[3]

def p_statement_expr(p):
    'statement : expr'
    print(p[1])

def p_expression_plus(p):
    'expr : expr expr PLUS'
    p[0] = p[1] + p[2]

def p_expression_minus(p):
    'expr : expr expr MINUS'
    p[0] = p[1] - p[2]

def p_expression_times(p):
    'expr : expr expr TIMES'
    p[0] = p[1] * p[2]

def p_expression_divide(p):
    'expr : expr expr DIVIDE'
    p[0] = p[1] / p[2]

def p_expression_uminus(p):
    'expr : MINUS expr %prec UMINUS'
    p[0] = -p[2]

def p_number(p):
    'expr : NUMBER'
    p[0] = p[1]

def p_expression_name(p):
    'expr : NAME'
    try:
        p[0] = vars[p[1]]
    except:
        print("Nome indefinido '%s'" % p[1])

def p_error(p):
    print("Erro de sintaxe na entrada.")

yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)
