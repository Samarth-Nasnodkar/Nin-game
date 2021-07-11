import pygame
from threading import Event, Thread


class Button:
    def __init__(self, left, top, width, height, surface: pygame.Surface = None):
        self.__coords = (left, top)
        self.__dims = (width, height)
        self.rect = pygame.Rect(left, top, width, height)
        self.__clicked = Event()
        self.surface = surface

    def on_click(self, func):
        mt = Thread(target=self.__click_event_loop)
        mt.start()

        def wrapper():
            while True:
                self.__clicked.wait()
                func()
                print("Func exec\n")
                self.__clicked.clear()

        t = Thread(target=wrapper)
        t.start()

    def __click_event_loop(self):
        while True:
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rect.collidepoint(x, y):
                        self.__clicked.set()
                        print("Clicked.\n")

    def render(self, surface: pygame.surface):
        surface.blit(self.surface, self.__coords)
