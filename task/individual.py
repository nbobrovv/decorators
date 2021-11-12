#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Объявите функцию с именем get_sq , которая вычисляет площадь прямоугольника по двум
параметрам: width и height – ширина и высота прямоугольника и возвращает результат.
Определите декоратор для этой функции с именем (внешней функции) func_show , который
отображает результат на экране в виде строки (без кавычек): "Площадь прямоугольника:
<значение>". Вызовите декорированную функцию get_sq.
"""


def func_show(func):

    def get_sq(**kwargs):
        x = 1
        for v in kwargs.values():
            x *= int(v)
        func(x)
    return get_sq


@func_show
def result(kwargs):
    print(f"Площадь прямоугольника: {kwargs}")


if __name__ == '__main__':
    result(width=4, height=6)