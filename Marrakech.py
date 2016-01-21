# This folder for all class and function
from PIL.ImImagePlugin import number


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
    def __init__(self, colorCarpet, numberCarpets, coin=30):
        self.color = colorCarpet
        self.playerCarpet = [carpet(colorCarpet, i) for i in range(numberCarpets)]
        self.coin = coin

    def get_player_carpet(self):
        hel = self.playerCarpet[0]
        self.playerCarpet.remove(self.playerCarpet[0])
        return hel

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

    def get_detail_XY(self, x, y):
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
        if (abs(assamCoordinate[0] - coordinate1[0]) <= 1 or abs(assamCoordinate[1] - coordinate1[1]) <= 1) and (
                abs(assamCoordinate[0] - coordinate2[0]) <= 1 or abs(assamCoordinate[1] - coordinate2[1]) <= 1):
            if self.detail[coordinate1[0]][coordinate1[1]] == 0 or self.detail[coordinate2[0]][coordinate2[1]] == 0:
                flag = True
            elif self.detail[coordinate1[0]][coordinate1[1]] == self.detail[coordinate2[0]][coordinate2[1]]:
                if myPlayer.get_color() == self.detail[coordinate1[0]][coordinate1[1]].get_color():
                    flag = True
                else:
                    flag = False
            else:
                flag = True
        else:
            flag = False
        if flag:
            helCarpet = myPlayer.get_player_carpet()
            self.detail[coordinate1[0]][coordinate1[1]] = helCarpet
            self.detail[coordinate2[0]][coordinate2[1]] = helCarpet
        return flag


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
        answer += dfs(myBoard, i[0], i[1], color, checkList)
    return answer + 1


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


def find_player(playersList, color):
    for i in len(playersList):
        if playersList[i].get_color() == color:
            return i


myList = [[0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0]]
gameBoard = board(4)
numberCarpets = gameBoard.get_number_carpets()
myAssam = assam()
playerList = [player('green', numberCarpets), player('blue', numberCarpets), player('red', numberCarpets),
              player('yellow', numberCarpets)]
while gameBoard.get_round() < numberCarpets:
    dice = input("dice : ")
    myAssam.move(dice)
    coordinate1 = input("coordinate1 : ")
    coordinate2 = input("coordinate2 : ")
    while not gameBoard.check_correct_move(myAssam, coordinate1, coordinate2, playerList[gameBoard.get_turn()]):
        print "incorrect coordination !"
        coordinate1 = input("coordinate1 : ")
        coordinate2 = input("coordinate2 : ")
    assamCoordinate = myAssam.get_coordinate()
    turnPlayer = gameBoard.get_turn()
    assamCell = gameBoard.get_detail_XY(assamCoordinate[0], assamCoordinate[1])
    if isinstance(assamCell, carpet):
        assamCellColor = assamCell.get_color()
    coin = dfs(gameBoard, assamCoordinate[0], assamCoordinate[1], assamCellColor)
    targetPlayer = find_player(playerList, assamCellColor)
    playerList[turnPlayer].set_coin(playerList[turnPlayer].get_coin() - coin)
    playerList[targetPlayer].set_coin(playerList[targetPlayer].get_coin() + coin)
    gameBoard.set_turn()
