from utils import process_item

while True:
    x = input('Enter the desired value: ')
    print(x)
    if x == 'q':
        break
    else:
        print('The value returned by process_item for the value ' + str(x) + ' is ' + str(process_item(x)))