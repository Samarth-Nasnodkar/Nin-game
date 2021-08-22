from Clickable import Clickable
import pygame

class Button(Clickable):
    def __init__(self, left, top, width, height, surface: pygame.Surface, tag):
        super().__init__(left, top, width, height, surface=surface, tag=tag)