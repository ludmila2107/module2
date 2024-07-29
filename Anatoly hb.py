# import random
#
# fruits = ['яблоко', 'банан', 'апельсин', 'груша', 'киви']
# random_fruit = random.choice(fruits)
# print(random_fruit)

import random

fruits = ['яблоко', 'банан', 'апельсин', 'груша', 'киви']
random_fruit = random.randint(0, len(fruits)-1)
print(random_fruit)
print(fruits[random_fruit])




