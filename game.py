# -.- coding: utf8 -.-
import pygame
pygame.init()
size = [800, 600]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

my_image = pygame.image.load("aquarium.png").convert_alpha()
my_image1 = pygame.image.load("fish1.png").convert_alpha()
my_image1 = pygame.transform.scale(my_image1, (150, 80))

# уменьшил до размера (100, 100)
scaled_image = pygame.transform.scale(my_image, (500, 300))

angle = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pass
                # пишем свой код
    # обновляем значения
    angle += 1
    # рисуем
    screen.fill((200, 100, 250))
    # screen.blit(my_image, (0,0))
    screen.blit(scaled_image, (200, 200))

    # исходное изображение поворачивается на значение переменной angle
    # и записывается в перменную rotated_image
    rotated_image = pygame.transform.rotate(my_image1, angle)
    screen.blit(rotated_image, (340, 310+100))
    rotated_image = pygame.transform.rotate(my_image1, angle+100)

    screen.blit(rotated_image, (330, 302))
    rotated_image = pygame.transform.rotate(my_image1, angle+50)

    screen.blit(rotated_image, (320+100, 320))
    rotated_image = pygame.transform.rotate(my_image1, angle+180)

    screen.blit(rotated_image, (310, 340-20))
    rotated_image = pygame.transform.rotate(my_image1, angle+35)

    screen.blit(rotated_image, (300, 315+100))

    pygame.display.flip()
    clock.tick(100)
pygame.quit()