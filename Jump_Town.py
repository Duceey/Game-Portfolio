"""
Jump Town
By Oskar Duce
"""
import pygame
import random
pygame.init()

# ~~~~~~~~~ Constants ~~~~~~~~~
PLAYER_X = 175
PLAYER_Y = 700
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_VEL = 10
PLAYER_JUMP_VEL = 23
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800
BORDER = 10

# ~~~~~~~~~ Classes ~~~~~~~~~

class Player:
    def __init__(self):
        self._x = PLAYER_X
        self._y = PLAYER_Y
        self._width = PLAYER_WIDTH
        self._height = PLAYER_HEIGHT
        self._vel = PLAYER_VEL
        self._jumpstate = False
        self._jumpvel = PLAYER_JUMP_VEL
        self._gravity = 0
        
    def move_left(self):
        self._x -= self._vel
    
    def move_right(self):
        self._x += self._vel

    def jump(self):
        self._jumpstate = True

    def gravity(self):
        if self._gravity < 40:
            self._gravity += 1
        self._y += self._gravity

    def reset_gravity(self):
        self._gravity = 0

    def move_player(self, vel):
        self._y += vel

class Platform:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def move_platform(self, vel):
        self._y += vel

# ~~~~~~~~~ Core Game ~~~~~~~~~
class Game:
    def __init__(self):
        self._win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Jump Town")
        self._run = True
        self._player = Player()
        self._platform_list = [Platform(0, 750, SCREEN_WIDTH, 20), Platform(0, 600, 100, 20), Platform(250, 450, 100, 20), Platform(250, 300, 100, 20), Platform(250, 150, 100, 20)]
        self._border = BORDER
        
    def play(self):
        while self._run:
            pygame.time.delay(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._run = False

            self._keys = pygame.key.get_pressed()

            if self._keys[pygame.K_a] and not self._keys[pygame.K_d] and self._player._x > self._border:
                self._player.move_left()
                
            elif self._keys[pygame.K_d] and not self._keys[pygame.K_a] and self._player._x < SCREEN_WIDTH-self._border-self._player._width:
                self._player.move_right()
                
            if self._keys[pygame.K_SPACE]:
                self._player.jump()

            if self._player._jumpstate:
                self._player._y -= self._player._jumpvel
                self._player.gravity()

            if self._player._gravity > self._player._jumpvel:
                for i in self._platform_list:
                    if self._player._y + self._player._height < i._y + i._height and self._player._x + self._player._width > i._x and i._x + i._width > self._player._x and self._player._y + self._player._height >= i._y:
                        self._player.reset_gravity()

            if self._player._jumpstate:
                for i in self._platform_list:
                    i.move_platform(3.5)

            if self._player._jumpstate:
                self._player.move_player(3.5)

            for i in self._platform_list:
                if i._y > SCREEN_HEIGHT:
                    self._platform_list.append(Platform(random.randrange(0,300), 0, 100, 20))
                    self._platform_list.remove(i)
            
            if self._player._y > 750:
                print('game over')
                self._run = False

                    
            self.draw()
            
        pygame.quit()
    
    def draw(self):
        self._win.fill((150, 210, 255))
        pygame.draw.rect(self._win, (50, 125, 50), (self._player._x, self._player._y, self._player._width, self._player._height))
        for i in self._platform_list: 
            pygame.draw.rect(self._win, (255, 0, 0), (i._x, i._y, i._width, i._height))
        pygame.display.update()
        

def main():
    Game().play()

if __name__ == "__main__":
    main()

