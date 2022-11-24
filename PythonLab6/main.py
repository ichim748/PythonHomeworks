import os
import re
import xml.etree.ElementTree as XML


def ex1(text):
    return [i for i in re.split('[^a-zA-Z1-9]', text) if i != '']


def ex2(regex_string, text_string, x):
    return list(set(i for i in re.split('\s', text_string) if re.match(regex_string, i) and len(i) == x))


def ex3(string, regular_expressions):
    return list(set(i for i in re.split('\s', string) for j in regular_expressions if re.match(j, i)))


def ex4(path, attrs):
    tree = XML.parse(path)
    output = []
    for node in tree.iter():
        buba = False
        for i in node.attrib:
            if not attrs.keys().__contains__(i) or (attrs.keys().__contains__(i) and node.attrib[i] != attrs[i] or i not in node.attrib):
                buba = True
                break
        if not buba and node != tree.getroot():
            output.append(node.tag)
    return list(set(output))


def ex5(path, attrs):
    tree = XML.parse(path)
    output = []
    for node in tree.iter():
        for i in attrs.keys():
            if node.attrib.__contains__(i) and node.attrib[i] == attrs[i]:
                output.append(node.tag)
                break
    return list(set(output))


def ex6(text):
    for i in re.split(' ', text):
        if re.match("(?i)^[aeiou][a-z]+[aeiou]$", i):
            temp = i
            for j in range(len(temp)):
                if j % 2 == 1:
                    temp = temp.replace(i[j], '*')
            text = text.replace(i, temp)
    return text


def ex7(cnp):
    result = re.match("(?P<gen>\d)(?P<an>\d\d)(?P<luna>\d\d)(?P<zi>\d\d)(?P<judet>\d\d)(?P<nr_ordine>\d\d\d)(?P<nr_control>\d)", cnp)
    if 1 <= int(result.group('gen')) <= 9 and 0 <= int(result.group('an')) <= 99 and 1 <= int(result.group('luna')) <= 12:
        if int(result.group('luna')) in [1, 3, 5, 7, 8, 10, 12] and 1 <= int(result.group('zi')) <= 31:
            if cifra_validare(cnp) == int(result.group('nr_control')):
                return True
            else:
                return False
        elif int(result.group('luna')) in [4, 6, 9, 11] and 1 <= int(result.group('zi')) <= 30:
            if cifra_validare(cnp) == int(result.group('nr_control')):
                return True
            else:
                return False
        elif int(result.group('luna')) == 2 and 1 <= int(result.group('zi')) <= 29:
            if cifra_validare(cnp) == int(result.group('nr_control')):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def cifra_validare(cnp):
    cnp = str(cnp)
    nr_control = '279146358279'
    suma = 0
    for i in range(len(nr_control)):
        suma += int(cnp[i]) * int(nr_control[i])
    if suma % 11 < 10:
        return suma % 11
    elif suma % 11 == 10:
        return 1


def ex8(path, regular_expression):
    output = []
    for root, directories, files in os.walk(path):
        for file in files:
            if re.match(regular_expression, file):
                f = open(root + '\\' + file, 'r')
                prezent = False
                for i in f.readline():
                    if re.match(regular_expression, i):
                        prezent = True
                        break
                if prezent:
                    output.append("<<" + file)
                else:
                    output.append(file)
    return output


if __name__ == '__main__':
    print(ex1('Un text, oarecare, .'))
    # print(ex2('\w+' , 'Ceva altceva nu stiu buba', 4))
    # print(ex3('Un text oarecare 0745075496 0745075496', ["07[0-9]"]))
    # print(ex4('C:\\Users\\Cosmin\\PycharmProjects\\PythonLab6\\test.xml', {'camp_unu' : 'Ceva', 'camp_doi' : 'Altceva'}))
    # print(ex5('C:\\Users\\Cosmin\\PycharmProjects\\PythonLab6\\test.xml', {'camp_unu': 'Ceva', 'camp_doi': 'Altceva'}))
    # print(ex6('unu doi trei patru altceva ceva apt'))
    # print(ex7('1270632341710'))
    # print(ex7('1270623341710'))
    # print(ex8('C:\\Users\\Cosmin\\PycharmProjects\\PythonLab6', "[a-z]+"))
