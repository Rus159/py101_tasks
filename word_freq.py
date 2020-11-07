import sys
import collections
from nltk.corpus import stopwords
import os
"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if os.path.isfile(file_path := sys.argv[1]):
            text = ''
            symbols = '-!@#№$<>%^"\'*.()_+="№;:,?'
            stop_words = set(stopwords.words("english"))
            stop_words.add('-')
            with open(sys.argv[1], 'rt') as file:
                file_lines = file.readlines()
                file_lines = [line.strip() for line in file_lines]

            for line in file_lines:
                text += line + ' '
            for char in symbols:
                text = text.replace(char, ' ')
            words = text.split()
            without_stop_words = [word for word in words if word not in stop_words]
            top_words = collections.Counter(without_stop_words).most_common(100)
            print('Top-100 words:')
            for i in range(len(top_words)):
                print('{}: {}'.format(top_words[i][0], top_words[i][1]))
        else:
            print('File is missing')
    else:
        print('Full path to the file is missing')
