from random import *
import uk
import time
import pygame
import threading
import word
import crossword

full = False
cross_word = []


def thread(my_func):
    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs)
        my_thread.start()

    return wrapper


class CrossWord:

    def __init__(self):
        self.word_cross = []
        # self.WORDS = word.data_words
        self.WORDS = uk.uk_txt

        self.crossword = []
        self.time = 0
        self.index_words = self.optimize()
        self.num_len_words = []
        print(len(self.WORDS))
    def optimize(self):
        a = []
        k = 0
        # a = [[self.WORDS.index(min(self.WORDS, key=lambda k: len(k) < i)),
        #       self.WORDS.index(min(self.WORDS[::-1], key=lambda k1: len(k1) < i))] for i in range(16)]
        #
        for i in self.WORDS:
            if len(i) > k:
                k = len(i)
        for i in range(k):
            a.append([0, 0])
            for ii in range(len(self.WORDS)):
                if len(self.WORDS[ii]) == i:
                    a[i][0] = ii
                    break
            for ii in range(len(self.WORDS)-1,0,-1):
                if len(self.WORDS[ii]) == i:
                    a[i][1] = ii
                    break




        return a

    def boo(self, f, s):
        for k in range(len(f)):
            if f[k] == s[k] or s[k] == '.':
                pass
            else:
                return False

        return True

    def find(self, text):
        a = []
        one_word = text
        begin, top = self.index_words[len(text)]
        chain = False
        # print(begin,top,text)
        # self.time = time.time()
        for i in range(begin, top):
            if self.boo(self.WORDS[i], text):
                a.append(self.WORDS[i])
                # chain = True
            # else:
            #     if chain:
            #         break
        if a:
            one_word = a[randint(0, len(a) - 1)]
            self.word_cross.append(one_word)
        # print(time.time()-self.time)
        # print(one_word)
        return one_word

    # def RND(self, N):
    #     randomize = self.WORDS[randint(0, len(self.WORDS) - 1)]
    #     while len(randomize) != N:
    #         randomize = self.WORDS[randint(0, len(self.WORDS) - 1)]
    #     return randomize
    @thread
    def solver(self, cross):
        global full
        global cross_word
        long = 0
        self.word_cross = []
        self.crossword = []
        crossword = cross.copy()

        for i in cross:
            for k in i.split('X'):
                if len(k) >= 3:
                    long += 1
                    # self.num_len_words.append(len(k))

        for i in [''.join(i) for i in list(zip(*cross))]:
            for k in i.split('X'):
                if len(k) >= 3:
                    long += 1
                    # self.num_len_words.append(len(k))
        # self.num_len_words = set(self.num_len_words)
        # if len(self.num_len_words) % 2:
        #     self.num_len_words.append(2).sort()
        # print()

        while len(self.word_cross) < long:
            self.time = time.time()
            self.word_cross = []
            crossword = cross.copy()

            for step in range(18, 2, -1):
                for x, i in enumerate(crossword):
                    for k in i.split('X'):
                        if (len(k) >= step) and ('.' in k):
                            crossword[x] = crossword[x].replace(k, self.find(k), 1)

                crossword = [''.join(i) for i in list(zip(*crossword))]
                for x, i in enumerate(crossword):
                    for k in i.split('X'):
                        if (len(k) >= step) and ('.' in k):
                            crossword[x] = crossword[x].replace(k, self.find(k), 1)
            cross_word = crossword.copy()
            if len(self.word_cross) == long or full:
                full = True
            # print(self.word_cross)
            cross_word = crossword.copy()
            print(f'{time.time() - self.time:.2f}sec {long}-{len(self.word_cross)}')
            if full:
                return
        full = True
        return crossword


class DrawCrossword:

    def __init__(self):
        # self.N = 30  # ------------------------------------------Ширина
        # self.M = 20
        self.matrix = []
        self.size = 30
        self.M = 0
        self.N = 0
        self.clock = None
        self.screen = None
        self.f1 = None

    def change(self, matrix):
        self.matrix = matrix

    def init(self, matrix):
        self.M = len(matrix)
        self.N = len(matrix[0])
        pygame.init()
        self.screen = pygame.display.set_mode([self.size * self.N, self.size * self.M])
        self.f1 = pygame.font.Font(None, 37)
        self.clock = pygame.time.Clock()
        self.matrix = matrix

    # @thread
    def draw(self):
        global full
        global cross_word
        while True:
            time.sleep(0.1)
            # for event in pygame.event.get():  # ------------------------------------------События нажатия клавиш
            #     if event.type == pygame.QUIT:
            #         full = True

            # for i in cross_word:
            #     print(i)
            # print()
            rotate_matrix = [''.join(i) for i in list(zip(*cross_word))]
            for x in range(self.N):
                for y in range(self.M):
                    if rotate_matrix[x][y] == 'X':
                        pygame.draw.rect(self.screen, (1, 200, 200),
                                         (x * self.size, y * self.size,
                                          self.size - 1, self.size - 1))
                    elif rotate_matrix[x][y] == '.':
                        pygame.draw.rect(self.screen, (255, 255, 255),
                                         (x * self.size, y * self.size,
                                          self.size - 1, self.size - 1))

                    elif rotate_matrix[x][y] == 'ф':
                        pygame.draw.rect(self.screen, (255, 255, 255),
                                         (x * self.size, y * self.size,
                                          self.size - 1, self.size - 1))
                        text2 = self.f1.render(rotate_matrix[x][y], 0, (0, 0, 0))
                        self.screen.blit(text2, (x * self.size+1, y * self.size + 1))


                    else:

                        pygame.draw.rect(self.screen, (255, 255, 255),
                                         (x * self.size, y * self.size,
                                          self.size - 1, self.size - 1))
                        text2 = self.f1.render(rotate_matrix[x][y], 0, (0, 0, 0))
                        self.screen.blit(text2, (x * self.size + 4, y * self.size + 1))


            pygame.display.update()
            if full:
                return
            for event in pygame.event.get():  # ------------------------------------------События нажатия клавиш
                if event.type == pygame.QUIT:
                    full = not full
                    return

    def close(self):
        while True:
            for event in pygame.event.get():  # ------------------------------------------События нажатия клавиш
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
        return


if __name__ == '__main__':
    c = CrossWord()
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
    d = DrawCrossword()
    cross_word = matrix.copy()
    d.init(matrix)
    d.change(matrix)
    c.solver(matrix)
    d.draw()
    # while not full:
    # d.change(c.solver(matrix))
    d.close()
