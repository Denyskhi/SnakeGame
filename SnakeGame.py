import pygame as pg
import time
import keyboard
import random

def drawField():
    sc.fill(LIGHT_GREEN)
    pg.draw.rect(sc, BROWN, (0, y * (cell), x * cell, 70))
    value = score_font.render("Your Score: " + str(score - 2), True, YELLOW)
    value1 = score_font.render("Your High Score: " + str(eHighScore), True, YELLOW)
    sc.blit(value, [0, y * cell])
    sc.blit(value1, [300, y * cell])
    for Y in range(0, y):
        for X in range (0, x):
            if field[Y][X] > 1:
                pg.draw.rect(sc, RED, (X*(cell), Y*(cell), cell - 1, cell - 1))
            elif field[Y][X] == -2:
                pg.draw.rect(sc, YELLOW, (X*cell, Y*cell, cell, cell))
            elif field[Y][X] == 1:
                pg.draw.rect(sc, BLUE, (X*cell, Y*cell, cell, cell))
            else:
                pg.draw.rect(sc, BLACK, (X*cell, Y*cell, cell, cell), 1)
                
    pg.display.update()
def renderApple():
    putApple = True
    for Y in range(0, y):
        for X in range (0, x):
            if field[Y][X] == -2:
                putApple = False
    if putApple:
        posX = random.randint(0, x - 1)
        posY = random.randint(0, y - 1)
        while field[posY][posX] != 0:
            posX = random.randint(0, x - 1)
            posY = random.randint(0, y - 1)
        field[posY][posX] = -2
    return putApple
def lost():
    if score - 2 > eHighScore:
        file = open('HighScore.txt', 'w')
        file.write(str(score - 2))
        file.close()
    sc.fill(RED)
    
    pg.quit()
    exit()

def move(direction):
    greatestNum = 0
    greatestRow = 0
    greatestCol = 0
    headRow = 0
    headCol = 0
    for r in range(0, y):
        for c in range(0, x):
            if field[r][c] > greatestNum:
                greatestNum = field[r][c]
                greatestRow = r
                greatestCol = c
            if field[r][c] == 1:
                headRow = r
                headCol = c
    if direction == 'right':
        if headCol < x - 1 and field[headRow][headCol + 1] <= 0:
            for r in range(0, y):
                for c in range(0, x):
                    if field[r][c] > 0:
                        field[r][c] = field[r][c] + 1
            if field[headRow][headCol + 1] != -2:
                field[greatestRow][greatestCol] = 0
            
            field[headRow][headCol + 1] = 1
            
        else:
            lost()
            
            
    elif direction == 'up':
        if headRow > 0 and field[headRow - 1][headCol] <= 0:
            for r in range(0, y):
                for c in range(0, x):
                    if field[r][c] > 0:
                        field[r][c] = field[r][c] + 1
            if field[headRow - 1][headCol] != -2:
                field[greatestRow][greatestCol] = 0
            
            field[headRow - 1][headCol] = 1
            
            
        else:
            lost()
        
    elif direction == 'down':
        if headRow < y - 1  and field[headRow + 1][headCol] <= 0:
            for r in range(0, y):
                for c in range(0, x):
                    if field[r][c] > 0:
                        field[r][c] = field[r][c] + 1
            if field[headRow + 1][headCol] != -2:
                field[greatestRow][greatestCol] = 0
            
            field[headRow + 1][headCol] = 1
            
        else:
            lost()
            
    elif direction == 'left':
        if headCol > 0  and field[headRow][headCol - 1] <= 0:
            for r in range(0, y):
                for c in range(0, x):
                    if field[r][c] > 0:
                        field[r][c] = field[r][c] + 1
            if field[headRow][headCol - 1] != -2:
                field[greatestRow][greatestCol] = 0
            
            field[headRow][headCol - 1] = 1
            
        else:
            lost()
    return greatestNum
            
                    
size = '15 x 10' #15 x 10
cell = 50    #50
score = 2
eHighScore = 0
try:
    file = open('HighScore.txt', 'r')
    try:
        eHighScore = int(file.readline())
    except:
        eHighScore = 0
except:
    file = open('HighScore.txt', 'w')
finally:
    file.close()
    

x = int(size.split(' x ')[0])
y = int(size.split(' x ')[1])
startTime = time.time()
pg.init()
display = (x * cell, y * cell + 70)
sc = pg.display.set_mode(display)
sideButton = 'right'
LIGHT_GREEN = (100, 255, 50)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (150, 40, 255)
BROWN = (150, 0, 100)
sc.fill(LIGHT_GREEN)
score_font = pg.font.SysFont("comicsansms", 30)
for Y in range(0, y):
        for X in range (0, x):
            pg.draw.rect(sc, BLACK, (X*cell, Y*cell, cell, cell), 1)
pg.draw.rect(sc, BROWN, (x*(cell - 1), y * (cell - 1), x * cell, 100))
pg.display.update()

field = []
for i in range(y):
    field.append([0] * x)

field[int(y/2)][0] = 2
field[int(y/2)][1] = 1

drawField()
while True:
    if keyboard.is_pressed('space'):
        break
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            exit()
while True:
    drawField()
    renderApple()
    if keyboard.is_pressed('left') and sideButton != 'right':
        sideButton = 'left'
        score = move('left')
        time.sleep(0.18)
        startTime = time.time()
    elif keyboard.is_pressed('right') and sideButton != 'left':
        sideButton = 'right'
        score = move('right')
        time.sleep(0.18)
        startTime = time.time()
    elif keyboard.is_pressed('up') and sideButton != 'down':
        sideButton = 'up'
        score = move('up')
        time.sleep(0.18)
        startTime = time.time()
    elif keyboard.is_pressed('down') and sideButton != 'up':
        sideButton = 'down'
        score = move('down')
        time.sleep(0.18)
        startTime = time.time()
    else:
        if time.time() - startTime >= 0.18:
            startTime = time.time()
            score = move(sideButton)
    
    
        
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            exit()
    
