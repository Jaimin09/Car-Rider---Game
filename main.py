
import pygame
import random
import obstacle
import player

pygame.init()

explosion_sound = pygame.mixer.Sound('Sounds/Explosion+3.wav')
Finish_Applause = pygame.mixer.Sound('Sounds/applause.wav')
pygame.mixer.music.load('Sounds/gameStart.wav')
pygame.mixer.music.play(-1)

black = (0,0,0)
red = (200,0,0)
blue = (0,0,175)
lightBlue = (0,0,255)
green = (0,200,0)
white = (255,255,255)
grey = (100,100,100)
lightRed = (255,0,0)
yellow = (200,200,0)
lightYellow = (255,255,0)
lightGreen = (0,255,0)

homepage = pygame.image.load('Images/lamborgini.png')
enemycar = pygame.image.load('Images/enemycar.png')

display_width = 500
display_height =700

roadStart = 100
roadEnd = 400

clock = pygame.time.Clock()
gameDisplay= pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Cars')
mainroad = pygame.image.load('Images/mainRoad.png')
mainroad2 = pygame.image.load('Images/mainRoad2.png')
playerCar1 = pygame.image.load('Images/car1.png')
icon = pygame.image.load('Images/icon.png')
pygame.display.set_icon(icon)


smallfont = pygame.font.SysFont("Gabriola", 35, bold= False, italic= True)
mediumfont = pygame.font.SysFont("Gabriola", 50, bold= False, italic= False)
largefont = pygame.font.SysFont("Gabriola", 100, bold= False, italic= False)


def text_object(text, color, font_size):
    if font_size == 'small':
        textSurf = smallfont.render(text, True, color)
    if font_size == 'medium':
        textSurf = mediumfont.render(text, True, color)
    if font_size == 'large':
        textSurf = largefont.render(text, True, color)
    textRect = textSurf.get_rect()
    return textSurf, textRect
def message_to_screen(text, color, y_coordinate ,font_size='small'):
    textSurf, textRect = text_object(text, color, font_size)
    textRect.center = display_width/2, display_height/2 + y_coordinate
    gameDisplay.blit(textSurf, textRect)

def text_to_button(text, color, button_position_and_size_list, font_size= 'small'):
    textSurf, textRect = text_object(text, color, font_size)
    textRect.center = button_position_and_size_list[0]+((button_position_and_size_list[2])/2), button_position_and_size_list[1]+((button_position_and_size_list[3])/2)
    gameDisplay.blit(textSurf, textRect)

def button(text, inactive_color, active_color, but_position, text_color= black, action = None):
    global control
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if but_position[0]+but_position[2]> cur[0] > but_position[0] and but_position[1]+but_position[3] > cur[1] > but_position[1]:
        pygame.draw.rect(gameDisplay, active_color, but_position)
        if click[0] == 1 and action != None :
            if action == "play":
                pygame.mixer.music.stop()
                pygame.mixer.music.load('Sounds/carhorn.wav')
                pygame.mixer.music.play(-1)
                gameLoop()
            if action == 'level2':
                gameLoop2()
            if action == "quit":
                pygame.quit()
                quit()
            if action == "manual":
                manual()
            #if action == "main":
             #   gameIntro()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, but_position)
    text_to_button(text, text_color, but_position)

def gameIntro():
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(yellow)
        gameDisplay.blit(homepage, (display_width/2 - 148, display_height/2 - 250))
        button("Play", green, lightGreen, [roadStart + 10*(roadEnd-roadStart)/400, 500, 120, 50],
               action='play')
        button("Quit", red, lightRed, [roadStart + 10 * (roadEnd - roadStart) / 400 + 160, 500, 120, 50], action='quit')
        button("Manuals", blue, lightBlue, [(roadStart + 10 * (roadEnd - roadStart) / 400) + 75, 425, 120, 50],
               action='manual')
        # button("Multiplayer Play", blue, lightBlue, [135, 425, 220, 50],
        #      action='multi')
        message_to_screen('CARS', red, 0, font_size='large')
        pygame.display.update()

def manual():
    main = True
    while main:
        gameDisplay.fill(yellow)
        message_to_screen("Accelerate = UP KEY", black, -300)
        message_to_screen("Slow = DOWN KEY", black, -250)
        message_to_screen("MoveRight = RIGHT KEY", black, -200)
        message_to_screen("MoveLeft = LEFT KEY", black, -150)
        message_to_screen("GearUp = SPACE", black, -100)
        message_to_screen("GearDown = x", black, -50)
        button("Play", green, lightGreen, [(roadStart + 10 * (roadEnd - roadStart) / 400) +75, 500, 120, 50],
               action='play')
       # button('MainMenu', green, lightGreen, [(roadStart + 10 * (roadEnd - roadStart) / 400) + 75,425, 120, 50], action= 'main')
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

def collide(pcX, pcY):
    collide = True
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosion_sound)
    while collide:
        pointList = [(pcX,pcY),(pcX-20,pcY-10),(pcX+10,pcY-5),(pcX-10,pcY-20),(pcX+25,pcY-5),(pcX+60,pcY-20),(pcX+40,pcY-5),(pcX+70,pcY-10),(pcX+50,pcY)]
        colorList = [red, lightRed, yellow, lightYellow]
        colorIndex  = random.randrange(0,4)
        clock.tick(30)
        for i in range(1):
            pygame.draw.polygon(gameDisplay, colorList[colorIndex], pointList)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        message_to_screen('You Explode', red, 0, font_size='medium')
        button(" PlayAgain", green, lightGreen, [roadStart+10*(roadEnd - roadStart) / 400,120,120,50],action='play')
        button("Quit", red, lightRed, [roadStart+10*(roadEnd - roadStart) / 400 + 160,120,120,50], action='quit')

def gameFinish():
    finish = True
    while finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        message_to_screen('You Win', red, 0, font_size='medium')
        button(" level 2", green, lightGreen, [roadStart+10*(roadEnd - roadStart) / 400,120,120,50],action='play')
        button("Quit", red, lightRed, [roadStart+10*(roadEnd - roadStart) / 400 + 160,120,120,50], action='quit')
        pygame.display.update()
   

def gameLoop():
    gameExit = False
    backgroundRoll = 0
    backgroundRollChangeY = 5
    player1_carX = 250
    player1_carY = 520
    player1_car_changeX = 0
    player1_car_changeY = 0
    backgroundImageRepeat = 21
    enemycarX1 = 100
    enemycarY1 = -200
    enemycarX2 = 200
    enemycarY2 = -5000
    enemycarX3 = 200
    enemycarY3 = -12000
    enemycarX4 = 200
    enemycarY4 = -15000   
    enemycarX_change = 0
    enemycarY_change = 10
    gear = 1
    player1_list = pygame.sprite.Group()
    block_list = pygame.sprite.Group()
    player1 = player.Player(player1_carX,player1_carY, 'car1')
    for i in range(int((backgroundImageRepeat-1)*1.8)):
        block = obstacle.Obstacle()
        block.rect.x = random.randrange(roadStart,roadEnd,51)
        block.rect.y = random.randrange(-((backgroundImageRepeat-1)*700)+700,0,100)
        block_list.add(block)
    player1_list.add(player1)

    while not gameExit :

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_DOWN:
                 #   backgroundRollChangeY = -20
                if event.key == pygame.K_LEFT:
                    player1_car_changeX = -10
                if event.key == pygame.K_RIGHT:
                    player1_car_changeX = 10
                if event.key == pygame.K_SPACE:
                    gear += 1
                if event.key == pygame.K_x:
                    gear -= 1
                if event.key == pygame.K_UP:
                    backgroundRollChangeY = 20
                    player1_car_changeY = -2
                    enemycarY_change = 25

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    backgroundRollChangeY = 5
                    player1_car_changeY = +2
                    enemycarY_change = 5
                if event.key == pygame.K_LEFT:
                    player1_car_changeX = 0
                if event.key == pygame.K_RIGHT:
                    player1_car_changeX = 0
               #if event.key == pygame.K_DOWN:
                  #  backgroundRollChangeY = 5

        backgroundRoll += backgroundRollChangeY
        enemycarY1 += enemycarY_change
        enemycarY2 += enemycarY_change
        enemycarY3 += enemycarY_change
        enemycarY4 += enemycarY_change
        player1_carY += player1_car_changeY
        player1_carX += player1_car_changeX

        carchange = [0,51,-51]
        for i in range(30):
            carchange.append(0)
        carchangeIndex = random.randrange(0,32)       
        enemycarX1 += carchange[carchangeIndex]
        enemycarX2 += carchange[carchangeIndex]
        enemycarX3 += carchange[carchangeIndex]
        enemycarX4 += carchange[carchangeIndex]

        if player1_carY <= 500- gear*25:
            player1_carY = 500- gear*25
        if player1_carY >= 520:
            player1_carY = 520
        if gear < 1:
            gear = 1
        if gear > 6:
            gear = 6
        if player1_carX >(roadEnd - 50)+ 2:
            collide(player1_carX,player1_carY)
            #player1_carX= (roadEnd-50)
        if player1_carX < roadStart-2:
            collide(player1_carX,player1_carY)
            #player1_carX = roadStart


        if backgroundRoll < 0:
            backgroundRoll = 0
        if backgroundRoll > ((backgroundImageRepeat-1)*700):
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(Finish_Applause)
            backgroundRoll = ((backgroundImageRepeat-1)*700)

        for i in range(0,backgroundImageRepeat):
            gameDisplay.blit(mainroad, (0,backgroundRoll+i*(-700)))

        pygame.draw.rect(gameDisplay, grey, (roadStart, 450 + backgroundRoll, (roadEnd - roadStart), 5))
        pygame.draw.rect(gameDisplay, grey, (roadStart, 510 + backgroundRoll, (roadEnd - roadStart), 5))
        message_to_screen("START", grey, 130 + backgroundRoll, 'medium')

        pygame.draw.rect(gameDisplay, grey,
                         (roadStart, 100 + 450 - (backgroundImageRepeat - 1) * 700 + backgroundRoll, (roadEnd - roadStart), 5))
        pygame.draw.rect(gameDisplay, grey,
                         (roadStart, 100 + 510 - (backgroundImageRepeat - 1) * 700 + backgroundRoll,(roadEnd - roadStart), 5))
        message_to_screen("FINISH", grey, 100 + 130 - (backgroundImageRepeat - 1) * 700 + backgroundRoll, 'medium')
        message_to_screen("YOU WIN", red, -300+130 - (backgroundImageRepeat - 1) * 700 + backgroundRoll, 'large')
        button(" level 2", green, lightGreen, [roadStart+10*(roadEnd - roadStart) / 400,  250-(backgroundImageRepeat-1)*700 + backgroundRoll,120,50],action='level2')
        button("Quit", red, lightRed, [roadStart+10*(roadEnd - roadStart) / 400 + 160, 250-(backgroundImageRepeat-1)*700 + backgroundRoll ,120,50], action='quit')

        block_list.update(backgroundRollChangeY)
        block_list.draw(gameDisplay)
        player1_list.update(player1_carX, player1_carY)
        player1_list.draw(gameDisplay)


        message_to_screen('Gear : '+str(gear), black, -250)
        distanceText = smallfont.render('  Distance : ' + str(backgroundRoll / 1000) , True, black)
        gameDisplay.blit(distanceText, (roadStart+0.4*roadStart, 50))
        distanceText = smallfont.render('km', True, black)
        gameDisplay.blit(distanceText, (roadEnd-50-0.05*roadEnd, 50))
        block_hit_list1 = pygame.sprite.spritecollide(player1, block_list, False)

        for block in block_hit_list1:
            collide(player1_carX,player1_carY)
       

        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()

def gameLoop2():
    gameExit = False
    backgroundRoll = 0
    backgroundRollChangeY = 5
    player1_carX = 250
    player1_carY = 520
    player1_car_changeX = 0
    player1_car_changeY = 0
    backgroundImageRepeat = 31
    enemycarX1 = 100
    enemycarY1 = -200
    enemycarX2 = 200
    enemycarY2 = -5000
    enemycarX3 = 200
    enemycarY3 = -12000
    enemycarX4 = 200
    enemycarY4 = -15000

    enemycarX_change = 0
    enemycarY_change = 10
    gear = 1
    player1_list = pygame.sprite.Group()
    block_list = pygame.sprite.Group()
    player1 = player.Player(player1_carX,player1_carY, 'car1')
    for i in range(int((backgroundImageRepeat-1)*1.8)):
        block = obstacle.Obstacle()
        block.rect.x = random.randrange(roadStart,roadEnd,51)
        block.rect.y = random.randrange(-((backgroundImageRepeat-1)*700)+700,0,100)
        block_list.add(block)
    player1_list.add(player1)

    while not gameExit :

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_DOWN:
                 #   backgroundRollChangeY = -20
                if event.key == pygame.K_LEFT:
                    player1_car_changeX = -10
                if event.key == pygame.K_RIGHT:
                    player1_car_changeX = 10
                if event.key == pygame.K_SPACE:
                    gear += 1
                if event.key == pygame.K_x:
                    gear -= 1
                if event.key == pygame.K_UP:
                    backgroundRollChangeY = 20
                    player1_car_changeY = -2
                    enemycarY_change = 25

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    backgroundRollChangeY = 5
                    player1_car_changeY = +2
                    enemycarY_change = 5
                if event.key == pygame.K_LEFT:
                    player1_car_changeX = 0
                if event.key == pygame.K_RIGHT:
                    player1_car_changeX = 0
               #if event.key == pygame.K_DOWN:
                  #  backgroundRollChangeY = 5

        backgroundRoll += backgroundRollChangeY
        enemycarY1 += enemycarY_change
        enemycarY2 += enemycarY_change
        enemycarY3 += enemycarY_change
        enemycarY4 += enemycarY_change
        player1_carY += player1_car_changeY
        player1_carX += player1_car_changeX

        carchange = [0,51,-51]
        for i in range(30):
            carchange.append(0)
        carchangeIndex = random.randrange(0,32)
        enemycarX1 += carchange[carchangeIndex]
        enemycarX2 += carchange[carchangeIndex]
        enemycarX3 += carchange[carchangeIndex]
        enemycarX4 += carchange[carchangeIndex]

        if player1_carY <= 500- gear*25:
            player1_carY = 500- gear*25
        if player1_carY >= 520:
            player1_carY = 520
        if gear < 1:
            gear = 1
        if gear > 6:
            gear = 6
        if player1_carX >(roadEnd - 50)+ 2:
            collide(player1_carX,player1_carY)
            #player1_carX= (roadEnd-50)
        if player1_carX < roadStart-2:
            collide(player1_carX,player1_carY)
            #player1_carX = roadStart

        if enemycarX1 >(roadEnd - 50)+2:
            enemycarX1 = (roadEnd - 50)+2
        if enemycarX1 < roadStart-2:
            enemycarX1 = roadStart-2
        if enemycarX2 >(roadEnd - 50)+2:
            enemycarX2 = (roadEnd - 50)+2
        if enemycarX2 < roadStart-2:
            enemycarX2 = roadStart-2
        if enemycarX3>(roadEnd - 50)+2:
            enemycarX3 = (roadEnd - 50)+2
        if enemycarX3< roadStart-2:
            enemycarX3 = roadStart-2
        if enemycarX4>(roadEnd - 50)+2:
            enemycarX4 = (roadEnd - 50)+2
        if enemycarX4< roadStart-2:
            enemycarX4 = roadStart-2

        if backgroundRoll < 0:
            backgroundRoll = 0
        if backgroundRoll > ((backgroundImageRepeat-1)*700):
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(Finish_Applause)
            backgroundRoll = ((backgroundImageRepeat-1)*700)

        for i in range(0,backgroundImageRepeat):
            gameDisplay.blit(mainroad2, (0,backgroundRoll+i*(-700)))


        #message_to_screen('Distance : ', black, -300)

        pygame.draw.rect(gameDisplay, grey, (roadStart, 450 + backgroundRoll, (roadEnd - roadStart), 5))
        pygame.draw.rect(gameDisplay, grey, (roadStart, 510 + backgroundRoll, (roadEnd - roadStart), 5))
        message_to_screen("START", grey, 130 + backgroundRoll, 'medium')
        message_to_screen("YOU WIN", red, -300+130 - (backgroundImageRepeat - 1) * 700 + backgroundRoll, 'large')
        pygame.draw.rect(gameDisplay, grey,
                         (roadStart, 100 + 450 - (backgroundImageRepeat - 1) * 700 + backgroundRoll, (roadEnd - roadStart), 5))
        pygame.draw.rect(gameDisplay, grey,
                         (roadStart, 100 + 510 - (backgroundImageRepeat - 1) * 700 + backgroundRoll,(roadEnd - roadStart), 5))
        message_to_screen("FINISH", grey, 100 + 130 - (backgroundImageRepeat - 1) * 700 + backgroundRoll, 'medium')

        block_list.update(backgroundRollChangeY)
        block_list.draw(gameDisplay)
        player1_list.update(player1_carX, player1_carY)
        player1_list.draw(gameDisplay)

        gameDisplay.blit(enemycar, (enemycarX1, enemycarY1))
        gameDisplay.blit(enemycar, (enemycarX2, enemycarY2))
        gameDisplay.blit(enemycar, (enemycarX3, enemycarY3))
        gameDisplay.blit(enemycar, (enemycarX4, enemycarY4))

        if player1_carX>enemycarX1 and player1_carX<enemycarX1+50 or player1_carX+50>enemycarX1 and player1_carX+50<enemycarX1+50:
            if player1_carY>=enemycarY1 and player1_carY<=enemycarY1+90 or player1_carY+86>=enemycarY1 and player1_carY+86<=enemycarY1+90:
                collide(player1_carX,player1_carY)
        if player1_carX>enemycarX2 and player1_carX<enemycarX2+50 or player1_carX+50>enemycarX2 and player1_carX+50<enemycarX2+50:
            if player1_carY>=enemycarY2 and player1_carY<=enemycarY2+90 or player1_carY+86>=enemycarY2 and player1_carY+86<=enemycarY2+90:
                collide(player1_carX,player1_carY)
        if player1_carX>enemycarX3 and player1_carX<enemycarX3+50 or player1_carX+50>enemycarX3 and player1_carX+50<enemycarX3+50:
            if player1_carY>=enemycarY3 and player1_carY<=enemycarY3+90 or player1_carY+86>=enemycarY3 and player1_carY+86<=enemycarY3+90:
                collide(player1_carX,player1_carY)
        if player1_carX>enemycarX4 and player1_carX<enemycarX4+50 or player1_carX+50>enemycarX4 and player1_carX+50<enemycarX4+50:
            if player1_carY>=enemycarY4 and player1_carY<=enemycarY4+90 or player1_carY+86>=enemycarY4 and player1_carY+86<=enemycarY4+90:
                collide(player1_carX,player1_carY)


        message_to_screen('Gear : '+str(gear), black, -250)
        distanceText = smallfont.render('  Distance : ' + str(backgroundRoll / 1000) , True, black)
        gameDisplay.blit(distanceText, (roadStart+0.4*roadStart, 50))
        distanceText = smallfont.render('km', True, black)
        gameDisplay.blit(distanceText, (roadEnd-50-0.05*roadEnd, 50))
        block_hit_list1 = pygame.sprite.spritecollide(player1, block_list, False)

        for block in block_hit_list1:
            collide(player1_carX,player1_carY)


        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()


gameIntro()
#gameLoop()
