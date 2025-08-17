from code.const import WIN_HEIGHT, WIN_WIDTH
from code.Menu import Menu
from code.Level import Level
import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()  # Run the menu
            
            if menu_return in  [0 , 1, 2]:  # If the first option is selected
                level = Level(self.window, 'Level1', menu_return)
                level = level.run() # Set the level to 1
            elif menu_return == 4:  # If the second option is selected
                pygame.quit() # Close window
                quit()  # End pygame
            else:
                pass
            