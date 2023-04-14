from Models import*


display.set_caption("PING-PONG")

background = transform.scale(image.load("fight_zone.jpg"), WZ)
player1 = Player("raketka4.png",5,(45,90), 550, 50)
player2 = Player("raketka4.png",5,(45,90), 50, 50)
ball = Gamesprite("ball.png",0, (50,50),200, 200)
#)
font.init()
font_text = font.Font(None, 72)
won1 = font_text.render("Player1 win",1,(0,255,0))
won2 = font_text.render("Player2 win",1,(0,255,0))

speed_x = 3
speed_y = 3




clock = time.Clock()
game_ower = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    
    if not game_ower:
        window.blit(background,(0,0))
        player2.update_l()
        player1.update_r()
        player1.reset()
        player2.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y >= WZ[1] - BZ[1] or ball.rect.y <= 0:
            speed_y *=-1
        if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball, player2):
            speed_x *= - 1

        if ball.rect.x <=0:
            window.blit(won2,(WZ[0]/2 - won2.get_width()/2,WZ[1]/2 - won2.get_height()/2))
            game_ower = True
        if ball.rect.x + ball.rect.width >= WZ[0]:
            window.blit(won1,(WZ[0]/2 - won1.get_width()/2,WZ[1]/2 - won1.get_height()/2))
            game_ower = True
        ball.reset()
        clock.tick(FPS)
        display.update()
        