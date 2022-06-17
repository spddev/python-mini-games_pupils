from ursina import *
# работа с 3D-объектами
from ursina.prefabs.first_person_controller import FirstPersonController

# основное окно  ursina
app = Ursina()
# текстуры игры
# небо
sky_texture = load_texture('assets/sky.png')
# трава
grass_texture = load_texture('assets/grass.png')
# земля
dirt_texture = load_texture('assets/dirt.png')
# дерево
oak_texture = load_texture('assets/oak.png')
# песок
sand_texture = load_texture('assets/sand.png')
# доски
wood_texture = load_texture('assets/wood.png')
# камень
stone_texture = load_texture('assets/stone.png')
# текстура по умолчанию
current_texture = grass_texture


# функция обновления кадра (фрейма)
def update():
    global current_texture
    # по нажатию клавиш на клавиатуре строим определённый блок
    # если на клавиатуре нажата цифра 1, то добавляем блок травы
    if held_keys['1']:
        current_texture = grass_texture
    # если на клавиатуре нажата цифра 2, то добавляем блок c землёй
    if held_keys['2']:
        current_texture = dirt_texture
    # если на клавиатуре нажата цифра 3, то добавляем блок c деревом
    if held_keys['3']:
        current_texture = oak_texture
    # если на клавиатуре нажата цифра 4, то добавляем блок c песком
    if held_keys['4']:
        current_texture = sand_texture
    # если на клавиатуре нажата цифра 5, то добавляем блок c камнем
    if held_keys['5']:
        current_texture = stone_texture
    # если на клавиатуре нажата цифра 6, то добавляем блок c досками
    if held_keys['6']:
        current_texture = wood_texture

    # запуск анимации руки по нажатию левой/правой кнопки мыши
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()


# класс для отображения неба
class Sky(Entity):
    # создание UV-сферы
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            # размер
            scale=150,
            texture=sky_texture,
            double_sided=True  # для замыкания сферы на саму себя
        )


# класс для анимации руки
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='cube',
            scale=(0.2, 0.3),
            color=color.white,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.4)
        )

    # Функции для анимации руки
    def active(self):
        self.position = Vec2(0.1, -0.5)
        self.rotation = Vec3(90, -10, 0)

    def passive(self):
        self.rotation = Vec3(150, -10, 0),
        self.position = Vec2(0.4, -0.4)

# класс для работы с 3D-объектами
class Voxel(Button):
    # инициализация класса
    # def __init__(self, position=(0, 0, 0)):
    #     super().__init__(
    #         parent=scene,
    #         position=position,
    #         model='cube',
    #         origin_y=.5,
    #         texture='white_cube',
    #         color=color.color(0, 0, 255),
    #         highlight_color=color.lime  # подсветка при наведении мыши
    #     )
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture=texture,
            color=color.color(0, 0, 255),
            highlight_color=color.lime  # подсветка при наведении мыши
        )

    # обработка реакции на клавиатуру и мышь
    def input(self, key):
        if self.hovered:
            # если нажата правая кнопка мыши
            if key == 'right mouse down':
                # установка блока там, где указывает указатель мыши
                voxel = Voxel(position=self.position + mouse.normal,
                              texture=current_texture)
            # если нажата левая кнопка мыши
            if key == 'left mouse down':
                # уничтожаем блок там, куда указывает мышь
                destroy(self)


# генерация ландшафта
# 1 способ - область 15 x 15
for z in range(15):
    for x in range(15):
        voxel = Voxel((x, 0, z))
# 2 способ - облаcть 8 x 8 x 8
# for z in range(8):
#     for x in range(8):
#         for y in range(8):
#             voxel = Voxel((x, z, y))
# отображаем игрока в качестве вида от первого лица
player = FirstPersonController()
# отображаем сферу
sky = Sky()
# отображаем руку
hand = Hand()
# запуск окна
app.run()
