from random import choice

digits = ['23456789', 'abcdefghjkmnpqrstuvwxyz', 'ABCDEFGHJKMNPQRSTUVWXYZ', '!#$%&*+-=?@^_', "il1Lo0O"]
chars = ''
parameters = []

password_amount = int(input('Сколько паролей нужно сгенерировать? '))
password_length = int(input('Какая длина пароля? '))


# проверяем, введен либо 0 либо 1
def is_yn_valid(ans):
    while True:
        if ans == '1':
            return True
        elif ans == '0':
            return False
        else:
            ans = input('Введите либо цифру 1 либо 0: ')


# задаем вопрос
def question(quest):
    if is_yn_valid(input(f'{quest}: ')):
        return True
    else:
        return False


def generate_password(length, chars):
    new_pass = ''
    for _ in range(length):
        new_pass += choice(chars)
    return new_pass


parameters.append(question('Включать ли цифры 0123456789? 1/0: '))
parameters.append(question('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? 1/0: '))
parameters.append(question('Включать ли заглавные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? 1/0: '))
parameters.append(question('Включать ли символы !#$%&*+-=?@^_? 1/0: '))
parameters.append(question('Включать ли неоднозначные символы il1Lo0O? 1/0: '))

cnt = 0
for i in parameters:
    if i:
        chars += digits[cnt]
    cnt += 1

for i in range(password_amount):
    print(generate_password(password_length, chars))
