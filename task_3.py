#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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


