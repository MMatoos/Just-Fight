import pygame as pg
import messages as mes
import time

white = (255, 255, 255)
bubu = (155, 124, 211)
black = (0, 0, 0)

button_img = pg.image.load('images/button.png')
button_pressed_img = pg.image.load('images/button1.png')


class Button(object):
    def __init__(self, rect, text_button, use):
        self.rect = pg.Rect(rect)
        self.image = pg.Surface(self.rect.size).convert()
        self.color = bubu
        self.hover_color = (255, 0, 0)
        self.image.fill(white)
        self.function = use
        self.text_button = text_button
        self.font = pg.font.Font('fonts/font.ttf', 35)
        self.font_color = white
        self.text = self.font.render(self.text_button, True, self.font_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)
        self.timex = 0
        self.clicked = 0
        self.used = 0

    def get_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)

    def on_click(self, event):
        if self.rect.collidepoint(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]):
            self.function()

    def is_hovering(self):
        if self.rect.collidepoint(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]):
            return True

    def draw(self, surf):
        if self.is_hovering():
            surf.blit(button_pressed_img, self.rect)
        else:
            surf.blit(button_img, self.rect)
        surf.blit(self.text, self.text_rect)

#pg.draw.rect(win, (94, 88, 66), (50, 525, 200, 75))
#pg.draw.rect(win, (94, 88, 66), (50, 625, 200, 75))
#pg.draw.rect(win, (94, 88, 66), (275, 525, 200, 75))
#pg.draw.rect(win, (94, 88, 66), (275, 625, 200, 75))