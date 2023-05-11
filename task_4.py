#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    return input('Введите параметры: ')


def test_input(num):
    try:
        if int(num):
            return True
    except ValueError:
        return False


def str_to_int(num):
    return int(num)


def print_int(num):
    print(num)

if __name__ == '__main__':
    numer = get_input()
    if test_input(numer):
        numer = str_to_int(numer)
        print(numer)
    else:
        print('число нельзя преобразовать')
