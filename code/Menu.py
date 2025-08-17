
import pygame.image
from pygame import Rect, Surface
from pygame.font import Font
from code.const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW
# -*- coding: utf-8 -*-


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./assets/MenuBg.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load("./assets/Menu.mp3")
        pygame.mixer_music.play(-1)  # Play the music in a loop
        selected = 0  # índice da opção selecionada (adicione antes do while True)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(
                text_size=50,
                text="MONTANHA",
                text_color=COLOR_ORANGE,
                text_center_pos=(WIN_WIDTH / 2, 100),)
            self.menu_text(
                text_size=50,
                text="DO TIRO",
                text_color=COLOR_ORANGE,
                text_center_pos=(WIN_WIDTH / 2, 140),)
            
            for i in range(len(MENU_OPTION)):
                if i == selected:
                    self.menu_text(
                text_size=20,
                text=MENU_OPTION[i],
                text_color=COLOR_YELLOW,
                text_center_pos=(WIN_WIDTH / 2, 180 + 25 * i),)
                else:
                    self.menu_text(
                    text_size=20,
                    text=MENU_OPTION[i],
                    text_color=COLOR_WHITE,
                    text_center_pos=(WIN_WIDTH / 2, 180 + 25 * i),)
            
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()  # End pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # Move down in the menu
                        if selected < len(MENU_OPTION) - 1:
                            selected += 1
                        else:
                            selected = 0
                    if event.key == pygame.K_UP: # Move up in the menu
                        if selected > 0:
                            selected -= 1
                        else:
                            selected = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # Select the option
                        return selected  # Return the selected option
            pygame.display.flip()


    def menu_text(
        self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
