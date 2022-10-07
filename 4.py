# Реализуйте алгоритм перемешивания списка, 
# без использования встроеных методов (особенно SHUFFLE, без него)
# можно (нужно) использовать библиотеку Random

import random
list = []

for _ in range(10):
    list.append(random.randint(0,50))
print('Оригинальный список: ' + str(list))

for i in range(len(list)-1):
    j = random.randint(0, len(list)-1)
    list[i], list[j] = list[j], list[i]

print('Перемешенный список: ' + str(list))

