from random import *
import pygame
import soursebmp  # ----------------------------------------- Ресурс картинок(квадратики)
import time


class Snake:
    def __init__(self):  # ------------------------------------------КОНСТРУКТОР-----------------
        self.N = 30  # ------------------------------------------Ширина
        self.M = 20  # ------------------------------------------Высота
        self.auto = False  # ------------------------------------------Автопилот Выключен
        self.head_snake = False  # ----------------------True(правда) когда сменилось направление головы змейки
        self.path_snake = []  # --------------------------Путь змейки в (вперед назад влево вправо)
        self.body_snake = [[15, 9], [15, 10], [15, 11], [15, 12]]  # -------Тело змейки Его координати в Списке
        self.s_found = True  # -------------------------------Что бы не проверять каждый раз Только когда нет пути
        self.fruit = self.rnd()  # -------------------------Случайное появление фрукта
        self.going = 'UP'  # ------------------------------------------ Направление с самого начало - Вверх
        self.speed = 0.3  # ------------------------------------------Скорость
        self.size = 16  # ------------------------------------Размер квардатиков
        self.matrix = self.matrix_ground()  # -------------------Матрица с змейкой
        self.body = [self.body_snake[0][1], self.body_snake[0][0]]  # -------------Голова змейки

    def dinamic(self, ex_s, marker=True):  # -------------------------- Пооск выхода в матрице - Динамическим способом
        x = self.body_snake[0][1]
        y = self.body_snake[0][0]
        a = []
        if marker:
            self.matrix[y][x] = ex_s
            counter = ex_s
            a.append([y, x])
        else:
            counter = ex_s
            self.matrix[y][x] = counter
            a.append([y, x])
        while len(a):
            if self.matrix[self.fruit[0]][self.fruit[1]]:  # -- then not Fruit 0
                return True
            if y > 0 and self.matrix[y - 1][x] == 0:  # y - 1  right
                if marker:
                    counter += 1
                y -= 1
                self.matrix[y][x] = counter
                a.append([y, x])
                continue
            if x < (len(self.matrix[y]) - 1) and self.matrix[y][x + 1] == 0:  # X + up
                if marker:
                    counter += 1
                x += 1
                self.matrix[y][x] = counter
                a.append([y, x])
                continue
            if x > 0 and self.matrix[y][x - 1] == 0:  # X - down
                if marker:
                    counter += 1
                x -= 1
                self.matrix[y][x] = counter
                a.append([y, x])
                continue
            if y < (len(self.matrix) - 1) and self.matrix[y + 1][x] == 0:  # y + 1  left
                if marker:
                    counter += 1
                y += 1
                self.matrix[y][x] = counter
                a.append([y, x])
                continue
            y = a[len(a) - 1][0]
            x = a[len(a) - 1][1]
            counter = self.matrix[y][x]
            a.pop()
        return False

    def found(self, finPoint):  # ------------ Маршрут к Фрукту(работает медленно)
        pozIn = [self.body_snake[0][0], self.body_snake[0][1]]
        self.matrix[pozIn[0]][pozIn[1]] = 1
        weight = 1
        for i in range(len(self.matrix) * len(self.matrix[0])):
            weight += 1
            for y in range(len(self.matrix)):
                for x in range(len(self.matrix[y])):
                    if self.matrix[y][x] == (weight - 1):
                        if y > 0 and self.matrix[y - 1][x] == 0:
                            self.matrix[y - 1][x] = weight
                        if y < (len(self.matrix) - 1) and self.matrix[y + 1][x] == 0:
                            self.matrix[y + 1][x] = weight
                        if x > 0 and self.matrix[y][x - 1] == 0:
                            self.matrix[y][x - 1] = weight
                        if x < (len(self.matrix[y]) - 1) and self.matrix[y][x + 1] == 0:
                            self.matrix[y][x + 1] = weight

                        if (abs(y - finPoint[0]) + abs(x - finPoint[1])) == 1:
                            self.matrix[finPoint[0]][finPoint[1]] = weight
                            return True
        return False

    def printPath(self, finPoint):  # -------------------- Словами Напрвление
        y = finPoint[0]
        x = finPoint[1]
        weight = self.matrix[y][x]
        result = list(range(weight))
        while (weight):
            weight -= 1
            if y > 0 and self.matrix[y - 1][x] == weight:
                y -= 1
                result[weight] = 'RIGHT'
            elif y < (len(self.matrix) - 1) and self.matrix[y + 1][x] == weight:
                result[weight] = 'LEFT'
                y += 1
            elif x > 0 and self.matrix[y][x - 1] == weight:
                result[weight] = 'DOWN'
                x -= 1
            elif x < (len(self.matrix[y]) - 1) and self.matrix[y][x + 1] == weight:
                result[weight] = 'UP'
                x += 1
        return result[1:]

    def matrix_ground(self):  # -----------------------------------Матрица: 0-проход -1-змейка
        self.matrix = [[0 for i in range(self.M)] for c in range(self.N)]
        for i in self.body_snake:
            self.matrix[i[0]][i[1]] = - 1
        return self.matrix

    def enter_snake(self):  # ------------------------------------Выресовка матрицы в консоле
        suka = [[str(self.matrix[x][y]) + ' ' if len(str(self.matrix[x][y])) == 3 else str(self.matrix[x][y]) + (
                4 - len(str(self.matrix[x][y]))) * ' ' for x in range(len(self.matrix))] for y in
                range(len(self.matrix[0]))]
        print()
        for i in suka:
            print(''.join(i))

    def bool_snake(self):  # ------------------------------------- Если есть выход к фрукту
        self.matrix_ground()
        # start_time = time.time()

        # print(time.time() - start_time)
        if self.dinamic(1, True):
            # print(time.time() - start_time)
            return True
        # print(time.time() - start_time)
        return False

    def can_pass(self):  # --------Обработка если есть выход или нету и коректеровка маршрута при любом расскладе
        k = 0
        corect_path = []
        # self.matrix_ground()
        if not self.bool_snake():
            print('i have not quit')
            # --------------------------------CORRECT-----------------------
            for i in self.matrix:
                for c in i:
                    if c > k:
                        corect_path = [self.matrix.index(i), i.index(c)]
                        k = c
            result = self.printPath(corect_path)
            self.s_found = False
            return result
        self.s_found = True
        self.matrix_ground()
        start_time = time.time()
        # self.enter_snake()
        self.found(self.fruit)
        # self.enter_snake()
        # print(time.time()-start_time)
        result = self.printPath(self.fruit)
        return result

    def rnd(self):  # --------------------------Случайно выбрасывает Фрукт Только не на тело Змейки
        self.fruit = [randint(0, self.N - 1), randint(0, self.M - 1)]
        while 1 <= self.body_snake.count(self.fruit):
            self.fruit = [randint(0, self.N - 1), randint(0, self.M - 1)]
        return self.fruit

    def crash(self):  # ------------------------------ Если голова змейки наткнулась на свое тело
        if self.body_snake.count([self.body_snake[0][0], self.body_snake[0][1]]) > 1:
            return False
        return True

    def main(self):
        start_time = time.time() + self.speed
        pygame.init()
        screen = pygame.display.set_mode([self.size * self.N, self.size * self.M])
        clock = pygame.time.Clock()
        my_image = pygame.image.frombuffer(soursebmp.white_bmp, (16, 16), 'RGB')  # ----Загрузка картинок
        my_snake = pygame.image.frombuffer(soursebmp.green_bmp, (16, 16), 'RGB')
        my_fruit = pygame.image.frombuffer(soursebmp.red_bmp, (16, 16), 'RGB')
        for x in range(self.N):  # -----------------------Рисование белых квадратиков
            for y in range(self.M):
                screen.blit(my_image, (x * self.size, y * self.size))
        running = True  # ----------------------------------Переменная для зацикление змейки-
        while running:
            if not self.crash():  # ------------------------Если змейка ударилась в свое тело То все заново
                for x in range(self.N):
                    for y in range(self.M):
                        screen.blit(my_image, (x * self.size, y * self.size))
                self.rnd()
                self.body_snake = [[15, 9], [15, 10], [15, 11], [15, 12]]
                # clock.tick(0.3)
                self.going = 'UP'
                self.speed = 0.3
            # clock.tick(self.speed)  # ------------------------------------------Задержка
            for event in pygame.event.get():  # ------------------------------------------События нажатия клавиш
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F1:  # --------------------------Включение Атопилота)
                        self.path_snake = self.can_pass()  # -------  Постройка маршрута
                        self.head_snake = True  # ------- Отвечает за изминение позиции головы
                        self.auto = not self.auto  # ---------  Переключение авто или  ручное
                    if event.key == pygame.K_PAGEUP:  # -----------------------Увиличение скорости
                        self.speed -= .05
                    if event.key == pygame.K_PAGEDOWN:  # -------------------------Уменьшение скорости
                        self.speed += .05
                    if event.key == pygame.K_RETURN:  # ----------------------Если нажат Энтер ТО вывод Консольной инфы
                        self.matrix_ground()
                        self.dinamic(888, False)
                        print(self.path_snake)
                        self.enter_snake()
                        print(self.body_snake[0])
                    if event.key == pygame.K_ESCAPE:  # ---------------------Выход если нажата кнопка Эскейп
                        running = False
                    if event.key == pygame.K_UP:
                        if self.going != 'DOWN':  # ---------------------------Это чтобы когда вверх нельзя было в низ
                            self.going = 'UP'
                    if event.key == pygame.K_DOWN:
                        if self.going != 'UP':
                            self.going = 'DOWN'
                    if event.key == pygame.K_LEFT:
                        if self.going != 'RIGHT':
                            self.going = 'LEFT'
                    if event.key == pygame.K_RIGHT:
                        if self.going != 'LEFT':
                            self.going = 'RIGHT'
            if start_time > time.time():
                continue

            if self.auto:  # ------------------------------------------- AUTO pilot ----------------
                if self.head_snake:
                    # print(self.speed)
                    if not self.s_found:  # -Если был не найдет путь то каждое перемищение проверять на Находжение пути
                        if self.bool_snake():  # --------------------Путь найден
                            self.path_snake = self.can_pass()  # ------------Новый маршрут
                    if len(self.path_snake) > 0:  # --------Если маршрут не пустой
                        self.going = self.path_snake[0]  # -----Занести с маршрута в направление
                        self.head_snake = False  # ----Это для того что бы не проверять каждый раз А только когда
                        self.path_snake.pop(0)  # -----------сменилось направление и удалить его

            if self.going == 'DOWN':  # --------------Это события направления
                self.body_snake.insert(0, [self.body_snake[0][0], self.body_snake[0][1] + 1])  # Вставление новой головы
                if self.body_snake[0][1] == self.M:  # ----------Если выход за предел То с другой стороны
                    self.body_snake[0][1] = 0
                if self.fruit == self.body_snake[0]:  # ---------Когда Съел фрукт
                    self.rnd()  # ------------------------------------------Новый Фрукт
                    self.speed -= .0025  # ------------------------------------------Увиличение скорости
                    self.path_snake = self.can_pass()  # ----------------Загрузка нвоого маршрута к Фркту
                else:
                    last_chip = self.body_snake.pop()  # -----------удаление последнего квадратика змейки
                self.head_snake = True  # --------Сообщение ----- то что ---------Сменилось направление змейка
            if self.going == 'UP':
                self.body_snake.insert(0, [self.body_snake[0][0], self.body_snake[0][1] - 1])
                if self.body_snake[0][1] == -1:
                    self.body_snake[0][1] = self.M - 1
                if self.fruit == self.body_snake[0]:
                    self.rnd()
                    self.speed -= .0025
                    self.path_snake = self.can_pass()
                else:
                    last_chip = self.body_snake.pop()
                self.head_snake = True
            if self.going == 'RIGHT':
                self.body_snake.insert(0, [self.body_snake[0][0] + 1, self.body_snake[0][1]])
                if self.body_snake[0][0] == self.N:
                    self.body_snake[0][0] = 0
                if self.fruit == self.body_snake[0]:
                    self.rnd()
                    self.speed -= .0025
                    self.path_snake = self.can_pass()
                else:
                    last_chip = self.body_snake.pop()
                self.head_snake = True

            if self.going == 'LEFT':
                self.body_snake.insert(0, [self.body_snake[0][0] - 1, self.body_snake[0][1]])
                if self.body_snake[0][0] == -1:
                    self.body_snake[0][0] = self.N - 1
                if self.fruit == self.body_snake[0]:
                    self.rnd()
                    self.speed -= .0025
                    self.path_snake = self.can_pass()
                else:
                    last_chip = self.body_snake.pop()
                self.head_snake = True
            start_time = time.time() + self.speed
            if self.speed < 0.005:
                self.speed = 0.009
            # -------------------------- DRAW ----------------------------
            screen.blit(my_image, (last_chip[0] * self.size, last_chip[1] * self.size))  # ---Квадратик которого уже нет

            for x in self.body_snake:
                screen.blit(my_snake, (x[0] * self.size, x[1] * self.size))  # ----Рисование тела змейки

            screen.blit(my_fruit, (self.fruit[0] * self.size, self.fruit[1] * self.size))  # ----Фрук(красный квадратик)
            pygame.display.flip()  # ------------------------------------Вывод на экран
            pygame.display.set_caption(str(len(self.body_snake) - 4))  # -------Рисование счета)
        pygame.quit()


if __name__ == '__main__':
    game = Snake()
    game.main()
