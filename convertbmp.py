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


def generator(save, l, count):
    global test_var
    global a_proc
    if a_proc[0][1] == count+1:
        print(a_proc[0][0], '%')
        a_proc.pop(0)
    if test_var >= 117:
        test_var = l
        return str(save) + ',\n' + ' ' * l
    test_var += len(str(save)) + 1
    return str(save) + ','

# @thread
def create_py_file(namefile):
    global test_var
    global a_proc
    if (namefile.find('.png') < 0) and (namefile.find('.bmp') < 0) and (namefile.find('.jpg') < 0):
        print('no file image')
        return False
    name_var = namefile.replace('.', '_') + '=bytes(['
    try:
        print('OPEN -', namefile)
        my_image = pygame.image.load(namefile).convert_alpha()
        png_string = pygame.image.tostring(my_image, 'RGB')
    except:
        print('errore open  image file')
        return False
    create_my_file = name_var[:name_var.find('_')] + '.py'
    print('RENDERING - ', len(png_string), ' bytes ')
    a_proc.clear()
    a_proc = procent(len(png_string), 10)
    test_var = len(name_var) - 1
    buf = ''.join([generator(c, len(name_var), count) for count, c in enumerate(png_string)])
    print('CORRECTED')
    if buf[-1] == ',':
        buf = buf[:-1]
    try:
        im = Image.open(namefile)
        f = open(create_my_file, 'w')
        print('CREATE -', create_my_file)
    except:
        print('error open file:', create_my_file)
        return False
    print("SAVE -", create_my_file)
    try:
        f.write("# X-" + str(im.size[0]) + ' Y-' + str(im.size[1]) + '\n' + name_var + buf + '])\n')
        f.close()
    except:
        print('error write file', create_my_file)
        return False
    print('COMPLETE image X-' + str(im.size[0]) + ' Y-' + str(im.size[1]), getSize(create_my_file), 'bytes')
    return True


ERROR = 0
cursor = 0
N = 20
M = 1
w = M * 200
h = N * 20
running = True
pygame.init()
screen = pygame.display.set_mode([w, h])
pygame.display.set_caption('Convert BMP in PY')
font = pygame.font.SysFont('arial', 18)
text = []
del_dir = []
path_dir = (os.listdir(path="."))
path_dir.insert(0, '..')
for i in path_dir:
    if cursor == path_dir.index(i):
        text.append(font.render(i, 1, (232, 238, 255), (11, 54, 98)))
    else:
        text.append(font.render(i, 1, (232, 238, 255)))
for i in text:
    screen.blit(i, (10, text.index(i) * N))
pygame.display.update()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            ERROR = 0
            if event.key == pygame.K_RETURN:
                try:
                    os.chdir(path_dir[cursor])
                    cursor = 0
                    text = []
                    del_dir = []
                    path_dir = (os.listdir(path="."))
                    path_dir.insert(0, '..')
                except:
                    if not create_py_file(path_dir[cursor]):
                        print(' cursor -', cursor)
                        ERROR = cursor
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP:
                cursor -= 1
                if (len(del_dir) > 0) and (cursor == -1):
                    path_dir.insert(0, del_dir[len(del_dir) - 1])
                    del_dir.pop()
                if cursor == -1:
                    cursor = 0
            if event.key == pygame.K_DOWN:
                if len(path_dir) - 1 > cursor:
                    cursor += 1
                    if (len(path_dir) > N) and (cursor == 20):
                        del_dir.append(path_dir[0])
                        path_dir.pop(0)
                    if cursor == 20:
                        cursor = 19
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass
            text.clear()
            screen.fill((0, 0, 0))
            for i in path_dir:
                if cursor == path_dir.index(i):
                    if ERROR:
                        text.append(font.render(i, 1, (232, 238, 255), (255, 80, 29)))
                    else:
                        text.append(font.render(i, 1, (232, 238, 255), (11, 54, 98)))
                else:
                    text.append(font.render(i, 1, (232, 238, 255)))
            for i in text:
                screen.blit(i, (10, text.index(i) * N))
            pygame.display.update()
pygame.quit()
