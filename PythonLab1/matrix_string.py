from math import sqrt


def is_number_palindrome(a):
    stack = []
    if type(a) == int:
        while a:
            if len(stack) >= 1:
                top_number = stack.pop()
                if top_number != a % 10:
                    if len(stack) >= 1:
                        one_before = stack.pop()
                        if one_before != a % 10:
                            stack.append(one_before)
                            stack.append(top_number)
                            stack.append(a % 10)
                    else:
                        stack.append(top_number)
                        stack.append(a % 10)
            else:
                stack.append(a % 10)
            a = a // 10
        if len(stack) > 0:
            return False
        return True
    else:
        print('The given parameter is not an integer!')


def number_from_text(my_string):
    if type(my_string) == str:
        found_number = False
        number = 0
        for i in my_string:
            if ord('0') <= ord(i) <= ord('9'):
                found_number = True
                number = number * 10 + int(i)
            elif found_number:
                break
        return number
    print('The given input is not a string!')


def number_of_bits(a):
    if type(a) == int:
        contor = 0
        for i in bin(a):
            if i == '1':
                contor += 1
        return contor
    else:
        print('The given parameter is not an integer!')


def most_common_letter(my_string):
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
    if type(my_string) == str:
        for c in my_string:
            if ord('A') <= ord(c) <= ord('Z'):
                arr[ord(c) - ord('A')] += 1
            if ord('a') <= ord(c) <= ord('z'):
                arr[ord(c) - ord('a')] += 1
        maxim = arr[0]
        poz_max = 0
        contor = 0
        for i in arr:
            if i > maxim:
                maxim = i
                poz_max = contor
            contor += 1
        return str(chr(poz_max+ord('a')))
    else:
        print('The given input is not a string!')


def number_of_words(my_string):
    if type(my_string) == str:
        return len(my_string.split())
    else:
        print('The given input is not a string!')


def create_matrix(row_count, data_list):
    mat = []
    for i in range(row_count):
        row_list = []
        for j in range(row_count):
            row_list.append(data_list[row_count * i + j])
        mat.append(row_list)
    return mat


def matrix_spiral_print(size, my_matrix):
    for i in range(size // 2):
        for j in range(size-2*i):
            print(str(my_matrix[i][j+i]), sep='', end='')
        for j in range(size-2*i-1):
            print(str(my_matrix[j+i+1][size-i-1]), sep='', end='')
        for j in range(size-2*i-2, i, -1):
            print(str(my_matrix[size-i-1][j]), sep='', end='')
        for j in range(size-2*i-1, i, -1):
            print(str(my_matrix[j][i]), sep='', end='')
    if size % 2:
        print(str(my_matrix[size//2][size//2]), sep='', end='')
    else:
        print(str(my_matrix[size // 2][size // 2 - 1]), sep='', end='')


if __name__ == '__main__':
    matrix_spiral_print(4, create_matrix(4, ['f', 'i', 'r', 's', 'n', '_', 'l', 't', 'o', 'b', 'a', '_', 'h', 't', 'y',
                                             'p']))