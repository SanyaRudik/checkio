from random import *
import uk
# import time
# import pygame
import threading
import word
import copy
import crossword

def thread(my_func):
    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs)
        my_thread.start()

    return wrapper
class CrossWords:
    def __init__(self, matrix):
        self.matrix = [[matrix[y][x] for x in range(len(matrix[0]))] for y in range(len(matrix))]
        # self.matrix = self.convert()
        self.c_matrix = tuple([[matrix[y][x] for x in range(len(matrix[0]))] for y in range(len(matrix))])
        self.count = self.word_count()
        self.X, self.Y = self.height_width()
        self.dict_word = self.creat_dict()
        self._sortcount()
        self.WORDS = uk.uk_txt
        # self.WORDS = word.data_words
        self.index_words = self.optimize()
        # print('---CONVERT----')
        # self.c_matrix = self.matrix.copy()
        # for i in self.c_matrix:
        #     print(i)

    # def convert(self):
    #
    #     return [[self.matrix[y][x] for x in range(len(self.matrix[0]))] for y in range(len(self.matrix))]

    def optimize(self):
        a = []
        k = 0
        for i in self.WORDS:
            if len(i) > k:
                k = len(i)
        for i in range(k):
            a.append([0, 0])
            for ii in range(len(self.WORDS)):
                if len(self.WORDS[ii]) == i:
                    a[i][0] = ii
                    break
            for ii in range(len(self.WORDS) - 1, 0, -1):
                if len(self.WORDS[ii]) == i:
                    a[i][1] = ii
                    break

        return a

    def _sortcount(self):
        self.count = sorted(self.count, key=lambda kv: len(self.dict_word[tuple(kv)]['cross']), reverse=True)

    def top_cross(self, word):
        a = []
        for c, i in enumerate(self.count[word]):
            for c_c, i_i in enumerate(self.count):
                if (word != c_c) and (i in i_i):
                    a.append(i_i)
        return a

    def put_name(self, tup):
        # for i in tup:
        # print(i)
        return ''.join([str(self.matrix[x][y]) for x, y in tup])

    def creat_dict(self):
        d = {}
        for i in range(len(self.count)):
            d[tuple(self.count[i])] = {'name': '',
                                       'cross': self.top_cross(i),
                                       'dict': []}
        return d

    def height_width(self):
        if len(self.matrix):
            return len(self.matrix), len(self.matrix[0])
        return len(self.matrix), 0

    def _render_str(self, row):
        a = []
        for i in row:
            if i == '.' and a and a[-1][-1] == '.':
                a[-1] += i
            else:
                a.append(i)
        return a

    def word_count(self):
        count = []
        for c_c, i in enumerate(self.matrix):
            poz_bar = 0
            # print(self._render_str(i))
            for k in self._render_str(i):
                if len(k) >= 3:
                    count.append([(c_c, y) for y in range(poz_bar, poz_bar + len(k))])
                poz_bar += len(k)
        for c_c, i in enumerate([''.join(i) for i in list(zip(*self.matrix))]):
            poz_bar = 0
            # print(self._render_str(i))
            for k in self._render_str(i):
                if len(k) >= 3:
                    count.append([(x, c_c) for x in range(poz_bar, poz_bar + len(k))])
                poz_bar += len(k)
        return count

    def print_all_word(self):
        self.original_matrix()

        for i in self.count:
            dd = self.dict_word[tuple(i)]['name']
            if not len(dd):
                continue
            for c, [x, y] in enumerate(i):
                # print(c, x, y)
                if dd[c] != '.':
                    self.matrix[x][y] = dd[c]
        crossword.cross_word = [''.join(x) for x in self.matrix]
        # for i in c.matrix:
        # mat.append(''.join(i))

    def boo(self, f, s):
        for k in range(len(f)):
            if f[k] == s[k] or s[k] == '.':
                pass
            else:
                return False

        return True

    def get_word(self, text):
        return ''.join([str(self.matrix[x][y]) for x, y in text])

    def find(self, text):  # ---------------------------------        FIND
        a = []
        one_word = self.get_word(text)
        # print(one_word)
        begin, top = self.index_words[len(text)]
        for i in range(begin, top):
            if self.boo(self.WORDS[i], one_word):
                a.append(self.WORDS[i])

        return a

    def check_all_name(self):
        for i in self.count:
            # print(self.dict_word[tuple(i)]['name'])
            if not len(self.dict_word[tuple(i)]['name']):
                return True
        return False

    def RND(self, name):
        if not len(name):
            return ''
        return name[randint(0, len(name) - 1)]

    def original_matrix(self):
        self.matrix = [[self.c_matrix[y][x] for x in range(len(self.c_matrix[0]))] for y in
                       range(len(self.c_matrix))]

    @thread
    def main(self):
        num = 0
        a = ''
        self.print_all_word()
        while self.check_all_name() and (num < len(self.count)):
            i = self.count[num]
            d_d = self.dict_word[tuple(i)]['dict']

            if not len(d_d):
                self.dict_word[tuple(i)]['dict'] = self.find(i)

            self.dict_word[tuple(i)]['name'] = self.RND(self.dict_word[tuple(i)]['dict'])
            if not len(self.dict_word[tuple(i)]['name']):
                self.dict_word[tuple(i)]['name'] = ''
                print(' ---- PROBLEM ----')
                num = 0
                self.dict_word[tuple(i)]['dict'] = []
                continue
            for cr_w in self.dict_word[tuple(i)]['cross']:
                self.print_all_word()
                self.dict_word[tuple(cr_w)]['dict'] = self.find(cr_w)
                if not len(self.dict_word[tuple(cr_w)]['dict']):
                    self.dict_word[tuple(cr_w)]['dict'] = self.find(cr_w)

                    if a == self.dict_word[tuple(i)]['name']:


                        self.dict_word.clear()
                        self.dict_word = self.creat_dict()
                        a = 0
                        num = -1
                        self.original_matrix()
                        if len(self.dict_word[tuple(i)]['name']):
                            self.dict_word[tuple(i)]['dict'].remove(self.dict_word[tuple(i)]['name'])

                        break

                    a = self.dict_word[tuple(i)]['name']
                    # print(self.dict_word[tuple(i)]['name'], '--------------------------', num)
                    if len(self.dict_word[tuple(i)]['name']):
                        self.dict_word[tuple(i)]['dict'].remove(self.dict_word[tuple(i)]['name'])
                        # self.WORDS.remove(self.dict_word[tuple(i)]['name'])
                    self.dict_word[tuple(i)]['name'] = ''
                    num -= 1
                    break
            num += 1

        return


matrix = ['.................X.................',
          '.XXXXXXX.XXXXXXXXX.XXXXXXX.XXXXXXXX',
          '.................X.................',
          '.X.X.XXX.XXX.X.X.X.X.X.XXX.XXX.X.X.',
          '.....X.....X.....X.....X.....X.....',
          '.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.',
          '.................X.................',
          'XX.X.X.XXX.X.X.X.XXX.X.X.XXX.X.X.X.',
          '...........X.X.X...X.X.X.....X.....',
          '.X.X.XXXXXXX.X.XXX.X.X.XXXXXXX.X.XX',
          '....X.......X.........X.......X....',
          '.XXX.XXX.XXXXXXX.X.X.X.XXX.XXXX.XX.',
          '.................X.................',
          '.X.X.XXX.XX.X.XX.X.X.X.XXX.XX.X.XX.',
          '.X.X.XXX.XX.X.XX.X.X.X.XXX.XX.X.XX.',
          '.X.......XX......X.X.......XX......']
#
# matrix = ['....XXX.X',
#           'XXX.X....',
#           'X....XX.X']


# matrix = ['......XXX.X',
#           'X.XXX.X....',
#           'X......XX.X',
#           'X.XXX.X....',
#           '........X.X',
#           '.XXXX.XXX.X',
#           '.XX.......X',
#           '....X.XXX.X',
#           '.XX.X.XXXXX',
#           'X...X......']
c = CrossWords(matrix)

# for i in c.dict_word:
#     print(c.dict_word[i]['name'], i)
    # for i_i in c.dict_word[i]['name']:
    #     print(i_i)
print('------------------------------------------------------------------------')
# for i in c.count:
#     print(i)
# print(c.index_words)
mat = []
c.main()
c.print_all_word()
for i in c.matrix:
    mat.append(''.join(i))
# for i in c.dict_word:
#     print(c.dict_word[i]['name'])

d = crossword.DrawCrossword()
crossword.cross_word = mat.copy()
d.init(mat)
d.change(mat)
# c.solver(matrix)
d.draw()
d.close()
