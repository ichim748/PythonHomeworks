def gcd(a, b):
    if type(a) == type(b) == int:
        while b:
            a, b = b, a % b
        return abs(a)


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    current_gcd = gcd(arr[0], arr[1])
    for i in range(2, len(arr)):
        current_gcd = gcd(current_gcd, arr[i])
    print('The current GCD is: ' + str(current_gcd))
