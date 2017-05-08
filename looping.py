import sys
import random
import os

for x in range(0,10):
    print(x,' ',end="")

print('\n')

grocery_list = ['juice', 'Tomatoes','Potatoes','Bannanas']

for y in grocery_list:
    print(y)


    for x in [2,4,6,8,10]:
        print(x)


    num_list = [[1,2,3],[10,20,30],[100,200,300]]

for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])

print('----while loop------')
random_num = random.randrange(0,100)

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)
