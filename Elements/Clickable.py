import pygame
from threading import Event, Thread


class Clickable:
    def __init__(self, left, top, width, height, surface: pygame.Surface = None, tag=None):
        """
        left -> The X coordinate of the top left vertex
        top -> The Y coordinate of the top left vertex
        width -> The horizontal length of the clickble
        height -> The vertical length of the clickble
        surface -> The surface correspondong to the clickble, maybe an Image
        tag -> A string to identify the clickble
        """
        self.__coords = (left, top) # The coordinated of the top left vertex of the rect
        self.__dims = (width, height) # The dimensions of the rect
        self.rect = pygame.Rect(left, top, width, height) # The rect
        self.__clicked = Event() # The event which will control on_click
        self.__hovered = Event() # The event which will control on_hover
        self.surface = surface # The surface of the button
        self.tag = tag # A tag to identify a button

    def on_click(self, func):
        """
        This function is called when this clickble is pressed.
        It can be used as a decorator or as a function.
        Decorator example:
            @clickble.on_click
            def _click():
                print(clickable.tag + " clicked.")
        """
        mt = Thread(target=self.__click_event_loop)
        mt.start()

        def wrapper():
            while True:
                self.__clicked.wait()
                func()
                self.__clicked.clear()

        t = Thread(target=wrapper)
        t.start()

    def on_hover(self, func):
        """
        This function is called when the cursor hovers over this clickable.
        It can be used as a decorator or as a function.
        Decorator example:
            @clickable.on_hover
            def _hover():
                print(clickable.tag + " hovered.")
        """
        mt = Thread(target=self.__hover_event_loop)
        mt.start()

        def wrapper():
            while True:
                self.__hovered.wait()
                func()
                self.__hovered.clear()

        t = Thread(target=wrapper)
        t.start()

    def __click_event_loop(self):
        """
        The loop to check for clicks on the clickable.
        If clicked, it triggers the self.__clicked event.
        """
        while True:
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rect.collidepoint(x, y):
                        self.__clicked.set()

    def __hover_event_loop(self):
        """
        The loop to check for cursor hoverings over the clickable.
        If hovered upon, it triggers the self.__hovered event.
        """
        while True:
            x, y = pygame.mouse.get_pos()
            if self.rect.collidepoint(x, y):
                self.__hovered.set()

    def render(self, screen: pygame.surface):
        """
        displays the surface on the screen.
        """
        screen.blit(self.surface, self.__coords)
