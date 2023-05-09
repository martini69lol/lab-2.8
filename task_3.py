# напишите функцию, которая считывает с клавиатуры числа и
# перемножает их до тех пор, пока не будет введен 0. Функция должна возвращать
# полученное произведение. Вызовите функцию и выведите на экран результат ее работы.

def enum(result):
    num = input('Введите числа: ')
    for i in num:
        if int(i) == 0:
            print(result)
            return False
        else:
            if result == 0:
                result = 1
            result *= int(i)
    print(result)


if __name__ == '__main__':
    result = 0
    while enum(result):
        enum(result)


