from random import randint

min_number = int(input('Please Enter the min number: '))
max_number = int(input('Please Enter the max number: '))

if (max_number< min_number):
    print('invalid input - Shutting down....')
else:
    rand_number = randint(min_number, max_number)
    print(rand_number)