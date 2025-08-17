from abc import ABC, abstractmethod

import pygame.image



class Entity(ABC):
    def __init__(self,name: str, position: tuple,):
        self.name = name
        self.surf = pygame.image.load("./assets/{}.png".format(name))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 5  # Default speed for the entity
    
    
    @abstractmethod
    def move(self, ):
        pass
