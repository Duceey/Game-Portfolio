"""
Land of Ushoo
By Oskar Duce
"""
import pygame
import classes
import constants
pygame.init()
# Story: memory forgotten... story becomes released throughout game

class Game:
    def __init__(self):
        self._screenwidth = constants.SCREEN_WIDTH
        self._screenheight = constants.SCREEN_HEIGHT
        self._win = pygame.display.set_mode((self._screenwidth, self._screenheight))
        pygame.display.set_caption("Land of Ushoo")
        self._run = True
        self._player = classes.Player()
        self._bg = pygame.image.load('pics/bg.png')
        
    def main(self):
        while self._run:
            pygame.time.delay(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._run = False

            # Movement
            self._keys = pygame.key.get_pressed()

            if self._keys[pygame.K_a] and not self._keys[pygame.K_d] and self._player._x > self._player._border:
                self._player.move_left()
                
            elif self._keys[pygame.K_d] and not self._keys[pygame.K_a] and self._player._x < self._screenwidth-self._player._border-self._player._width:
                self._player.move_right()

            else:
                self._player._left = False
                self._player._right = False
                self._player._idle = True
                self._player.resetwalk()

            if self._keys[pygame.K_SPACE] and not self._player._y < self._screenheight - self._player._border - self._player._height:
                self._player.resetjump()
                self._player.set_jump(True)
                
            if self._player._injump is True:
                self._player._y -= self._player._jumpvel

            # Gravity
            if self._player._y < self._screenheight - self._player._border - self._player._height:
                self._player.gravity()
            else:
                self._player.set_gravity(0)
                
            if self._player._y > self._screenheight - self._player._border - self._player._height:
                self._player._y = self._screenheight - self._player._border - self._player._height
                self._player.set_jump(False)


            self.draw()
            
        pygame.quit()

    def draw(self):
        self._win.blit(self._bg, (0,0))
        if self._player._walkcount + 1 >= 24:
            self._player.resetwalk()

        if self._player._jumpcount + 1 >= 16:
            self._player.resetjump()

        if self._player._idlecount + 1 >= 16:
            self._player.resetidle()

        if self._player._injump and self._player._right:
            self._win.blit(self._player._jump[self._player._jumpcount//4], (self._player._x, self._player._y))
            self._player.jumpstep()
        elif self._player._injump and self._player._left:
            self._win.blit(pygame.transform.flip(self._player._jump[self._player._jumpcount//4], True, False), (self._player._x, self._player._y))
            self._player.jumpstep()
        elif self._player._right:
            self._win.blit(self._player._walk[self._player._walkcount//4], (self._player._x, self._player._y))
            self._player.walkstep()
        elif self._player._left:
            self._win.blit(pygame.transform.flip(self._player._walk[self._player._walkcount//4], True, False), (self._player._x, self._player._y))
            self._player.walkstep()
        else:
            self._win.blit(self._player._stand[self._player._idlecount//4], (self._player._x, self._player._y))
            self._player.idlestep()
            
            
        pygame.display.update()
     
def main():
    Game().main()

if __name__ == "__main__":
    main()
