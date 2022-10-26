import string


def ex1(a:list, b:list):
    output = []
    intersection = {i for i in a if i in b}
    reunion = {i for i in a or b}
    difference1 = {i for i in a if i not in b}
    difference2 = {i for i in b if i not in a}
    output += [intersection, reunion, difference1, difference2]
    return output


def ex2(a:string):
    dictionary = {}
    for i in a:
        added = False
        for j in dictionary.items():
            if j[0] == i:
                dictionary[i] += 1
                added = True
        if not added:
            dictionary[i] = 1
    return dictionary


def ex3(a, b):
    differences1 = [i for i in a if i not in b]
    differences2 = [i for i in b if i not in a]
    if len(differences1) > 0 or len(differences2) > 0:
        return False
    return True


def ex4(tag, content, **name_parameters):
    output = '<' + tag.strip() + ' '
    for i in name_parameters.items():
        output += i[0].strip()
        output += '=\\'
        output += '"'
        output += i[1].strip()
        output += ' \\"'
    output += '> '
    output += content.strip()
    output += ' </'
    output += tag.strip()
    output += '>'
    return output


def ex5(validation_rules, dictionary):
    for i in dictionary.keys():
        exists = False
        for j in validation_rules:
            if j[0] == i:
                exists = True
                values = j
                break
        if not exists:
            return False
        if (values[1] != '' and dictionary[i].find(values[1]) == -1) or (values[1] != '' and dictionary[i].find(values[1]) != 0) or (values[2] != '' and dictionary[i].find(values[2]) == -1) or (values[3] != '' and dictionary[i].find(values[3]) == -1) or (values[3] != '' and dictionary[i].find(values[3]) != len(dictionary[i]) - len(values[2])):
            return False
        return True


def ex6(a: list):
    dictionary = {}
    for i in a:
        added = False
        for j in dictionary.items():
            if j[0] == i:
                dictionary[i] += 1
                added = True
        if not added:
            dictionary[i] = 1
    unique = [i for i in dictionary.keys() if dictionary[i] == 1]
    not_unique = [i for i in dictionary.keys() if dictionary[i] != 1]
    return len(unique), len(not_unique)


def ex7(*sets):
    output_string = ''
    for i in range(0, len(sets)):
        for j in range(i+1, len(sets)):
            if sets[i] is not None and sets[j] is not None:
                output = ex1(list(sets[i]), list(sets[j]))
                temp_string = str(sets[i]) + ', ' + str(sets[j]) + '=> \n'
                temp_string += '{ \n'
                temp_string += '"' + str(sets[i]) + ' | ' + str(sets[j]) + '":' + str(output[1]) + ',\n'
                temp_string += '"' + str(sets[i]) + ' & ' + str(sets[j]) + '":' + str(output[0]) + ',\n'
                temp_string += '"' + str(sets[i]) + ' - ' + str(sets[j]) + '":' + str(output[2]) + ',\n'
                temp_string += '"' + str(sets[j]) + ' - ' + str(sets[i]) + '":' + str(output[3]) + ',\n'
                temp_string += '} \n'
                output_string += temp_string
    return output_string


def ex8(mapping):
    y = mapping.get("start")
    visited_key = [y]
    z = mapping.get(y)
    while z not in visited_key:
        visited_key.append(z)
        next_element = mapping.get(z)
        z = next_element
    return visited_key


def ex9(*args, **kwargs):
    counter = 0
    if len(args) != len(kwargs):
        return None
    for i in range(0, len(args)):
        for j in kwargs.keys():
            if kwargs[j] == i:
                counter += 1
    return counter


if __name__ == '__main__':
    print(ex9(1, 2, 3, 4, x=1, y=2, z=3, w=5))
    #print(ex8(({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})))
    #print(ex7({1, 2}, {2, 3}, {1, 4}))
    #print(ex6([1, 2, 3, 4, 5, 6, 7, 7]))
    #print(ex5({("key1", "", "inside", "")}, {"key1": "come inside, it's too cold out"}))
    #print(ex4("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") )
    #print(ex3({1:'donkey', 2:'chicken', 3:'dog'}, {1:'donkey', 2:'chimpansee', 4:'chicken'}))
    #print(ex2('ala bala portocala'))
    #print(ex1([1, 2, 3], [3, 2, 4]))