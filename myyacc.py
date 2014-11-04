#!/usr/bin/env python3

import ply.yacc as yacc
import lexer
tokens = lexer.tokens

def p_assign(p):
    '''assign : NAME EQUALS expr'''

def p_expr(p):
    '''expr : expr PLUS term
            | expr MINUS term
            | term'''

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | factor'''

def p_factor(p):
    '''factor : NUMBER'''

yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break

    yacc.parse(s)
