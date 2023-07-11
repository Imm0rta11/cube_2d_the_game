import pygame
pygame.init()
fonts_title = pygame.font.Font('Fonts/Anton-Regular.ttf', 50)
fonts_game_small = pygame.font.Font('Fonts/Geo-Regular.ttf', 15)
fonts_game = pygame.font.Font('Fonts/Geo-Regular.ttf', 25)
fonts_game_normal = pygame.font.Font('Fonts/Geo-Regular.ttf', 30)
fonts_game_huge = pygame.font.Font('Fonts/Geo-Regular.ttf', 50)
# Main menu
game_title = fonts_title.render('Cube 2D!', False, (255, 255, 255))
game_select_in_menu_play = fonts_game.render('Press Y for play', False, (255, 255, 255))
game_select_in_menu_settings = fonts_game.render('Press G to go settings', False, (255, 255, 255))
game_select_in_menu_record = fonts_game.render('Press R to go records', False, (255, 255, 255))
game_select_in_menu_shop = fonts_game.render('Press S to go shop', False, (255, 255, 255))
game_select_in_menu_exit_game = fonts_game.render('Press ESC for quit with game', False, (255, 255, 255))
# Settings
settings_title = fonts_title.render('Settings', False, (255, 255, 255))
settings_text_how_control = fonts_game.render('Press H to go how control panel?', False, (255, 255, 255))
settings_text_up_volume = fonts_game.render('Press up for up volume', False, (255, 255, 255))
settings_text_down_volume = fonts_game.render('Press down for down volume', False, (255, 255, 255))
# How control? menu
settings_how_control_title = fonts_title.render('How control?', False, (255, 255, 255))
settings_how_control_up = fonts_game_huge.render('Up - W', False, (255, 255, 255))
settings_how_control_down = fonts_game_huge.render('Down - S', False, (255, 255, 255))
settings_how_control_left = fonts_game_huge.render('Left - A', False, (255, 255, 255))
settings_how_control_right = fonts_game_huge.render('Right - D', False, (255, 255, 255))
settings_how_control_pause = fonts_game_huge.render('Pause - P', False, (255, 255, 255))
# Records
records_title = fonts_title.render('Records', False, (255, 255, 255))
records_text_your_record_is = fonts_game_normal.render('Your record is:', False, (255, 255, 255))
# Shop
store_title = fonts_title.render('Store', False, (255, 255, 255))
shop_text = fonts_game.render('Press 2-6 + o for buy', False, (255, 255, 255))
shop_text_2 = fonts_game.render('Press 1-6 + e for equip', False, (255, 255, 255))
shop_text_you_not_money = fonts_game.render("You don't have enough in game currency", False, (255, 255, 255))
shop_text_price_owned = fonts_game.render('Owned', False, (255, 255, 255))
# Pause
pause = fonts_game_huge.render('PAUSE', False, (255, 255, 255))
pause_text = fonts_game_normal.render('Press C for unpause', False, (255, 255, 255))
pause_text_1 = fonts_game_normal.render('Press B to go menu', False, (255, 255, 255))
# GameOver
gameover_title = fonts_title.render('GAMEOVER!', False, (255, 255, 255))
gameover_text_1 = fonts_game_normal.render('Press R for retry', False, (255, 255, 255))
gameover_text_2 = fonts_game_normal.render('Press B to go menu', False, (255, 255, 255))
# Back
back = fonts_game.render('Press B to go back', False, (255, 255, 255))
# Credits
credits_ = fonts_game_small.render('BY IMMORTALL', False, (255, 255, 255))
