import math


def is_prime(x:int):
    if x % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(x)+1)):
            if x % i == 0:
                return False
        return True


def process_item(x):
    while True:
        x += 1
        if is_prime(x):
            return x


x = int(input('Enter the value for x: '))
print('The value returned by process_item for the value ' + str(x) + ' is ' + str(process_item(x)))