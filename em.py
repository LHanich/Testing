from random import *
 
 
numbers = range(1, 51)  # create a number list, start from 1 to 50
numbers_p = range(1, 12)
 
shuffle(numbers)  # shuffle the numbers list
shuffle(numbers_p)
 
x = sample(numbers, 5)  # pick 5 random number from shuffled list
y = sample(numbers_p, 2)
 
print x, y