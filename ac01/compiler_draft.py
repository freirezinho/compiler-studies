import os
file_path = 'Saulo Santos Freire - ex03.c'
word_delimiters = [" ", "(", ")"]
line_delimiters = [';', '\n']
string_limiters = '"'
reserved_words = ['auto', 'break', 'case', 'char',
'const', 'continue', 'default', 'do',
'double', 'else', 'enum', 'extern',
'float', 'for', 'goto' 'if',
'int', 'long', 'register', 'return',
'short', 'signed', 'sizeof', 'static',
'struct', 'switch', 'typedef', 'union',
'unsigned', 'void', 'volatile', 'while']

file = open(file_path)

for line in file.readlines():
    print(line)