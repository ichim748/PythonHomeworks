from math import sqrt


def first_n_fibonacci(n: int):
    fib_set = []
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fib_set.append(1)
        fib_set.append(1)
        for i in range(2, n):
            fib_set.append(fib_set[i - 1] + fib_set[i - 2])
        return fib_set


def is_prime(n: int):
    if type(n) == int:
        if n % 2 == 0:
            return False
        else:
            for i in range(3, int(sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False
            return True
    else:
        return False


def prime_numbers_from_list(lista):
    return [i for i in lista if is_prime(i)]


def list_operations(lista_a, lista_b):
    intersection = [i for i in lista_a if i in lista_b]
    reunion = [i for i in lista_a + lista_b]
    a_minus_b = [i for i in lista_a if not i in lista_b]
    b_minus_a = [i for i in lista_b if not i in lista_a]
    return intersection, reunion, a_minus_b, b_minus_a


def compose(note, pasi, start):
    list_finala = []
    list_finala.append(note[start])
    for i in pasi:
        if i + start >= len(note):
            start += i
            while start >= len(note):
                start %= len(note)
            list_finala.append(note[start])
        else:
            start += i
            list_finala.append(note[start])
    return list_finala


def zero_under_main_diagonal(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, i):
            if i > j:
                matrix[i][j] = 0
    return matrix


def element_that_appears_x_times(*liste):
    contor_aparitii = {}
    x = liste[len(liste)-1]
    out_list = []
    for i in range(len(liste)-1):
        for j in liste[i]:
            if j in contor_aparitii.keys():
                contor_aparitii[j] += 1
            else:
                contor_aparitii[j] = 1
    for i in contor_aparitii.keys():
        if contor_aparitii[i] == x:
            out_list.append(i)
    return out_list


def is_palindrome(a):
    temp = a
    reverse = 0
    while temp > 0:
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp = temp // 10
    return a == reverse


def ex_8(string_list, x = 1, flag = True):
    list_of_lists = []
    for i in string_list:
        current_list = []
        for character in i:
            if ord(character) % x == 0 and flag:
                current_list.append(character)
            elif ord(character) % x != 0 and not flag:
                current_list.append(character)
        list_of_lists.append(current_list)
    return list_of_lists


def palindromes_from_list(lista):
    return len([i for i in lista if is_palindrome(i)]), max([i for i in lista if is_palindrome(i)])


def spectators_that_cant_see(matrix):
    final_output = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for t in range(i-1, -1, -1):
                if matrix[t][j] >= matrix[i][j]:
                    final_output.append([i, j])
                    break
    return final_output


def ex_10(*liste):
    output = []
    for i in range(len(liste)):
        temp = []
        for j in liste:
            if i < len(j):
                temp.append(j[i])
            else:
                temp.append(None)
        output.append(tuple(temp))
    return output


def order_tuples(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i][1][2] < lista[j][1][2]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def words_that_rhyme(lista):
    dictionary = {}
    for cuvant in lista:
        if cuvant[-2:] in dictionary:
            dictionary[cuvant[-2:]].append(cuvant)
        else:
            dictionary[cuvant[-2:]] = [cuvant]
    return list(dictionary.values())


if __name__ == "__main__":
    '''
    print(first_n_fibonacci(5))
    print(prime_numbers_from_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(list_operations([1, 2, 3], [2, 3, 4]))
    print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
    print(zero_under_main_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(element_that_appears_x_times([1, 2, 3, 4, 4], [2, 4], 2))
    print(palindromes_from_list([121, 211, 311, 414, 96369]))
    print(ex_8(["test", "hello", "lab002"], 2, False))
    print(spectators_that_cant_see([[1, 2, 3, 2, 1, 1],[2, 4, 4, 3, 7, 2],[5, 5, 2, 5, 6, 4],[6, 6, 7, 6, 7, 5]]))
    print(ex_10([1,2,3], [5,6,7], ["a", "b", "c"]))
    print(ex_10([1, 2, 3], [5, 6, 7], ["a", "b"]))
    print(order_tuples([('abc', 'bcd'), ('abc', 'zza')]))
    print(words_that_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
    '''