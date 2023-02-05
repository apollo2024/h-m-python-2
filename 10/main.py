# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# 5 -> 1 0 1 1 0
# 2
import array as arr
import random


n = int(input())
coins = [random.randint(0, 1) for i in range(n)]

print(coins)

eagles = 0
tails = 0

for i in range(len(coins)):
    if coins[i] == 0:
        eagles += 1
    else:
        tails += 1

if eagles > tails:
    print(f'нужно перевернуть: {tails}')    
else:
    print(f'нужно перевернуть: {eagles}')