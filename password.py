"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""

if __name__ == '__main__':
    alpha_flag = False
    num_flag = False
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    nums = '0123456789'
    password = input('Введите пароль: ')
    for char in password:
        if char.lower() in alpha:
            alpha_flag = True
        if char in nums:
            num_flag = True
    if alpha_flag and num_flag and len(password) >= 8:
        print('Пароль сложный')
    else:
        print('Пароль простой')
