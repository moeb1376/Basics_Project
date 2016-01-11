import pygame, sys, pygame.font, pygame.draw, string, random
from pygame.locals import *
import pygame.event as GAME_EVENTS

pygame.init()


num = -1
windowWidth = 650
windowHeight = 650
BoardList = [[None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None],
             [None,None,"Y","R","G","B",None],
             [None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None]]

surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Marrakech Board!')

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
def box(screen,boxX,boxY):
  print ask(screen, boxX, boxY, "")
def quitGame():
    pygame.quit()
    sys.exit()
def Board(x,y,cell):
    for i in range(y,y+8*cell,cell):
        pygame.draw.line(surface,(255,255,255),(y,i),(y+7*cell,i),True)
    for i in range(x,x+8*cell,cell):
        pygame.draw.line(surface,(255,255,255),(i,x),(i,x+7*cell),True)
def BoardCells(screen,list):
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

while True:

    surface.fill((0,0,0))
    pygame.draw.rect(surface,(100,100,100),(0,0,windowWidth,windowHeight))
    mousePosition = pygame.mouse.get_pos()

    BoardCells(surface,BoardList)
    Board(150,150,50)

    diceX = 10
    diceY = 50
    fontobject = pygame.font.Font(None,18)
    pygame.draw.rect(surface, (0,0,0), (diceX, diceY, 50, 20), 0)
    pygame.draw.rect(surface, (255,255,255), (diceX - 2, diceY - 2, 54, 24), 2)
    surface.blit(fontobject.render("Dice!", 1, (255,255,255)), (diceX + 7, diceY + 5))
    for i in range (num+1):
        pygame.draw.circle(surface,(0,200,200),(diceX + 70 + i * 20, diceY + 9),7,0)
    if pygame.mouse.get_pressed()[0] == True:
        if (mousePosition[0] > diceX and mousePosition[0] < diceX + 50):
            if (mousePosition[1] > diceY and mousePosition[1] < diceY + 20):
                num = random.randrange(0,6)

    boxX = 10
    boxY = 10
    pygame.draw.rect(surface, (0,0,0), (boxX, boxY, 50, 20), 0)
    pygame.draw.rect(surface, (255,255,255), (boxX - 2, boxY - 2, 54, 24), 2)
    surface.blit(fontobject.render("Move", 1, (255,255,255)), (boxX + 7, boxY + 5))
    if pygame.mouse.get_pressed()[0] == True:
        if (mousePosition[0] > boxX and mousePosition[0] < boxX + 50):
            if (mousePosition[1] > boxY and mousePosition[1] < boxY + 20):
                box(surface, boxX + 60, boxY)


    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitGame()
        if event.type == QUIT:
            quitGame()

    pygame.display.update()