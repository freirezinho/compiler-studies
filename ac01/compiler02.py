import os
import re
"""
EXERCÍCIO 02

Escreva um programa em Python com as seguintes funcionalidades:
• Ler um arquivo de um programa escrito na linguagem C (ex03.c).
• Modificar as palavras reservadas do programa lido para MAIÚSCULO.
• Gravar um arquivo do mesmo programa na linguagem C com as modificações
solicitadas (ex03.out)
• Abaixo está a tabela com as palavras reservadas da linguagem C.
"""
file_path = './ex03.c'

reserved_words = ['auto', 'break', 'case', 'char',
                  'const', 'continue', 'default', 'do',
                  'double', 'else', 'enum', 'extern',
                  'float', 'for', 'goto' 'if',
                  'int', 'long', 'register', 'return',
                  'short', 'signed', 'sizeof', 'static',
                  'struct', 'switch', 'typedef', 'union',
                  'unsigned', 'void', 'volatile', 'while']

lettersRegExp = re.compile('[a-z]+[^\n\(\)\"\\\;\s]')


def substrings(word):
    yield word


word_set = set().union(*map(substrings, reserved_words))
print(word_set)
new_lines = []

og_file = open(file_path, 'r')
new_file = open("ex03.out", 'w')
lines = og_file.readlines()
for line in lines:
    # print(line)
    words = line
    for word in words.split():
        if '"' in word:
            break
        print(f'word: {word}')
        found_words = lettersRegExp.findall(word)
        print(f'found words: {found_words}')
        for found_word in found_words:

            if found_word in word_set:
                print(f'replacing {found_word}')
                words = words.replace(found_word, found_word.upper())
    # words = " ".join(words)
    new_file.write(words)

og_file.close()
new_file.close()
