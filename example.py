#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def add_two(a):
    x = 2
    return a + x


def add_four(a):
    x = 2

    def add_some():
        print(f'Вывод внутри вложенной функции add_some(): {str(x)}')
        return a + x

    return add_some()


x = 4


def fun():
    print(f'Вывод при вызове функции fun(): {x + 3}')


def fun1(a):
    x = a * 3
    def fun2(b):
        nonlocal x
        return b + x
    return fun2


if __name__ == '__main__':
    print(f'Вывод функции add_two(4): {add_two(4)}')
    print(f'Вывод функции add_four(5): {add_four(5)}')
    fun()
    test_fun = fun1(4)
    print(f'Вывод замыкания: {test_fun(7)}')
    