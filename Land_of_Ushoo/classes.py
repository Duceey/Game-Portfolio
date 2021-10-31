"""
List of classes for Land of Ushoo
"""
import pygame
import constants
pygame.init()

class Player:
    def __init__(self):
        self._x = 50
        self._y = 646
        self._width = 64
        self._height = 64
        self._vel = 18
        self._name = 'Inchu'
        self._border = 40
        self._jumpvel = 40
        self._injump = False
        self._gravity = 0
        self._left = False
        self._right = False
        self._idle = True
        self._walkcount = 0
        self._idlecount = 0
        self._jumpcount = 0
        self._walk = [pygame.image.load('pics/R1.png'), pygame.image.load('pics/R2.png'), pygame.image.load('pics/R3.png'), pygame.image.load('pics/R4.png'), pygame.image.load('pics/R5.png'), pygame.image.load('pics/R6.png')]
        self._stand = [pygame.image.load('pics/I1.png'), pygame.image.load('pics/I2.png'), pygame.image.load('pics/I3.png'), pygame.image.load('pics/I4.png')]
        self._jump = [pygame.image.load('pics/J1.png'), pygame.image.load('pics/J2.png'), pygame.image.load('pics/J3.png'), pygame.image.load('pics/J4.png')]
        
    def move_left(self):
        self._left = True
        self._right = False
        self._x -= self._vel
        
    def move_right(self):
        self._left = False
        self._right = True
        self._x += self._vel

    def set_jump(self, jumpstate):
        self._injump = jumpstate

    def set_gravity(self, value):
        self._gravity = value

    def gravity(self):
        self._gravity += 4
        self._y += self._gravity

    def resetwalk(self):
        self._walkcount = 0

    def walkstep(self):
        self._walkcount += 1

    def resetjump(self):
        self._jumpcount = 0

    def jumpstep(self):
        self._jumpcount += 1

    def resetidle(self):
        self._idlecount = 0

    def idlestep(self):
        self._idlecount += 1
    
    def draw(self, window):
        pass

    def get_name(self):
        return self._name

# Enemy Classes
class Enemy:
    def __init__(self):
        pass

class Slaughter(Enemy):
    def __init__(self, x, y, width, height):
        self._x = 0
        self._y = 0
        self._width = 0
        self._height = 0
        self._vel = 0

class Petrify(Enemy):
    def __init__(self, x, y, width, height):
        self._x = 0
        self._y = 0
        self._width = 0
        self._height = 0
        self._vel = 0

class Blitz(Enemy):
    def __init__(self):
        self._x = 0
        self._y = 0
        self._width = 0
        self._height = 0
        self._vel = 0

# Weapon Classes
class Weapon:
    def __init__(self):
        pass

class Sword(Weapon):
    def __init__(self):
        pass

class Bow(Weapon):
    def __init__(self):
        pass
    
# Upgrade Classes
class Upgrade:
    # DoubleJump, Dash, Barrier
    def __init__(self):
        pass

class DoubleJump(Upgrade):
    def __init__(self):
        pass

class Dash(Upgrade):
    def __init__(self):
        pass

class Barrier(Upgrade):
    def __init__(self):
        pass

class WallJump(Upgrade):
    def __init__(self):
        pass

class Platform:
    def __init__(self, x, y, width, height, colour):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._colour = colour
