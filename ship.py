# !/usr/local/python
# coding: utf-8

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, screen, setting):

        super(Ship, self).__init__()
        self.screen = screen
        self.setting = setting
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def center_ship(self):
        self.center = self.screen_rect.centerx
