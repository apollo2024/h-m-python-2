# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

from random import randint
num = randint(10, 1000)

print(num)

counter = 1

while counter < num:
    print(counter,end='  ')
    counter *= 2