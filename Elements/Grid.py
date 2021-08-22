import pygame
from Button import *
from enum import Enum


class ContentFit(Enum):
    wrapContent = 0
    matchParent = 1


class Grid:
    rows: int  # The number of rows
    columns: int  # The number of columns
    width: int  # Width of the grid
    height: int  # Height of the grid
    cellDimensions: tuple  # The dimensions of each cell
    __cellCoords: list

    def __init__(
        self,
        rows: int,
        columns: int,
        position: tuple,
        fit: ContentFit,
        screenDimensions: tuple = (0, 0),
        cellWidth: int = 0,
        cellHeight: int = 0,
        paddingLeft: int = 0,
        paddingTop: int = 0,
        paddingBottom: int = 0,
        paddingRight: int = 0,
    ) -> None:
        self.rows = rows
        self.columns = columns
        self.position = position
        self.fit = fit
        self.paddingLeft = paddingLeft
        self.paddingRight = paddingRight
        self.paddingTop = paddingTop
        self.paddingBottom = paddingBottom
        if self.fit == ContentFit.matchParent:
            self.cellDimensions[0] = int(screenDimensions[0] / self.columns) - (
                self.paddingRight + self.paddingLeft
            )
            self.cellDimensions[1] = int(screenDimensions[1] / self.rows) - (
                self.paddingTop + self.paddingBottom
            )
        elif self.fit == ContentFit.wrapContent:
            self.cellDimensions = (cellWidth, cellHeight)

        self.cells = [[] * self.columns] * self.rows
        self.__cellCoords = [[] * self.columns] * self.rows
        self.__fill_cords()

    def __fill_cords(self) -> None:
        w, h = self.position
        for i in range(self.rows):
            h += self.paddingTop
            for j in range(self.columns):
                w += self.paddingLeft
                self.__cellCoords[i][j] = (w, h)
                w += self.paddingLeft + self.cellDimensions[0] + self.paddingRight
            h += self.cellDimensions[1] + self.paddingBottom + self.paddingTop
            w = self.position[0]

    def render(self, surface: pygame.Surface) -> None:
        for i in range(self.rows):
            for j in range(self.columns):
                surface.blit(
                    self.cells[i][j],
                    pygame.Rect(
                        self.__cellCoords[i],
                        self.__cellCoords[j],
                        self.cellDimensions[0],
                        self.cellDimensions[1],
                    ),
                )
