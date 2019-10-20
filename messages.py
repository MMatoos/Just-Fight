import pygame as pg
import time

white = (255, 255, 255)
black = (0, 0, 0)
rect = pg.Rect(750, 525, 1000, 10000)
rect1 = pg.Rect(550, 525, 200, 240)


def message_display(win, x, y, w, h, text, size):
    large_text = pg.font.Font('fonts/font.ttf', size)
    text_surface, text_rectangle = text_objects(text, large_text)
    text_rectangle.center = (x+(w/2), y+(h/2)-15)
    win.blit(text_surface, text_rectangle)
    pg.display.flip()


def smessage_display(win, x, y, text, size):
    small_text = pg.font.Font("fonts/font.ttf", size)
    text_surface, text_rectangle = text_objects(text, small_text)
    text_rectangle = (x, y)
    win.blit(text_surface, text_rectangle)
    pg.display.flip()


def message_clear(win):
    pg.draw.rect(win, 0, rect)


def hp_clear(win):
    pg.draw.rect(win, 0, rect1)


def down_clear(win):
    pg.draw.rect(win, 0, (0, 510, 1280, 210))


def text_objects(text, font):
    text_surface = font.render(text, True, white)
    return text_surface, text_surface.get_rect()

