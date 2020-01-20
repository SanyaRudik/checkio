import pygame
import os
from PIL import Image
import threading
test_var = 0
a_proc = []
tread_var = []
def thread(my_func):
    global tread_var
    print(threading.activeCount())
    # tread_var.append(my_func)
    if threading.activeCount() > 1:
        return

    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs)
        my_thread.start()
    # tread_var.pop()
    return wrapper

def procent(n, step):
    """
    :param n: Целое число
    :param step: Шаг - который нужен
    :return: Лист в [ % , Число соотвецтвующие этому %]
    """
    a = []
    for ii in range(step, 100 + step, step):
        a.append([ii, ii * n // 100])
    return a


def getSize(filename):
    st = os.stat(filename)
    return st.st_size


def generator(save, l):
    global test_var
    if test_var >= 117:
        test_var = l
        return '"' + save + '"' + ',\n' + ' ' * l
    test_var += len(str(save)) + 1
    return '"' + save + '"' + ','


def create_py_file(namefile):
    global test_var
    a = []
    if (namefile.find('.txt') < 0):
        print('no file TXT')
        return False
    name_var = namefile.replace('.', '_') + '= ['
    try:
        print('OPEN -', namefile)
        f_resurs = open(namefile, 'r', encoding="utf-8")
        data = f_resurs.readlines()
        f_resurs.close()
        for i in data:
            s = i.partition('/')
            if len(s[0]) > 3:
                a.append(s[0].replace('\n','').lower())

    except:
        print('errore open  file')
        return False
    a = sorted(a, key=len)
    for i in range(100):
        print(a[i])
    # return True



    create_my_file = name_var[:name_var.find('_')] + '.py'
    print('RENDERING - ', len(a), ' words ')
    test_var = len(name_var) - 1
    buf = ''.join([generator(c, len(name_var)) for count, c in enumerate(a)])
    print('CORRECTED')
    if buf[-1] == ',':
        buf = buf[:-1]
    try:
        # im = Image.open(namefile)
        f = open(create_my_file, 'w',encoding="utf-8")
        print('CREATE -', create_my_file)
    except:
        print('error open file:', create_my_file)
        return False
    print("SAVE -", create_my_file)
    try:
        f.write(name_var + buf + ']\n')
        f.close()
    except:
        print('error write file', create_my_file)
        return False
    print('COMPLETE', getSize(create_my_file), 'words')
    return True


create_py_file('uk.txt')