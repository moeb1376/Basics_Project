import pygame, sys, pygame.font, pygame.draw, string, random
from pygame.locals import *
import pygame.event as GAME_EVENTS

pygame.init()

pressRotate = True
pressDice = True
x = 3
y = 3
turn = 0
num = 0
pos = 0
boardX = 150
boardY = 150
cell = 50
windowWidth = 650
windowHeight = 650
playerCoin = [30, 30, 30, 30]
BoardList = [[None,None,None,None,"G",None,None],
             [None,None,None,None,None,None,None],
             [None,None,"Y",None,None,None,None],
             [None,None,None,None,None,None,None],
             [None,"R",None,None,None,None,None],
             [None,None,None,None,None,"B",None],
             [None,None,None,None,None,None,None]]

surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Marrakech Board!')

def quitgame():
    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
def get_key():
  while True:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
def display_box(screen, boxX, boxY, message):
  pygame.draw.rect(screen, (0,0,0), (boxX, boxY, 200,20), 0)
  pygame.draw.rect(screen, (255,255,255), (boxX - 2, boxY - 2,204,24), 2)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)), (boxX, boxY+3))
  pygame.display.flip()
def ask(screen, boxX, boxY, question):
  pygame.font.init()
  current_string = []
  display_box(screen, boxX, boxY, question + string.join(current_string,""))
  while True:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, boxX, boxY, question + string.join(current_string,""))
  return string.join(current_string,"")
def box(screen,boxX,boxY,turn):
  carpet = ask(screen, boxX, boxY, "").split("/")
  carpet1 = carpet[0].split("-")
  carpet2 = carpet[1].split("-")
  if (turn%4 == 0):
    BoardList[ int(carpet1[0]) - 1 ][ int(carpet1[1]) - 1 ] = "Y"
    BoardList[ int(carpet2[0]) - 1 ][ int(carpet2[1]) - 1 ] = "Y"
  if (turn%4 == 1):
    BoardList[ int(carpet1[0]) - 1 ][ int(carpet1[1]) - 1 ] = "R"
    BoardList[ int(carpet2[0]) - 1 ][ int(carpet2[1]) - 1 ] = "R"
  if (turn%4 == 2):
    BoardList[ int(carpet1[0]) - 1 ][ int(carpet1[1]) - 1 ] = "G"
    BoardList[ int(carpet2[0]) - 1 ][ int(carpet2[1]) - 1 ] = "G"
  if (turn%4 == 3):
    BoardList[ int(carpet1[0]) - 1 ][ int(carpet1[1]) - 1 ] = "B"
    BoardList[ int(carpet2[0]) - 1 ][ int(carpet2[1]) - 1 ] = "B"
def AssamMove(screen,pos,x,y):
    if (pos%4 == 1):
        pygame.draw.circle(screen, (165,42,42), (x,y), 20, 0)
        pygame.draw.circle(screen, (255,255,255), (x,y), 20, 2)
        pygame.draw.circle(screen, (0,0,0), (x, y - 8), 5, 0)
        pygame.draw.circle(screen, (0,0,0), (x, y + 8), 5, 0)
        pygame.draw.circle(screen, (0,0,0), (x + 8, y), 5, 0)
    if (pos%4 == 0):
        pygame.draw.circle(screen, (165,42,42), (x,y), 20, 0)
        pygame.draw.circle(screen, (255,255,255), (x,y), 20, 2)
        pygame.draw.circle(screen, (0,0,0), (x, y - 8), 5, 0)
        pygame.draw.circle(screen, (0,0,0), (x + 8, y), 5, 0)
        pygame.draw.circle(screen, (0,0,0), (x - 8, y), 5, 0)
    if (pos%4 == 3):
        pygame.draw.circle(screen, (165,42,42), (x,y), 20, 0)
        pygame.draw.circle(screen, (255,255,255), (x,y), 20, 2)
        pygame.draw.circle(screen, (0,0,0), (x, y + 8), 5, 0)
        pygame.draw.circle(screen, (0,0,0), (x - 8, y), 5, 0)
        pygame.draw.circle(screen, (0,0,0), (x, y - 8), 5, 0)
    if (pos%4 == 2):
        pygame.draw.circle(screen, (165,42,42), (x,y), 20, 0)
        pygame.draw.circle(screen, (255,255,255), (x,y), 20, 2)
        pygame.draw.circle(screen, (0,0,0), (x, y + 8), 5, 0)
        pygame.draw.circle(screen, (0,0,0), (x - 8, y), 5, 0)
        pygame.draw.circle(screen, (0,0,0), (x + 8, y), 5, 0)

class ShowBoard:
    def __init__(self):
        pass

    def lines(self,screen,x,y,cell):
        for i in range(y, y+8*cell, cell):
            pygame.draw.line(screen, (255,255,255), (y,i), (y+7*cell,i), True)
        for i in range(x, x+8*cell, cell):
            pygame.draw.line(screen, (255,255,255), (i,x), (i,x+7*cell), True)

    def borders(self,screen,x,y,cell):
        for i in range(y, y+8*cell, 2*cell):
            pygame.draw.circle(screen, (255,255,255), (x, i), cell/2, 1)
        for i in range(x, x+8*cell, 2*cell):
            pygame.draw.circle(screen, (255,255,255), (i, y), cell/2, 1)
        for i in range(y+7*cell, y, -2*cell):
            pygame.draw.circle(screen, (255,255,255), (x+7*cell, i), cell/2, 1)
        for i in range(x+7*cell, x, -2*cell):
            pygame.draw.circle(screen, (255,255,255), (i, y+7*cell), cell/2, 1)
        pygame.draw.rect(surface,(100,100,100),(x,y,x+4*cell,y+4*cell))

    def cells(self,screen,list):
        for i in range (7):
            for j in range (7):
                if list[j][i] == None:
                    continue
                elif list[j][i] == "Y":
                    pygame.draw.rect(screen,(255,222,0),(150 + i*50, 150 + j*50, 50, 50))
                elif list[j][i] == "R":
                    pygame.draw.rect(screen,(255,0,0),(150 + i*50, 150 + j*50, 50, 50))
                elif list[j][i] == "G":
                    pygame.draw.rect(screen,(0,255,0),(150 + i*50, 150 + j*50, 50, 50))
                else:
                    pygame.draw.rect(screen,(0,0,255),(150 + i*50, 150 + j*50, 50, 50))
class assam:
    def __init__(self, face=1, x=3, y=3):
        self.face = face
        self.x = x
        self.y = y

    def move(self, dice):
        if self.face == 1:
            hel = self.x + dice
            if self.y != 6:
                self.x = hel - (hel - 6 + hel % 7) * int(hel > 6)
                self.y += (-1) ** (self.y) * (hel // 7)
                self.face += 2 * (hel // 7)
            else:
                self.x = hel - (hel % 7 + 1) * (hel // 7)
                self.y -= (hel % 7) * (hel // 7)
                self.face += 3 * (hel // 7)
        elif self.face == 4:
            hel = self.y - dice
            if self.x != 0:
                self.y = hel - (2 * hel + 1) * int(hel < 0)
                self.x += (-1) ** (self.x + 1) * int(hel < 0)
                self.face -= 2 * int(hel < 0)
            else:
                self.y = hel * int(hel > 0)
                self.x = (-1) * (hel + 1) * int(hel < 0)
                self.face -= 3 * int(hel < 0)
        elif self.face == 3:
            hel = self.x - dice
            if self.y != 0:
                self.x = hel - (2 * hel + 1) * int(hel < 0)
                self.y += (-1) ** (self.y + 1) * int(hel < 0)
                self.face -= 2 * int(hel < 0)
            else:
                self.x = hel * int(hel > 0)
                self.y = (-1) * (hel + 1) * int(hel < 0)
                self.face -= int(hel < 0)
        else:
            hel = self.y + dice
            if self.x != 6:
                self.y = hel - (hel - 6 + hel % 7) * int(hel > 6)
                self.x += (-1) ** (self.x) * (hel // 7)
                self.face += 2 * (hel // 7)
            else:
                self.y = hel - (hel % 7 + 1) * (hel // 7)
                self.x -= (hel % 7) * (hel // 7)
                self.face += (hel // 7)

    def __str__(self):
        return 'assam . x : ' + str(self.x) + ' / assam . y : ' + str(self.y) + ' / assam . face : ' + str(self.face)
class carpet:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self):
        return self.color + "  " + str(self.number)

    def __eq__(self, other):
        return ((self.color == other.color) and (self.number == other.number))
class player:
    def __init__(self, colorCarpet, numberCarpets):
        self.playerCarpet = [carpet(colorCarpet, i) for i in range(numberCarpets)]

    def get_player_carpet(self):
        hel = self.playerCarpet[0]
        self.playerCarpet.remove(0)
        return hel
class board:
    turn = 0
    round = 0

    def __init__(self, numberPlayers, detail=[[0 for i in range(7)] for i in range(7)]):
        self.numberPlayers = numberPlayers
        self.detail = detail

    def get_number_carpets(self):
        if (self.numberPlayers == 4):
            return 12
        else:
            return 15

    def get_detail_XY(self, x, y):
        return self.detail[x][y]

    def set_turn(self):
        if self.turn == 3:
            self.turn = 0
            self.round += 1
        else:
            self.turn += 1

AssamMove(surface,pos,windowWidth/2,windowHeight/2)
myAssam = assam(4,3,3)

while True:

    delay = 0
    surface.fill((0,0,0))
    pygame.draw.rect(surface,(100,100,100),(0,0,windowWidth,windowHeight))
    mousePosition = pygame.mouse.get_pos()
    fontobject = pygame.font.Font(None,18)

    MarrakechBoard = ShowBoard()
    ShowBoard.borders(MarrakechBoard,surface,boardX,boardY,cell)
    ShowBoard.cells(MarrakechBoard,surface,BoardList)
    ShowBoard.lines(MarrakechBoard,surface,boardX,boardY,cell)

    assamX = boardX + cell / 2 + cell * myAssam.x
    assamY = boardY + cell / 2 + cell * myAssam.y
    AssamMove(surface,myAssam.face,assamX,assamY)


    rotateX = 10
    rotateY = 10
    pygame.draw.rect(surface, (0,0,0), (rotateX, rotateY, 50, 20), 0)
    pygame.draw.rect(surface, (255,255,255), (rotateX - 2, rotateY - 2, 54, 24), 2)
    surface.blit(fontobject.render("Left", 1, (255,255,255)), (rotateX + 7, rotateY + 5))
    if pygame.mouse.get_pressed()[0] == True and pressRotate == True:
        if (mousePosition[0] > rotateX and mousePosition[0] < rotateX + 50):
            if (mousePosition[1] > rotateY and mousePosition[1] < rotateY + 20):
                myAssam.face -= 1
                if myAssam.face % 4 == 0:
                    myAssam.face = 4
                else:
                    myAssam.face = myAssam.face % 4
                pressRotate = False
                pressDice = True

    rotateX = 80
    rotateY = 10
    pygame.draw.rect(surface, (0,0,0), (rotateX, rotateY, 60, 20), 0)
    pygame.draw.rect(surface, (255,255,255), (rotateX - 2, rotateY - 2, 64, 24), 2)
    surface.blit(fontobject.render("Straight", 1, (255,255,255)), (rotateX + 7, rotateY + 5))
    if pygame.mouse.get_pressed()[0] == True and pressRotate == True:
        if (mousePosition[0] > rotateX and mousePosition[0] < rotateX + 50):
            if (mousePosition[1] > rotateY and mousePosition[1] < rotateY + 20):
                pressDice = True
                pressRotate = False

    rotateX = 160
    rotateY = 10
    pygame.draw.rect(surface, (0,0,0), (rotateX, rotateY, 50, 20), 0)
    pygame.draw.rect(surface, (255,255,255), (rotateX - 2, rotateY - 2, 54, 24), 2)
    surface.blit(fontobject.render("Right", 1, (255,255,255)), (rotateX + 7, rotateY + 5))
    if pygame.mouse.get_pressed()[0] == True and pressRotate == True:
        if (mousePosition[0] > rotateX and mousePosition[0] < rotateX + 50):
            if (mousePosition[1] > rotateY and mousePosition[1] < rotateY + 20):
                myAssam.face += 1
                if myAssam.face % 4 == 0:
                    myAssam.face = 4
                else:
                    myAssam.face = myAssam.face % 4
                pressDice = True
                pressRotate = False

    diceX = 10
    diceY = 50
    pygame.draw.rect(surface, (0,0,0), (diceX, diceY, 50, 20), 0)
    pygame.draw.rect(surface, (255,255,255), (diceX - 2, diceY - 2, 54, 24), 2)
    surface.blit(fontobject.render("Dice!", 1, (255,255,255)), (diceX + 7, diceY + 5))
    for i in range (num):
        pygame.draw.circle(surface,(0,200,200),(diceX + 70 + i * 20, diceY + 9),7,0)
        pygame.draw.circle(surface,(255,255,255),(diceX + 70 + i * 20, diceY + 9),7,2)
    if pygame.mouse.get_pressed()[0] == True and pressDice == True:
        if (mousePosition[0] > diceX and mousePosition[0] < diceX + 50):
            if (mousePosition[1] > diceY and mousePosition[1] < diceY + 20):
                num = random.randrange(1,7)
                myAssam.move(num)
                pressRotate = True
                pressDice = False

    coinX = 250
    coinY = 580
    if (turn%4 == 0):
        pygame.draw.circle(surface, (255,222,0), (210,590), 20, 0)
        pygame.draw.circle(surface, (255,255,255), (210,590), 20, 2)
        pygame.draw.rect(surface, (0,0,0), (coinX, coinY, 60, 20), 0)
        pygame.draw.rect(surface, (255,255,255), (coinX - 2, coinY - 2, 64, 24), 2)
        surface.blit(fontobject.render("Coin: " + str(playerCoin[0]), 1, (255,255,255)), (coinX + 7, coinY + 5))
    if (turn%4 == 1):
        pygame.draw.circle(surface, (255,0,0), (210,590), 20, 0)
        pygame.draw.circle(surface, (255,255,255), (210,590), 20, 2)
        pygame.draw.rect(surface, (0,0,0), (coinX, coinY, 60, 20), 0)
        pygame.draw.rect(surface, (255,255,255), (coinX - 2, coinY - 2, 64, 24), 2)
        surface.blit(fontobject.render("Coin: " + str(playerCoin[1]), 1, (255,255,255)), (coinX + 7, coinY + 5))
    if (turn%4 == 2):
        pygame.draw.circle(surface, (0,255,0), (210,590), 20, 0)
        pygame.draw.circle(surface, (255,255,255), (210,590), 20, 2)
        pygame.draw.rect(surface, (0,0,0), (coinX, coinY, 60, 20), 0)
        pygame.draw.rect(surface, (255,255,255), (coinX - 2, coinY - 2, 64, 24), 2)
        surface.blit(fontobject.render("Coin: " + str(playerCoin[2]), 1, (255,255,255)), (coinX + 7, coinY + 5))
    if (turn%4 == 3):
        pygame.draw.circle(surface, (0,0,255), (210,590), 20, 0)
        pygame.draw.circle(surface, (255,255,255), (210,590), 20, 2)
        pygame.draw.rect(surface, (0,0,0), (coinX, coinY, 60, 20), 0)
        pygame.draw.rect(surface, (255,255,255), (coinX - 2, coinY - 2, 64, 24), 2)
        surface.blit(fontobject.render("Coin: " + str(playerCoin[3]), 1, (255,255,255)), (coinX + 7, coinY + 5))

    boxX = 10
    boxY = 90
    pygame.draw.rect(surface, (0,0,0), (boxX, boxY, 50, 20), 0)
    pygame.draw.rect(surface, (255,255,255), (boxX - 2, boxY - 2, 54, 24), 2)
    surface.blit(fontobject.render("Move", 1, (255,255,255)), (boxX + 7, boxY + 5))
    if pygame.mouse.get_pressed()[0] == True:
        if (mousePosition[0] > boxX and mousePosition[0] < boxX + 50):
            if (mousePosition[1] > boxY and mousePosition[1] < boxY + 20):
                box(surface, boxX + 60, boxY, turn)
                for i in range(1000001):
                    turn += 1

    quitgame()
    pygame.display.update()