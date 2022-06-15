import pygame
from random import randrange

# основные настройки
# размеры игрового поля
RES = 800
SIZE = 50
# границы координат x и y
x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
# границы появления яблок
apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
# длина змейки по умолчанию
length = 1
# отрисовка змейки
snake = [(x, y)]
# смещение координат от изначального положения змейки (по умолчанию)
dx, dy = 0, 0
# частота смены кадров
fps = 60
# Словарь клавиш управления змейкой
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
# игровые очки
score = 0
# скорость змейки и её изменение
speed_count, snake_speed = 0, 10
# инициализация pygame
pygame.init()
# отображение основного окна игры
surface = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
# параметры шрифта для игровых очков
font_score = pygame.font.SysFont('Arial', 26, bold=True)
# параметры шрифта для сообщения о конце игры
font_end = pygame.font.SysFont('Arial', 66, bold=True)
# фоновое изображение
img = pygame.image.load('img/snake_background.jpg').convert()


# закрытие игры
def close_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()