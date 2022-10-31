import os


def ex1(path):
    output = set()
    for root, directories, files in os.walk(path):
        for file in files:
            output.add(os.path.basename(file).split('.')[1])
    return sorted(output)


def ex2(path, file):
    if os.path.exists('./' + file):
        f = open('./' + file, 'w')
    else:
        f = open('./' + file, 'x')
    for root, directories, files in os.walk(path):
        for file1 in files:
            if file1 is not None:
                if os.path.join(root, file1).startswith('C'):
                    f.write(os.path.join(root, file1)+'\n')
    f.close()


def ex3(my_path):
    if os.path.isfile(my_path):
        f = open(my_path, 'r')
        return f.read()[-20:]
    elif os.path.isdir(my_path):
        output = {}
        for root, directories, files in os.walk(my_path):
            for file in files:
                if output.__contains__(os.path.basename(file).split('.')[1]):
                    output[os.path.basename(file).split('.')[1]] += 1
                else:
                    output[os.path.basename(file).split('.')[1]] = 1
        output = [(k, v) for k, v in output.items()]
        output.sort(key=lambda x: x[1], reverse=True)
        return output


def ex4():
    path = input('Enter the path of the directory')
    return ex1(path)


def ex5(target, to_search):
    if os.path.isfile(target):
        f = open(target, 'r')
        if f.read().__contains__(to_search):
            f.close()
            return True
        else:
            f.close()
            return False
    elif os.path.isdir(target):
        output_list = []
        for root, directories, files in os.walk(target):
            for file in files:
                f = open(root + '\\' + file, 'r')
                if f.read().__contains__(to_search):
                    f.close()
                    output_list.append(file)
                f.close()
        return output_list
    else:
        raise ValueError('Buba')


def ex6(target, to_search, callback):
    if os.path.isfile(target):
        f = open(target, 'r')
        if f.read().__contains__(to_search):
            f.close()
            return True
        else:
            f.close()
            return False
    elif os.path.isdir(target):
        output_list = []
        for root, directories, files in os.walk(target):
            for file in files:
                f = open(root + '\\' + file, 'r')
                if f.read().__contains__(to_search):
                    f.close()
                    output_list.append(file)
                f.close()
        return output_list
    else:
        callback(ValueError('Buba'))


def ex7(file_path):
    dictionary = {}
    dictionary['full_path'] = os.path.abspath(file_path)
    dictionary['file_size'] = os.stat(file_path).st_size
    if os.path.basename(file_path).split('.')[1]:
        dictionary['file_extension'] = os.path.basename(file_path).split('.')[1]
    else:
        dictionary['file_extension'] = ''
    f = open(file_path, 'r+')
    dictionary['can_read'] = f.writable()
    dictionary['can_write'] = f.readable()
    return dictionary


def ex8(dir_path):
    output = {}
    for root, directories, files in os.walk(dir_path):
        for file in files:
            if os.path.isfile:
                output[root + '\\' + file] = os.path.basename(file).split('.')[1]
            elif os.path.isdir:
                output[root + '\\' + file] = 'director'
    return output


if __name__ == '__main__':
    #print(ex8('C:\\Users\\Cosmin\\PycharmProjects\\PythonLab4'))
    #print(ex7('./outputLab4.txt'))
    #print(ex5('zarzavat', 'Ceva'))
    #print(ex5('./outputLab4.txt', 'Cosmin'))
    #print(ex5('C:\\Users\\Cosmin\\PycharmProjects\\PythonLab4', 'Cosmin'))
    #print(ex4())
    print(ex3('C:\\Users\\Cosmin\\PycharmProjects\\PythonLab4'))
    #ex2("C:\\Users\\Cosmin\\PycharmProjects\\PythonLab4", 'outputLab4.txt')
    #print(ex1("C:\\Users\\Cosmin\\PycharmProjects\\PythonLab4"))
