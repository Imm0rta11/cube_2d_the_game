import pygame
from textures import *
from text import *

pygame.init()
win = pygame.display.set_mode((800, 600))


def draw_main_menu():
    win.blit(background_menu, (0, 0))
    win.blit(game_title, (320, 125))
    win.blit(credits_, (405, 190))
    win.blit(game_select_in_menu_play, (325, 250))
    win.blit(game_select_in_menu_settings, (290, 300))
    win.blit(game_select_in_menu_record, (295, 350))
    win.blit(game_select_in_menu_shop, (310, 400))
    win.blit(game_select_in_menu_exit_game, (260, 450))


def draw_settings():
    win.blit(background_menu, (0, 0))
    win.blit(settings_title, (320, 125))
    win.blit(settings_text_how_control, (260, 250))
    win.blit(settings_text_up_volume, (300, 300))
    win.blit(settings_text_down_volume, (275, 350))
    win.blit(back, (315, 450))


def draw_how_control():
    win.blit(background_menu, (0, 0))
    win.blit(settings_how_control_title, (270, 125))
    win.blit(settings_how_control_up, (320, 200))
    win.blit(settings_how_control_down, (320, 250))
    win.blit(settings_how_control_left, (320, 300))
    win.blit(settings_how_control_right, (320, 350))
    win.blit(settings_how_control_pause, (320, 400))
    win.blit(back, (310, 480))


def draw_records():
    win.blit(background_menu, (0, 0))
    win.blit(records_title, (320, 125))
    win.blit(records_text_your_record_is, (315, 250))
    win.blit(back, (310, 350))


def draw_shop():
    win.blit(background_menu, (0, 0))
    win.blit(background_shop_slot, (100, 160))
    win.blit(background_shop_slot, (318, 160))
    win.blit(background_shop_slot, (536, 160))
    win.blit(background_shop_slot, (100, 315))
    win.blit(background_shop_slot, (318, 315))
    win.blit(background_shop_slot, (536, 315))
    win.blit(blue_player_idle, (140, 192))
    win.blit(green_player_idle, (357, 192))
    win.blit(cyan_player_idle, (574, 192))
    win.blit(yellow_player_idle, (140, 347))
    win.blit(red_player_idle, (357, 347))
    win.blit(purple_player_idle, (576, 347))
    win.blit(shop_text_price_owned, (132, 245))
    win.blit(store_title, (330, 75))
    win.blit(shop_text, (270, 475))
    win.blit(shop_text_2, (270, 500))
    win.blit(back, (300, 550))


def draw_game():
    win.blit(background_in_game, (0, 0))
    win.blit(line_bar, (0, 550))


def draw_game_over_screen():
    win.blit(background_menu, (0, 0))
    win.blit(gameover_title, (285, 178))
    win.blit(gameover_text_1, (285, 285))
    win.blit(gameover_text_2, (285, 325))


def draw_pause():
    win.blit(pause, (350, 180))
    win.blit(pause_text, (300, 235))
    win.blit(pause_text_1, (300, 270))
