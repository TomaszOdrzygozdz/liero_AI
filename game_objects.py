import random
from collections import namedtuple, defaultdict

from GAME_SETTINGS import WORM_HEIGHT, WORM_WIDTH

Vector = namedtuple("Vector", "x y")
keys_direction_map = {'a': [-1,0], 'd': [1,0], 'w': [0,-1], 's': [0,1]}


class GameObject:
    def __init__(self, **kwargs):
        for arg, value in kwargs.items():
            self.__dict__[arg] = value

class Worm(GameObject):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #TODO(Tomek): automatically read canvas geometry
        self.pressed_keys = defaultdict(bool)
        self.random_position(0,0,900,900)

    def random_position(self, min_x, min_y, max_x, max_y):
        self.x = random.uniform(min_x, max_x)
        self.y = random.uniform(min_y, max_y)

    def draw_worm(self, canvas):
        canvas.create_oval(self.x, self.y, self.x + WORM_HEIGHT, self.y + WORM_WIDTH, fill=self.color)

    def move_worm(self):
        final_direction = [0,0]
        for key, value in keys_direction_map.items():
            if self.pressed_keys[key]:
                for i in range(2):
                    final_direction[i] += value[i]

        self.x += final_direction[0]
        self.y += final_direction[1]


class State:
    def __init__(self):
        self.worms = [Worm(color="red"), Worm(color="green")]

    def draw_state(self, canvas):
        for worm in self.worms:
            worm.draw_worm(canvas)

    def move_worm(self):
        for worm in self.worms:
            worm.move_worm()