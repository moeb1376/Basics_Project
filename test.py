import pygame, sys, pygame.font, pygame.draw, string, random
from pygame.locals import *
import pygame.event as GAME_EVENTS

pygame.init()

pressRotate = True
pressDice = True
pressMove = True
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
<<<<<<< HEAD
f = open("LOG.txt","w")
f.close()
=======
>>>>>>> 2a6c472eb5c86de2a3837b66eb178965fabf1883

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
  coordinate1 = (int(carpet1[1]) - 1, int(carpet1[0]) - 1)
  coordinate2 = (int(carpet2[1]) - 1, int(carpet2[0]) - 1)
  return (coordinate1,coordinate2)
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
def get_child(x, y):
    answer = []
    if -1 < x - 1 < 7:
        answer.append((x - 1, y))
    if -1 < x + 1 < 7:
        answer.append((x + 1, y))
    if -1 < y - 1 < 7:
        answer.append((x, y - 1))
    if -1 < y + 1 < 7:
        answer.append((x, y + 1))
    return answer
def dfs(myBoard, assamX, assamY, color, checkList=[[0 for i in range(7)] for i in range(7)]):
    if myBoard.get_detail_XY(assamX, assamY).get_color() != color or checkList[assamX][assamY] == 1:
        checkList[assamX][assamY] = 1
        return 0
    childs = get_child(assamX, assamY)
    hel = 0
    for i in childs:
        hel += checkList[i[0]][i[1]]
    if hel == 4:
        return 1
    answer = 0
    checkList[assamX][assamY] = 1
    for i in childs:
        if isinstance(myBoard.get_detail_XY(i[0] , i[1]) , carpet):
            answer += dfs(myBoard, i[0], i[1], color, checkList)
    return answer + 1
def find_player(playersList, color):
    for i in range (len(playersList)):
        if playersList[i].get_color() == color:
            return i
<<<<<<< HEAD
def LOG(iterable, *myString):
    myFile = open("LOG.txt" , 'a')
    answer = ""
    for i in myString:
        answer += str(i) + iterable
    answer += "\n"
    myFile.write(answer)
    myFile.close()

=======
>>>>>>> 2a6c472eb5c86de2a3837b66eb178965fabf1883

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
                if list[j][i] == 0:
                    continue
                elif list[j][i].get_color() == "Y":
                    pygame.draw.rect(screen,(255,222,0),(150 + i*50, 150 + j*50, 50, 50))
                elif list[j][i].get_color() == "R":
                    pygame.draw.rect(screen,(255,0,0),(150 + i*50, 150 + j*50, 50, 50))
                elif list[j][i].get_color() == "G":
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
    def get_neighbor(self):
        answer = []
        for i in range(-1,2):
            for j in range(-1,2):
                if -1<self.x + i <7 and -1<self.y + j<7:
                    answer.append((self.x + i , self.y + j))
        answer.remove((self.x,self.y))
        return answer
    def get_coordinate(self):
        return (self.x, self.y)

    def get_coordinate(self):
        return (self.x, self.y)

    def __str__(self):
        return 'assam . x : ' + str(self.x) + ' / assam . y : ' + str(self.y) + ' / assam . face : ' + str(self.face)
class carpet:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def get_color(self):
        return self.color

    def __str__(self):
        return self.color + "  " + str(self.number)

    def __eq__(self, other):
        if not isinstance(other, carpet):
            return False
        return ((self.color == other.color) and (self.number == other.number))
class player:
    def __init__(self, colorCarpet, numberCarpets, rgb, coin=30):
        self.color = colorCarpet
        self.playerCarpet = [carpet(colorCarpet, i) for i in range(numberCarpets)]
        self.coin = coin
        self.rgb = rgb
    def get_player_carpet(self):
        hel = self.playerCarpet[0]
        self.playerCarpet.remove(self.playerCarpet[0])
        return hel

    def get_rgb(self):
        return self.rgb

    def get_color(self):
        return self.color

    def set_coin(self, coin):
        self.coin = coin

    def get_coin(self):
        return self.coin
class board:
    def __init__(self, numberPlayers, detail=[[0 for i in range(7)] for i in range(7)], gameTurn=0, gameRound=0):
        self.numberPlayers = numberPlayers
        self.detail = detail
        self.gameTurn = gameTurn
        self.gameRound = gameRound

    def get_number_carpets(self):
        if (self.numberPlayers == 4):
            return 12
        else:
            return 15

    def get_detail_XY(self, y, x):
        return self.detail[x][y]

    def get_turn(self):
        return self.gameTurn

    def get_round(self):
        return self.gameRound

    def set_turn(self):
        if self.gameTurn == 3:
            self.gameTurn = 0
            self.gameRound += 1
        else:
            self.gameTurn += 1

    def check_correct_move(self, myAssam, coordinate1, coordinate2, myPlayer):
        flag = False
        assamCoordinate = myAssam.get_coordinate()
<<<<<<< HEAD
        helCoordinate = myAssam.get_neighbor()
        for i in helCoordinate:
            LOG("______" , '        ' , "i : " , i , "cor 1 , 2 : ",coordinate1,coordinate2)
            if coordinate1 == i or coordinate2 == i:
                flag = True
                break
        if flag:
            if self.detail[coordinate1[1]][coordinate1[0]] == 0 or self.detail[coordinate2[1]][coordinate2[0]] == 0:
                flag = True
            elif self.detail[coordinate1[1]][coordinate1[0]] == self.detail[coordinate2[1]][coordinate2[0]]:
                if myPlayer.get_color() == self.detail[coordinate1[1]][coordinate1[0]].get_color():
=======
        if (abs(assamCoordinate[0] - coordinate1[0]) <= 1 or abs(assamCoordinate[1] - coordinate1[1]) <= 1) and (
                abs(assamCoordinate[0] - coordinate2[0]) <= 1 or abs(assamCoordinate[1] - coordinate2[1]) <= 1):
            if self.detail[coordinate1[0]][coordinate1[1]] == 0 or self.detail[coordinate2[0]][coordinate2[1]] == 0:
                flag = True
            elif self.detail[coordinate1[0]][coordinate1[1]] == self.detail[coordinate2[0]][coordinate2[1]]:
                if myPlayer.get_color() == self.detail[coordinate1[0]][coordinate1[1]].get_color():
>>>>>>> 2a6c472eb5c86de2a3837b66eb178965fabf1883
                    flag = True
                else:
                    flag = False
            else:
                flag = True
<<<<<<< HEAD
        LOG(" ",'flag : ',flag)
        LOG(" ","assamcoordinate : ",assamCoordinate)
        LOG(" ","coordinate 1 o 2 : ",coordinate1,coordinate2)
        LOG(" ","detail 1 : " , self.detail[coordinate1[1]][coordinate1[0]])
        LOG(" ","detail 2 : " , self.detail[coordinate2[1]][coordinate2[0]])
        for i in range(7):
            for j in range(7):
                print self.detail[j][i],
            print
        for i in range(7):
            for j in range(7):
                if self.detail[j][i] != 0:
                    print (j,i)
            print
        print 20*"*"
=======
        else:
            flag = False
>>>>>>> 2a6c472eb5c86de2a3837b66eb178965fabf1883
        if flag:
            helCarpet = myPlayer.get_player_carpet()
            self.detail[coordinate1[1]][coordinate1[0]] = helCarpet
            self.detail[coordinate2[1]][coordinate2[0]] = helCarpet
        return flag

AssamMove(surface,pos,windowWidth/2,windowHeight/2)
gameBoard = board(4)
numberCarpets = gameBoard.get_number_carpets()
myAssam = assam()
playerList = [player('Y', numberCarpets, (255,222,0)), player('R', numberCarpets, (255,0,0)), player('G', numberCarpets, (0,255,0)), player('B', numberCarpets, (0,0,255))]

while gameBoard.get_round() < numberCarpets:
    surface.fill((0,0,0))
    pygame.draw.rect(surface,(100,100,100),(0,0,windowWidth,windowHeight))
    mousePosition = pygame.mouse.get_pos()
    fontobject = pygame.font.Font(None,18)

    MarrakechBoard = ShowBoard()
    ShowBoard.borders(MarrakechBoard,surface,boardX,boardY,cell)
    ShowBoard.cells(MarrakechBoard,surface,gameBoard.detail)
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
                pressDice = False
                pressMove = True
                assamCoordinate = myAssam.get_coordinate()
                turnPlayer = gameBoard.get_turn()
                assamCell = gameBoard.get_detail_XY(assamCoordinate[0], assamCoordinate[1])
                if isinstance(assamCell, carpet):
                    assamCellColor = assamCell.get_color()
                    coin = dfs(gameBoard, assamCoordinate[0], assamCoordinate[1], assamCellColor)
                    targetPlayer = find_player(playerList, assamCellColor)
                    playerList[turnPlayer].set_coin(playerList[turnPlayer].get_coin() - coin)
                    playerList[targetPlayer].set_coin(playerList[targetPlayer].get_coin() + coin)


    pygame.draw.rect(surface, (0,0,0), (540, 110, 63, 20), 0)
    pygame.draw.rect(surface, (255,255,255), (538, 108, 67, 24), 2)
    surface.blit(fontobject.render("Round: " + str(gameBoard.get_round() + 1), 1, (255,255,255)), (544, 115))
    pygame.draw.circle(surface, playerList[gameBoard.get_turn()].get_rgb(), (570,65), 30, 0)
    pygame.draw.circle(surface, (255,255,255), (570,65), 30, 2)

    coinX = 100
    coinY = 600
    pygame.draw.rect(surface, (0,0,0), (coinX, coinY, 100, 20), 0)
    pygame.draw.rect(surface, (255,255,255), (coinX - 2, coinY - 2, 104, 24), 2)
    surface.blit(fontobject.render("Yellow Coin: " + str(playerList[0].get_coin()), 1, (255,255,255)), (coinX + 4, coinY + 5))
    pygame.draw.rect(surface, (0,0,0), (coinX + 120, coinY, 100, 20), 0)
    pygame.draw.rect(surface, (255,255,255), (coinX  + 120 - 2, coinY - 2, 104, 24), 2)
    surface.blit(fontobject.render("Red Coin: " + str(playerList[1].get_coin()), 1, (255,255,255)), (coinX  + 120 + 4, coinY + 5))
    pygame.draw.rect(surface, (0,0,0), (coinX + 240, coinY, 100, 20), 0)
    pygame.draw.rect(surface, (255,255,255), (coinX  + 240 - 2, coinY - 2, 104, 24), 2)
    surface.blit(fontobject.render("Green Coin: " + str(playerList[2].get_coin()), 1, (255,255,255)), (coinX  + 240 + 4, coinY + 5))
    pygame.draw.rect(surface, (0,0,0), (coinX + 360, coinY, 100, 20), 0)
    pygame.draw.rect(surface, (255,255,255), (coinX  + 360 - 2, coinY - 2, 104, 24), 2)
    surface.blit(fontobject.render("Blue Coin: " + str(playerList[3].get_coin()), 1, (255,255,255)), (coinX  + 360 + 4, coinY + 5))

    boxX = 10
    boxY = 90
    pygame.draw.rect(surface, (0,0,0), (boxX, boxY, 50, 20), 0)
    pygame.draw.rect(surface, (255,255,255), (boxX - 2, boxY - 2, 54, 24), 2)
    surface.blit(fontobject.render("Move", 1, (255,255,255)), (boxX + 7, boxY + 5))
    if pygame.mouse.get_pressed()[0] == True and pressMove == True:
        if (mousePosition[0] > boxX and mousePosition[0] < boxX + 50):
            if (mousePosition[1] > boxY and mousePosition[1] < boxY + 20):
                coordinate = box(surface, boxX + 60, boxY, turn)
                pressMove = False
                pressRotate = True
                while not gameBoard.check_correct_move(myAssam, coordinate[0], coordinate[1], playerList[gameBoard.get_turn()]):
                    coordinate = box(surface, boxX + 60, boxY, turn)
                gameBoard.set_turn()
                turn += 1

    quitgame()
    pygame.display.update()