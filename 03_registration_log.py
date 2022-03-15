# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotEmailError(Exception):
    pass


class NotNumber(NotEmailError):
    pass


class WrongName(NotEmailError):
    pass


file_registry = 'registrations.txt'


with open(file_registry, 'r', encoding='utf8') as file, open('registrations_good.log.txt', 'a', encoding='utf8') \
        as file_good_log, open('registrations_bag.log.txt', 'a', encoding='utf8') \
        as file_bag_log:
    for line in file:
        try:
            edit_line = line.replace("\n", "")  # удаляю перевод каретки \n
            name, email, age = edit_line.split(' ')  # создаю поля name, email, age

            if not name.isalpha():  # проверяю на вхождение только букв
                raise WrongName('неверное значение в поле "name"')

            if "." and "@" not in email:
                raise NotEmailError('поле "е-мейл" не содержит @ или .')

            if not age.isdigit() or 10 > int(age) or int(age) > 99:
                raise NotNumber('поле "age" не является числом или введен не корректный возраст')

            else:
                file_good_log.write(line)
        except ValueError:
            file_bag_log.write(f'{edit_line} - пустая строка или несоответствие по количеству полей\n')

        except WrongName:
            file_bag_log.write(f'{edit_line} - неверное значение в поле "name"\n')

        except NotNumber:
            file_bag_log.write(f'{edit_line} - поле "age" не является числом или введен не корректный возраст\n')
        except NotEmailError:
            file_bag_log.write(f'{edit_line} - поле "email" отсутствует или не содержит "@" или "."\n')

# Зачёт!
