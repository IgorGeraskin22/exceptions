# -*- coding: utf-8 -*-
import random

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
# https://goo.gl/JnsDqu


ENLIGHTENMENT_CARMA_LEVEL = 777
carma_level = 0


class IamGodError(Exception):
    pass


class DrunkError(IamGodError):
    pass


class CarCrashError(IamGodError):
    pass


class GluttonyError(IamGodError):
    pass


class DepressionError(IamGodError):
    pass


class SuicideError(IamGodError):
    pass


exclusion_list = [IamGodError('Я стал Богом'), DrunkError('Я напился'), CarCrashError('Я еду на машине'),
                  GluttonyError('Я переел'), DepressionError('У меня дипрессия'), SuicideError('Я ухожу')]


def one_day():
    try:
        if dice == 13:
            raise IamGodError()
    except IamGodError:
        print(random.choice(exclusion_list))


while True:

    dice = random.randint(1, 13)
    one_day()
    if dice == 1 or dice <= 7:

        if carma_level < ENLIGHTENMENT_CARMA_LEVEL:
            carma_level += dice
        else:
            break

print('Карма равна = ', carma_level)
one_day()

# Зачёт!
