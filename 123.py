
#显示提示消息
def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to play.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

#程序退出系统
def terminate():
    pygame.quit()
    sys.exit()

#随机起始位置函数
def getRandomLocation():
    randx=random.randint(0,CELLWIDTH - 1)
    randy=random.randint(0,CELLHEIGHT - 1)
    if (randx in range(3,11) or randx in range(21,29)) and randy==5:
        randx=random.randint(0,CELLWIDTH - 1)
        randy=random.randint(0,CELLHEIGHT - 1)
    elif (randy ==17 and randx in range(13,18)) or (randy==6 and randx in [9,27]):
        randx=random.randint(0,CELLWIDTH - 1)
        randy=random.randint(0,CELLHEIGHT - 1)
    elif (randy ==15 and randx ==17) or (randy==16 and randx ==16):
        randx=random.randint(0,CELLWIDTH - 1)
        randy=random.randint(0,CELLHEIGHT - 1)
    return {'x': randx, 'y': randy}

#显示游戏结束提示框
def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 100)
    gameSurf = gameOverFont.render('you killed', True, WHITE)
    overSurf = gameOverFont.render('yourself', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear out any key presses in the event queue

    while True:
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
#显示得分情况
def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

#讲蛇描绘出来
def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, DARKGREEN, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, RED, wormInnerSegmentRect)

#把苹果画出来
def drawApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, RED, appleRect)

#将障碍物画出来
def drawbarrier(barrierCoords):
     for coord in barrierCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        barrierRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, RED, barrierRect)
        barrierInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, WHITE, barrierInnerSegmentRect)

#画格子
def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))


if __name__ == '__main__':
    main()
