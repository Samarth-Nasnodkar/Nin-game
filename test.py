from Elements.Button import *
import pygame
import pygame.display as display
import pygame.draw as draw
import pygame.event as event

running = True
pygame.init()
screen = display.set_mode((720, 720))
screen.fill((0, 0, 0))
rect = pygame.Rect(10, 10, 100, 100)
button = Button(10, 10, 100, 100, rect, "B1")
draw.rect(screen, (255, 255, 255), rect)
display.update()


@button.on_click
def ds():
    print(button.tag + " pressed")

@button.on_hover
def ds():
    print(button.tag + " hovered")

while running:
    for e in event.get():
        if e == pygame.QUIT:
            pygame.quit()
            runtime = False