from ursina import *
import random

# конструктор приложения на ursina
app = Ursina()
# настройки камеры
# ортографическая проекция камеры
camera.orthographic = True
# отдалённость
camera.fov = 40

# создание объекта "автомобиль"
car = Entity(
    model='quad',
    texture='assets/car2.png',
    collider='box',
    scale=(2, 1),
    rotation_z=-90
)
# создание объекта "дорога"
road1 = Entity(
    model='quad',
    texture='assets/roadnew.png',
    collider='box',
    scale=15,
    z=1
)
# создание второго объекта "дорога" путём дублирования
road2 = duplicate(road1, y=15)
# список частей дороги
pair = [road1, road2]

# добавление игровых противников
enemies = []

def newEnemy():
    val = random.uniform(-2, 2)
    new = duplicate(
        car,
        texture='assets/car3.png',
        x= 2 * val,
        y=25,
        color=color.random_color(),
        rotation_z=
            90 if val < 0
            else -90
    )
    # добавляем созданный "автомобиль" в список противников
    enemies.append(new)
    # отрисовываем объект на экране через временной интервал задержки
    invoke(newEnemy, delay=0.5)

newEnemy()


# основная часть игры
def update():
    # движение "автомобиля" влево и вправо по клавишам W,A,S,D
    car.x -= held_keys['a'] * 5 * time.dt
    car.x += held_keys['d'] * 5 * time.dt
    car.y -= held_keys['s'] * 5 * time.dt
    car.y += held_keys['w'] * 5 * time.dt

    # иллюзия движения дороги
    for road in pair:
        road.y -= 6 * time.dt
        if road.y < -15:
            road.y += 30
    for enemy in enemies:
        if enemy.x < 0:
            enemy.y -= 10 * time.dt
        else:
            enemy.y -= 5 * time.dt
        # если кооордината y противника станет меньше -10,
        # то противник скроется с экрана
        if enemy.y < -10:
            enemies.remove(enemy)
            destroy(enemy)

# запуск приложения
app.run()
