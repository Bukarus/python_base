#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)

my_family = ['me', 'mother', 'father', 'sister', 'brother', 'grandma', 'grandpa', ]
# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['me', 171], ['mother', 165], ['father', 172], ['sister', 169], ['brother', 175], ['grandma', 158],
    ['grandpa', 170],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца -', my_family_height[2][1], 'см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
total_height = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1] + \
               my_family_height[4][1] + my_family_height[5][1] + my_family_height[6][1]
print('Общий рост моей семьи - ', total_height, 'см')
