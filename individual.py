#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def outer():
    def inner(x):
        return x + 3
    return inner


if __name__ == "__main__":
    cnt = outer()
    k = int(input("Введите значение k: "))
    result = cnt(k)
    print("Результат:", result)
