from random import *
import pygame
import aq


class Akvarium:
    Poz_fish = []

    def __init__(self, H=50, W=35):
        self.screen = pygame.display.set_mode([800,600])
        self.clock = pygame.time.Clock()
        self.my_image = pygame.image.frombuffer(aq.aq_png, (1920, 1080), 'RGB')
        self.my_image1 = pygame.image.load("fish1.png").convert_alpha()
        self.my_image1 = pygame.transform.scale(self.my_image1, (H, W))
        self.scaled_image = pygame.transform.scale(self.my_image, (780, 500))

    def draw(self, X, Y):
        self.screen.blit(self.my_image1, (X, Y))

    def add_fish(self, X1, Y1):
        self.Poz_fish.append(str(X1) + ' ' + str(Y1))
        self.draw(X1, Y1)

    def random_fish(self, moder):
        mode = moder
        if (int(mode[0]) > 1) and (int(mode[0]) < 750):
            mode[0] = str(randint(int(mode[0]) - 5, int(mode[0]) + 5))
        else:
            if int(mode[0]) == 1:
                mode[0] = str(3)
            else:
                mode[0] = str(745)

        if (int(mode[1]) > 110) and (int(mode[1]) < 450):
            mode[1] = str(randint(int(mode[1]) - 1, int(mode[1]) + 1))
        else:
            if int(mode[1]) == 110:
                mode[1] = str(113)
            else:
                mode[1] = str(445)

        return mode

    def swimming_fish(self):
        running = True
        angle = 0
        n = 20
        while running:
            angle += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.my_image = pygame.image.frombuffer(aq.aq_png, (1920, 1080), 'RGB')
                        self.scaled_image = pygame.transform.scale(self.my_image, (780, 500))

                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_DOWN:
                        n -= 5
                    if event.key == pygame.K_UP:
                        n += 5
                    if event.key == pygame.K_RIGHT:

                        # frombuffer(soursebmp.red_bmp, (16, 16), 'RGB'

                        self.my_image = pygame.image.load("aquarium.png").convert_alpha()
                        self.scaled_image = pygame.transform.scale(self.my_image, (780, 500))
            self.screen.fill((200, 100, 250))

            self.screen.blit(self.scaled_image, (10, 70))
            for x in range(len(self.Poz_fish)):
                s = self.Poz_fish[x]
                s = s.split()
                s = self.random_fish(s)
                self.draw(int(s[0]), int(s[1]))
                self.Poz_fish[x] = (s[0] + ' ' + s[1])
            rotated_image = pygame.transform.rotate(self.my_image1, angle)
            self.screen.blit(rotated_image, (340, 310 + 100))

            pygame.display.flip()
            self.clock.tick(n)

pygame.init()
# size = [800, 600]

A_K = Akvarium()
B_Ak = Akvarium(1,4)

for i in range(100):
    A_K.add_fish(randint(10, 720), randint(110, 450))
A_K.swimming_fish()


# for i in range(10):
#     A_K.window.coords(A_K.var[i], 0, 0, 75, 25)
# print(A_K.var)
pygame.quit()
