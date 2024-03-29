import game_functions as gf
from settings import Settings
from alien import Alien
from ship import Ship
import pygame
import sys
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets, aliens, ai_settings, screen, ship)
        gf.update_aliens(ai_settings, aliens, ship)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)

run_game()
