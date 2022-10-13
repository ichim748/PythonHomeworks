if __name__ == '__main__':
    first_string = str(input('Enter the first string: '))
    second_string = str(input('Enter the second string: '))
    print('The second string can be found in the first string ' + str(first_string.count(second_string)) + ' times')