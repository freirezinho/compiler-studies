import os

"""
EXERCÍCIO 02

Escreva um programa em Python com as seguintes funcionalidades:
• Ler um arquivo de um programa escrito na linguagem C (ex03.c).
• Modificar as palavras reservadas do programa lido para MAIÚSCULO.
• Gravar um arquivo do mesmo programa na linguagem C com as modificações
solicitadas (ex03.out)
• Abaixo está a tabela com as palavras reservadas da linguagem C.
"""
file_path = './Saulo Santos Freire - ex03.c'

reserved_words = ['auto', 'break', 'case', 'char',
'const', 'continue', 'default', 'do',
'double', 'else', 'enum', 'extern',
'float', 'for', 'goto' 'if',
'int', 'long', 'register', 'return',
'short', 'signed', 'sizeof', 'static',
'struct', 'switch', 'typedef', 'union',
'unsigned', 'void', 'volatile', 'while']

with open(file_path) as file:
    lines = file.readlines()