if __name__ == '__main__':
    first_string = input('Enter the string: ')
    for i in range(0, 26):
        first_string = first_string.replace(chr(ord('A')+i), '_'+chr(ord('a')+i))
    first_string = first_string.removeprefix('_')
    print('The new string is: ' + str(first_string))
