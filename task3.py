# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPTS = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

print('Давайте сыграем в игру, я загадываю число от 1 до 1000, а вы попробуйте его угадать. У вас есть 10 попоыток')

for i in range(ATTEMPTS):
    user_num = int(input('Попробуйте угадать число, которое я загадал: '))
    if user_num == num:
        print('Отлично! Вы угадали мое число')
        break
    elif user_num < num:
        print('Вы почти угадали, но мое число больше вашего')
    elif user_num > num:
        print('Вы почти угадали, но мое число меньше вашего')
else:
    print(f'К сожалению вы не угадали. Я загадал число: {num}. Попробуйте еще раз...')
