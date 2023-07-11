import pygame

from imports import *

pygame.init()
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Cube 2D')

keys = pygame.key.get_pressed()

score_x = random.randint(0, 752)
score_y = random.randint(0, 500)

player_x = 375
player_y = 250
player_speed = 4
score = 0

run = True
game = False
game_over = False
settings = False
records = False
shop = False
how_control = False
pause = False
menu = True

player_up = blue_player_up
player_down = blue_player_down
player_right = blue_player_right
player_left = blue_player_left
player_idle = blue_player_idle

up = False
down = False
right = False
left = False


price_1 = '1000$'
price_2 = '1500$'
price_3 = '2000$'
price_4 = '2500$'
price_5 = '3500$'


while run:
    pygame.time.Clock().tick(60)
    keys = pygame.key.get_pressed()
    if menu and not game:
        draw_main_menu()
        if keys[pygame.K_y]:
            menu = False
            game = True
            score = 0
            time.sleep(0.3)
        if keys[pygame.K_g]:
            menu = False
            settings = True
            time.sleep(0.3)
        if keys[pygame.K_r]:
            menu = False
            records = True
            time.sleep(0.3)
        if keys[pygame.K_s]:
            menu = False
            shop = True
            time.sleep(0.3)
        if keys[pygame.K_ESCAPE]:
            file_1 = open('money.py', 'w')
            file_1.write(f'money = {money}')
            file_1.close()
            if score > score_record:
                file = open('score_record.py', 'w')
                file.write(f'score_record = {score}')
                file.close()
            file_3 = open('volume_config.py', 'w')
            file_3.write(f'volume = {volume}')
            file_3.close()
            run = False
    if settings and not menu:
        draw_settings()
        settings_text_volume = fonts_game.render(f'Volume: {round(volume)}', False, (255, 255, 255))
        win.blit(settings_text_volume, (350, 400))
        if keys[pygame.K_h]:
            settings = False
            how_control = True
            time.sleep(0.3)
        if keys[pygame.K_UP]:
            volume += 0.1
            pygame.mixer.music.set_volume(volume)
        if keys[pygame.K_DOWN]:
            volume -= 0.1
            pygame.mixer.music.set_volume(volume)
        if keys[pygame.K_b]:
            settings = False
            menu = True
            time.sleep(0.3)
    if how_control and not settings:
        draw_how_control()
        if keys[pygame.K_b]:
            how_control = False
            settings = True
            time.sleep(0.3)
    if records and not menu:
        draw_records()
        records = fonts_game.render(str(score_record) + ' score', False, (255, 255, 255))
        win.blit(records, (355, 300))
        if keys[pygame.K_b]:
            records = False
            menu = True
            time.sleep(0.3)
    if shop and not menu:
        draw_shop()
        if green_item.green:
            price_1 = 'Owned'
        if red_item.red:
            price_4 = 'Owned'
        if purple_item.purple:
            price_5 = 'Owned'
        if yellow_item.yellow:
            price_3 = 'Owned'
        if cyan_item.cyan:
            price_2 = 'Owned'
        money_display = fonts_game_normal.render(f'{money}$', False, (255, 255, 255))
        shop_text_price_1 = fonts_game.render(price_1, False, (255, 255, 255))
        shop_text_price_2 = fonts_game.render(price_2, False, (255, 255, 255))
        shop_text_price_3 = fonts_game.render(price_3, False, (255, 255, 255))
        shop_text_price_4 = fonts_game.render(price_4, False, (255, 255, 255))
        shop_text_price_5 = fonts_game.render(price_5, False, (255, 255, 255))
        win.blit(shop_text_price_1, (350, 245))
        win.blit(shop_text_price_2, (568, 245))
        win.blit(shop_text_price_3, (133, 398))
        win.blit(shop_text_price_4, (350, 398))
        win.blit(shop_text_price_5, (568, 398))
        win.blit(money_display, (600, 100))
        if keys[pygame.K_1]:
            if keys[pygame.K_e]:
                player_up = blue_player_up
                player_down = blue_player_down
                player_right = blue_player_right
                player_left = blue_player_left
                player_idle = blue_player_idle
        if keys[pygame.K_2]:
            if keys[pygame.K_o]:
                if money >= 1000 and not green_item.green:
                    money -= 1000
                    green_item.green = True
                    file_2 = open('purchased_items/green_item.py', 'w')
                    file_2.write('green = True')
                    file_2.close()
            if keys[pygame.K_e]:
                if green_item.green:
                    player_up = green_player_up
                    player_down = green_player_down
                    player_right = green_player_right
                    player_left = green_player_left
                    player_idle = green_player_idle
        if keys[pygame.K_3]:
            if keys[pygame.K_o]:
                if money >= 1000 and not cyan_item.cyan:
                    money -= 1000
                    cyan_item.cyan = True
                    file_2 = open('purchased_items/cyan_item.py', 'w')
                    file_2.write('cyan = True')
                    file_2.close()
            if keys[pygame.K_e]:
                if cyan_item.cyan:
                    player_up = cyan_player_up
                    player_down = cyan_player_down
                    player_right = cyan_player_right
                    player_left = cyan_player_left
                    player_idle = cyan_player_idle
        if keys[pygame.K_4]:
            if keys[pygame.K_o]:
                if money >= 1000 and not yellow_item.yellow:
                    money -= 1000
                    yellow_item.yellow = True
                    file_2 = open('purchased_items/yellow_item.py', 'w')
                    file_2.write('yellow = True')
                    file_2.close()
            if keys[pygame.K_e]:
                if yellow_item.yellow:
                    player_up = yellow_player_up
                    player_down = yellow_player_down
                    player_right = yellow_player_right
                    player_left = yellow_player_left
                    player_idle = yellow_player_idle
        if keys[pygame.K_5]:
            if keys[pygame.K_o]:
                if money >= 1000 and not red_item.red:
                    money -= 1000
                    red_item.red = True
                    file_2 = open('purchased_items/red_item.py', 'w')
                    file_2.write('red = True')
                    file_2.close()
            if keys[pygame.K_e]:
                if red_item.red:
                    player_up = red_player_up
                    player_down = red_player_down
                    player_right = red_player_right
                    player_left = red_player_left
                    player_idle = red_player_idle
        if keys[pygame.K_6]:
            if keys[pygame.K_o]:
                if money >= 1000 and not purple_item.purple:
                    money -= 1000
                    purple_item.purple = True
                    file_2 = open('purchased_items/purple_item.py', 'w')
                    file_2.write('purple = True')
                    file_2.close()
            if keys[pygame.K_e]:
                if purple_item.purple:
                    player_up = purple_player_up
                    player_down = purple_player_down
                    player_right = purple_player_right
                    player_left = purple_player_left
                    player_idle = purple_player_idle
        if keys[pygame.K_b]:
            shop = False
            menu = True
            time.sleep(0.3)
    if game and not menu and not game_over:
        draw_game()
        text_in_line_bar_score = fonts_game.render('S  C  O  R  E  :  ' + str(score), False, (255, 255, 255))
        win.blit(text_in_line_bar_score, (325, 559))
        player_hit_box = blue_player_idle.get_rect(topleft=(player_x, player_y))
        point_hit_box = point.get_rect(topleft=(score_x, score_y))
        win.blit(point, (score_x, score_y))
        if keys[pygame.K_w]:
            up = True
            down = False
            right = False
            left = False
            player_anim = True
        if keys[pygame.K_s]:
            down = True
            up = False
            right = False
            left = False
        if keys[pygame.K_d]:
            right = True
            up = False
            down = False
            left = False
        if keys[pygame.K_a]:
            left = True
            up = False
            down = False
            right = False
        if keys[pygame.K_p]:
            pause = True

        if up and player_y > 0:
            player_y -= player_speed
            win.blit(player_up, (player_x, player_y))
        elif down and player_y < 500:
            player_y += player_speed
            win.blit(player_down, (player_x, player_y))
        elif right and player_x < 752:
            player_x += player_speed
            win.blit(player_right, (player_x, player_y))
        elif left and player_x > 0:
            player_x -= player_speed
            win.blit(player_left, (player_x, player_y))
        else:
            win.blit(player_idle, (player_x, player_y))
        if player_hit_box.colliderect(point_hit_box):
            score_x = random.randint(0, 752)
            score_y = random.randint(0, 500)
            player_speed += 0.05
            money += 10
            score += 10
        if player_y < 0 or player_y > 500 or player_x > 752 or player_x < 0:
            game_over = True
            game = False
    if pause and not menu and not game_over:
        draw_pause()
        game = False
        pause = True
        if keys[pygame.K_c]:
            pause = False
            game = True
        if keys[pygame.K_b]:
            pause = False
            menu = True
            up = False
            down = False
            right = False
            left = False
            player_x = 375
            player_y = 250
            score_x = random.randint(0, 752)
            score_y = random.randint(0, 500)
            if score > score_record:
                score_record = score
                file_4 = open('score_record.py', 'w')
                file_4.write(f'score_record = {score}')
                file_4.close()
    if game_over:
        draw_game_over_screen()
        if keys[pygame.K_b]:
            game_over = False
            menu = True
            up = False
            down = False
            right = False
            left = False
            player_x = 375
            player_y = 250
            score_x = random.randint(0, 752)
            score_y = random.randint(0, 500)
            if score > score_record:
                file_4 = open('score_record.py', 'w')
                file_4.write(f'score_record = {score}')
                file_4.close()
        if keys[pygame.K_r]:
            game_over = False
            menu = False
            game = True
            up = False
            down = False
            right = False
            left = False
            player_x = 375
            player_y = 250
            score_x = random.randint(0, 752)
            score_y = random.randint(0, 500)
            score = 0
        if score > score_record:
            score_record = score
            file = open('score_record.py', 'w')
            file.write(f'score_record = {score}')
            file.close()
        file_1 = open('money.py', 'w')
        file_1.write(f'money = {money}')
        file_1.close()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            file_1 = open('money.py', 'w')
            file_1.write(f'money = {money}')
            file_1.close()
            if score > score_record:
                file = open('score_record.py', 'w')
                file.write(f'score_record = {score}')
                file.close()
            file_3 = open('volume_config.py', 'w')
            file_3.write(f'volume = {volume}')
            file_3.close()
            pygame.quit()
            run = not run
