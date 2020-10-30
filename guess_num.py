"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""
import random


if __name__ == '__main__':
    num = random.randint(0, 1000000)

    print('С подключением, %username%! Попробуй угадать число от 0 до 1 000 000. Для выхода из игры введи exit или пустую строку.')
    answer = '0'
    while int(answer) != num and answer != 'exit' and answer != '':
        answer = input('Введи предполагаемое число: ')
        if answer == '':
            print('Не введено число')
        if answer == 'exit':
            pass
        elif 1 > int(answer) > 1000000:
            print('Число не соответствует диапазону')
        elif int(answer) == num:
            print('Число угадано!')
        elif num > int(answer):
            print('Число меньше загаданного')
        else:
            print('Число больше загаданного')
