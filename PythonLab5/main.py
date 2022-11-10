#import utils
from inspect import signature


def sum_arguments(*args, **kwargs):
    return sum(kwargs.values())


suma = lambda *args, **kwargs: sum(kwargs.values())


def ex3(string):
    lista = []
    for i in string:
        if i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u':
            lista.append(i.lower())
    return list(lista)


vocale = lambda string: list(i.lower() for i in string if i.lower() in ['a', 'e', 'i', 'o', 'u'])


def is_vowel(x):
    return x.lower() in ['a', 'e', 'i', 'o', 'u']


vocale_filter = lambda string: list(set(filter(is_vowel, string)))


def ex4(*args, **kwargs):
    output = []
    for i in args:
        if type(i) is dict:
            if len(i.keys()) >= 2:
                bad = False
                contains_string_key = False
                for j in i.keys():
                    if type(j) == str and len(j) < 3:
                        bad = True
                    elif type(j) == str and len(j) >= 3:
                        contains_string_key = True
                if not bad and contains_string_key:
                    output.append(i)
    for i in kwargs.values():
        if type(i) is dict:
            if len(i.keys()) >= 2:
                bad = False
                for j in i.keys():
                    if type(j) == str and len(j) < 3:
                        bad = True
                if not bad:
                    output.append(i)
    return output


def is_number(i):
    return type(i) == int or type(i) == float or type(i) == complex


def ex5(list):
    output = []
    for i in list:
        if is_number(i):
            output.append(i)
        elif type(i) == list or type(i) == set or type(i) == frozenset or type(i) == tuple:
            for j in i:
                if is_number(j):
                    output.append(j)
        elif type(i) == dict:
            for j in i.keys():
                if is_number(j):
                    output.append(j)
            for j in i.values():
                if is_number(j):
                    output.append(j)
    return output


def ex6(lista):
    even = [i for i in lista if i % 2 == 0]
    odd = [i for i in lista if i % 2 == 1]
    return [(even[i], odd[i]) for i in range(len(even))]


def first_n_fib(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    elif n == 3:
        return [0, 1, 1]
    else:
        output = [0, 1, 1]
        for i in range(n-3):
            output.append(output[-1] + output[-2])
        return output


def ex7(**kwargs):
    numere = first_n_fib(1000)
    if kwargs.keys().__contains__('filters'):
        for i in kwargs.get('filters'):
            numere = list(filter(i, numere))
    if kwargs.keys().__contains__('offset'):
        offset = kwargs.get('offset')
        numere = numere[2:]
    if kwargs.keys().__contains__('limit'):
        limit = kwargs.get('limit')
        numere = numere[:limit]
    return numere


def sum_digits(x):
    return sum(map(int, str(x)))


def ex9(pairs):
    output = []
    for i in pairs:
        output.append({'sum': i[0] + i[1], 'prod': i[0] * i[1], 'pow': i[0] ** i[1]})
    return output


def ex8a(function):
    def temp(*args, **kwargs):
        print('The arguments are: ', end='')
        print('(', end='')
        for i in args:
            print(str(i) + ', ', end='')
        print('), ', end='')
        print('{', end='')
        for j in kwargs.keys():
            print(str(j) + ':' + str(kwargs.get(j)) + ', ', end='')
        print('}.', end='')
        print(' And the output of the function on all arguments is: ', end='')
        print(function(*args))
    return temp


def ex8b(function):
    def temp(*args):
        temp_result = function(*args)
        return temp_result * 2
    return temp


def ex8c(function, decorators):
    def temp(*args):
        output = function(*args)
        for i in decorators:
            output = i(function)(*args)
        return output
    return temp


def multiply_by_two(ceva):
    return ceva * 2


def add_numbers(a, b):
    return a + b


if __name__ == '__main__':
    #print(suma(1, 2, 3, c=4, d=5))
    #print(ex3('Ceva Ala bala portocala'))
    #print(vocale('Ala bala portocala'))
    #print(vocale_filter('Ala bala portocala'))
    #print(ex4({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764, dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True}))
    #print(ex5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
    #print(ex6([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))
    #print(ex7(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20], limit=2, offset=2))
    # ex8
    # augmented_multiply_by_two = ex8a(multiply_by_two)
    # x = augmented_multiply_by_two(10)
    # augmented_add_numbers = ex8a(add_numbers)
    # x = augmented_add_numbers(3, 4)
    # augmented_multiply_by_three = ex8b(multiply_by_two)
    # print(augmented_multiply_by_three(10))
    decorated_function = ex8c(add_numbers, [ex8a, ex8b])
    print(decorated_function(3, 4))
    #print(ex9(pairs=[(5, 2), (19, 1), (30, 6), (2, 2)]))
