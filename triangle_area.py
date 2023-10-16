# Liam Toebbe
# 10/12/2023

import math


def area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(2)(s * (s - a) * (s - b) * (s - c))


print(area(2, 2, 2))
