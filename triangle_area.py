# Liam Toebbe
# 10/12/2023

import math


def s(a, b, c):
    (a+b+c)/2


def area(s, a, b, c):
    math.sqrt(2)(s * (s - a) * (s - b) * (s - c))


print(area(3, 2, 2, 2))
