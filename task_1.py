# основная ветка программы, не считая заголовков функций,
# состоит из двух строки кода. Это вызов функции test() и инструкции if __name__ ==
# '__main__' . В ней запрашивается на ввод целое число. Если оно положительное, то
# вызывается функция positive(), тело которой содержит команду вывода на экран слова
# "Положительное". Если число отрицательное, то вызывается функция negative(), ее тело
# содержит выражение вывода на экран слова "Отрицательное".

def positive():
    print('Положительное')


def negative():
    print('Отрицательное')


def test():
    num = int(input('>>>'))
    if num % 2 == 0:
        positive()
    else:
        negative()


if __name__ == '__main__':
    test()
