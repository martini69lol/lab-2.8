#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def circle(r):
    result = 3.14 * (r**2)
    return result


def cylinder():
    result = 0
    question = int(input('Если вы хотите получить площадь боковой поверхности цилиндра введите 1, '
                         'если полную площадь цилиндра введите 2'))
    if question == 1:
        h = int(input('Введите h'))
        r = int(input('Введите r'))
        circle(r)
        result = 2*3.14*r*h
    elif question == 2:
        h = int(input('Введите h'))
        r = int(input('Введите r'))
        result = 2*3.14*r*(r + h)
    return result


if __name__ == '__main__':
    cylinder()
