#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author = 'Koreshichi'

'''
lexical analysis module
'''

import ply.lex as lex

reserved = {                      #保留字dict
	'else'   : 'ELSE',
	'if'     : 'IF',
	'int'    : 'INT',
	'return' : 'RETURN',
	'void'   : 'VOID',
	'while'  : 'WHILE',
}

tokens = [
	'COMMENT',          #'/*...*/的注释'
	'SEMICOLON',        #';'
	'NEQUAL',           #'!='
	'EQUAL',            #'=='
	'MOREE',
	'LESSE',            #'<='
	'MORE',             #'>='
	'LESS',
	'IS',               #'='
	'COMMA',            #','
	'LPAREN', 			#'('
	'RPAREN',           #')'
	'LBRAK',            #'['
	'RBRAK',            #']'
	'PLUS',
	'MINUS',
	'TIMES',
	'DIVIDE',
	'ID',
	'NUMBER',	
] + list(reserved.values())          #链接保留字

#匹配正则
t_SEMICOLON = r';'
t_NEQUAL    = r'!='
t_EQUAL     = r'=='
t_MOREE     = r'>='
t_LESSE     = r'<='
t_MORE      = r'>'
t_LESS      = r'<'
t_IS        = r'='
t_COMMA     = r','
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRAK     = r'\['
t_RBRAK     = r'\]'
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'

def t_COMMENT(t):                  #丢弃注释
	r'/\*(.|\n)*\*/'
	pass
	
def t_ID(t):                       #保留字识别
	r'[a-zA-Z]+'
	t.type = reserved.get(t.value,'ID')
	return t
	
def t_NUMBER(t):                   #数字转换
	r'\d+'
	t.value = int(t.value)
	return t
	
def t_newline(t):                  #行号计数
	r'\n+'
	t.lexer.lineno += len(t.value)
	
t_ignore = ' \t'                   #忽略空格

def t_error(t):
	print ("ERROR:\tIllegal character in line %d : '%s'" % (t.lineno,t.value[0]))
	t.lexer.skip(1)
	
lexer = lex.lex()

#------------------------------------test---------------------------------
print("输入测试字符串,双击回车结束：")
stopword = ''
str = ''
for line in iter(input,stopword):
	str += line + '\n'

lexer.input(str)

for tok in lexer:
	print (tok)

	
