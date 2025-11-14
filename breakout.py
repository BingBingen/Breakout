import pygame, sys
import random

def main():
    pygame.init()
    clock = pygame.time.Clock()

    #------display------
    screen_width = 900
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    FPS = 60 
    font = pygame.font.Font("fonts/pixely.ttf", 34)
    big_font = pygame.font.Font("fonts/pixely.ttf", 70)
    hit_sound = pygame.mixer.Sound("sounds/hit.wav")
    loss_sound = pygame.mixer.Sound("sounds/lose.wav")
    win_sound = pygame.mixer.Sound("sounds/win.wav")

    black = (0,0,0)
    white = (255,255,255)

    #------Sprites/Objects-----
    paddle = pygame.Rect(screen_width/2 - 70, screen_height - 50, 140, 20)
    ball = pygame.Rect(screen_width/2 - 10, screen_height - 80, 20, 20)
    score = 0  
    brick_row = 5
    brick_column = 9
    brick_padding = 10
    brick_width = 80
    brick_height = 30 
    brick_offset_x = 60
    brick_offset_y = 50
    expand_timer = 0
    destroyer_img = pygame.image.load("images/destroyer.png").convert_alpha()
    destroyer_rect = destroyer_img.get_rect(center = (screen_width/2, screen_height/2))
    destroyer_speed = 5

    bricks = []
    for row in range(brick_row):
        for col in range(brick_column):
            brick_x = brick_offset_x + col * (brick_width + brick_padding)
            brick_y = brick_offset_y + row * (brick_height + brick_padding)
            
            if row == 0:
                hp = 3
                points = 50 
                power = random.choice([None, None, None, "expand"]) #random.choice only onlys for a list or tuple
                color = (247, 128, 113) #light red

            elif row == 1 or row == 2:
                hp = 2
                points = 25
                power = random.choice([None, None, None, None, None, "min-expand", "faster"])
                color = (143, 212, 250) #light blue
            else:
                hp = 1
                points = 10
                power = None
                color = (181, 252, 187) #light green

            #list of dictionaries 
            bricks.append({ 
                "rect": pygame.Rect(brick_x, brick_y, brick_width, brick_height),
                "hp": hp,
                "color": color,
                "point": points,
                "power": power
            })

    #-------Game Variables-----
    move_left = False
    move_right = False
    paddle_speed = 0 
    ball_speed_x = 7
    ball_speed_y = -8
    ball_active = False
    song_played = False
    lives = 3 
    pwu = 0 
    def reset_ball(paddle, w = 20, h = 20):
        new_x = paddle.centerx - w
        new_y = paddle.top - h - 5
        return pygame.Rect(new_x, new_y, w, h)

    def paddle_movement(paddle, speed, screen_width): 
        paddle.x += speed 

        if paddle.right >= screen_width:
            paddle.right = screen_width
        elif paddle.left <= 0:
            paddle.left = 0

        return paddle
    
    def ball_animation(ball, speed_x, speed_y, screen_width, screen_height, paddle, lives):
        ball.x += speed_x
        ball.y += speed_y

        if ball.top <= 0:
            ball.top = 0
            speed_y *= -1
        
        elif ball.right >= screen_width:
            speed_x *= -1
            ball.right = screen_width

        elif ball.left <= 0:
            speed_x *= -1 
            ball.left = 0

        elif ball.bottom >= screen_height: 
            ball = reset_ball(paddle)
            speed_y *= -1 
            lives -= 1 
            return ball, speed_x, speed_y, False, lives

        return ball, speed_x, speed_y, True, lives
    
    def destroyer_animation(rect, speed, screen_width):
        rect.x += speed
        if rect.right >= screen_width or rect.left <= 0:
            speed *= -1 
        
        return rect, speed

    # ------ Main Loop ----- 
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                if event.key == pygame.K_RIGHT:
                    move_right = True
                if event.key == pygame.K_UP:
                    ball_active = True
                if event.key == pygame.K_SPACE and song_played == True:
                    main()
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                if event.key == pygame.K_RIGHT:
                    move_right = False
        

        #Updates Sprite
        if move_left:
            paddle_speed = -(9 + pwu)
        elif move_right:
            paddle_speed = (9 + pwu)
        else:
            paddle_speed = 0 
            
        paddle = paddle_movement(paddle, paddle_speed, screen_width)

        if ball_active:
            ball, ball_speed_x, ball_speed_y, ball_active, lives = ball_animation(ball, ball_speed_x, ball_speed_y, screen_width, screen_height, paddle, lives)
            destroyer_rect, destroyer_speed = destroyer_animation(destroyer_rect, destroyer_speed, screen_width)

            if ball.colliderect(paddle) and ball_speed_y > 0:
                offset = ball.centerx - paddle.centerx 
                normalized_offset = offset / (paddle.width / 2)
                ball_speed_x = normalized_offset * 7   # control angle
                ball_speed_y *= -1        
            '''
            if ball.colliderect(destroyer_rect):
                #top and bottom collision
                if ball_speed_y > 0 and ball.bottom >= destroyer_rect.top and ball.top >= destroyer_rect.top:
                    ball.bottom = destroyer_rect.top - 1
                    ball_speed_y *= -1
                elif ball_speed_y < 0 and ball.top <= destroyer_rect.bottom and ball.bottom > destroyer_rect.bottom:
                    ball.top = destroyer_rect.bottom + 1
                    ball_speed_y *= -1
                else:
                    # Side collision
                    if ball.centerx < destroyer_rect.centerx:
                        ball.right = destroyer_rect.left - 1
                    else:
                        ball.left = destroyer_rect.right + 1
                    ball_speed_x *= -1
                hit_sound.play()
            ''' 
        else:
            ball.centerx = paddle.centerx
            ball.bottom = paddle.top - 5
        '''
        

        '''
        #each brick is a dictionary
        for brick in bricks[:]:
            rect = brick["rect"]
            points = brick["point"]
            if ball.colliderect(rect):
                brick["hp"] -= 1
                hit_sound.play()

                if brick["hp"] <= 0:
                    bricks.remove(brick)
                    ball_speed_x *= 1 + random.uniform(0.01,0.05)
                    ball_speed_y *= 1 + random.uniform(0.01,0.05)
                    score += points

                    if brick["power"] == "expand":
                        paddle.width = min(paddle.width + 60, 220)
                        expand_timer = pygame.time.get_ticks()
                    elif brick["power"] == "min-expand": 
                        paddle.width = min(paddle.width + 35, 180)
                        expand_timer = pygame.time.get_ticks()
                    elif brick["power"] == "faster":
                        pwu += 0.5
                else:
                    r, g, b = brick["color"]
                    brick["color"] = (max(0, r - 40), max(0, g - 40), max(0, b - 40))

                ball_speed_y *= - 1
                break
                    
            
        #Screen
        screen.fill(black)
        pygame.draw.rect(screen, white, paddle)
        pygame.draw.ellipse(screen, white, ball)
        score_text = font.render(f"Score: {score}", True, white)
        screen.blit(score_text, (20, 10))
        lives_text = font.render(f'Lives: {lives}', True, white)
        screen.blit(lives_text, (screen_width - 150, 10))
        #screen.blit(destroyer_img, destroyer_rect)

        for brick in bricks:
            pygame.draw.rect(screen, brick["color"], brick["rect"])

        if lives == 0:
            ball_speed_x, ball_speed_y, paddle_speed = 0,0,0
            game_over_text = big_font.render("GAME OVER!", True, white)
            game_rect = game_over_text.get_rect(center = (screen_width/2, screen_height/2))
            screen.blit(game_over_text, game_rect)

            play_again_text = font.render("Press SPACE to Restart.", True, white)
            again_rect = play_again_text.get_rect(center = (screen_width/2, screen_height/2 + 50))
            screen.blit(play_again_text, again_rect)
        
            if song_played == False:
                loss_sound.play()
                song_played = True

        if bricks == []:
            ball_speed_x = ball_speed_y = paddle_speed = 0 

            game_over_text = big_font.render("You Win!", True, white)
            game_rect = game_over_text.get_rect(center = (screen_width/2, screen_height/2))
            screen.blit(game_over_text, game_rect)

            play_again_text = font.render("Press SPACE to Play Again.", True, white)
            again_rect = play_again_text.get_rect(center = (screen_width/2, screen_height/2 + 50))
            screen.blit(play_again_text, again_rect)

            if song_played == False:
                win_sound.play()
                song_played = True

        if expand_timer != 0 and pygame.time.get_ticks() - expand_timer > 5000:
            paddle.width = 140
            expand_timer = 0


        clock.tick(FPS)
        pygame.display.flip()

if __name__ == "__main__":
    main()

