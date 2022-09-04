import os
import re

"""
EXERCÍCIO 1
Ler um arquivo de um programa escrito na linguagem C (ex03.c).
• Contar a quantidade de letras a..zA..Z, dígitos 0..9 e espaços em branco e
caracteres especiais..
• Imprimir uma relação das letras, dígitos, espaços em branco, caracteres especiais
e a quantidade de cada um desses símbolos encontrado.
• A relação deve estar classificada pelo valor das quantidades encontradas.
• Ao final, imprimir o número de linhas no arquivo fonte e o tamanho do arquivo em
bytes.
"""

lettersRegExp = re.compile('[a-zA-Z]')
digitsRegExp = re.compile('\d')
whitespaceRegExp = re.compile('\s')
specialCharsRegExp = re.compile('[^a-zA-Z\s\d]')
file_path = './ex03.c'
letters = []
letters_count = 0
digits = []
digits_count = 0
whitespaces = []
whitespaces_count = 0
special_chars = []
special_chars_count = 0

with open(file_path) as file:
    # ex
    lines = file.readlines()
    for line in lines:
        found_letters = lettersRegExp.findall(line)
        found_digits = digitsRegExp.findall(line)
        found_whitespaces = whitespaceRegExp.findall(line)
        found_specialchars = specialCharsRegExp.findall(line)
        digits_count += len(found_digits)
        letters_count += len(found_letters)
        whitespaces_count += len(found_whitespaces)
        special_chars_count += len(found_specialchars)
    count_dict = {}
    count_dict[letters_count] = 'letras'
    count_dict[digits_count] = 'dígitos'
    count_dict[whitespaces_count] = 'espaços em branco'
    count_dict[special_chars_count] = 'caracteres especiais'
    count_list = [letters_count, digits_count,
                  whitespaces_count, special_chars_count]
    count_list.sort(reverse=True)
    print("Este arquivo possui...\n")
    for count in count_list:
        print(f'{count} {count_dict[count]}')
    print("\nMetadata: \n")
    print(f'{len(lines)} linhas')
    print(f'{os.stat(file_path).st_size} bytes')
