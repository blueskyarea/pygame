# coding: utf-8
import pygame
from pygame.locals import *
import sys
SCREEN = Rect(0, 0, 400, 400)

def main():
    pygame.display.set_mode(SCREEN.size)

    while (1):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
