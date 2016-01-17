#This folder for all class and function
class assam :
	def __init__(self , face = 1 , x = 3 , y = 3):
		self.face = face
		self.x = x
		self.y = y
	def move(self , dice):
		if self.face == 1:
			hel = self.x + dice
			if self.y != 6:
				self.x = hel - (hel - 6 + hel % 7 ) * int(hel > 6)
				self.y += (-1)**(self.y) * (hel // 7)
				self.face += 2 * (hel // 7)
			else:
				self.x = hel - (hel % 7 + 1) * (hel // 7)
				self.y -= (hel % 7 ) * (hel // 7)
				self.face += 3 * (hel // 7)
		elif self.face == 4:
			hel = self.y - dice
			if self.x != 0:
				self.y = hel - (2*hel + 1) * int(hel < 0)
				self.x += (-1) ** (self.x + 1) * int(hel < 0)
				self.face -= 2 * int(hel < 0)
			else:
				self.y = hel * int(hel > 0)
				self.x = (-1) * (hel+1) * int(hel < 0)
				self.face -= 3 * int(hel < 0)
		elif self.face == 3:
			hel = self.x - dice
			if self.y != 0:
				self.x =  hel - (2*hel + 1) * int(hel < 0)
				self.y += (-1) ** (self.y + 1) * int(hel < 0)
				self.face -= 2 * int(hel < 0)
			else:
				self.x = hel * int(hel > 0)
				self.y = (-1) * (hel+1) * int(hel < 0)
				self.face -= int(hel < 0)
		else:
			hel = self.y + dice
			if self.x != 6:
				self.y = hel - (hel - 6 + hel % 7 ) * int(hel > 6)
				self.x += (-1)**(self.x) * (hel // 7)
				self.face += 2 * (hel // 7)
			else:
				self.y = hel - (hel % 7 + 1) * (hel // 7)
				self.x -= (hel % 7 ) * (hel // 7)
				self.face += (hel // 7)
	def __str__(self):
		return 'assam . x : ' + str(self.x) + ' / assam . y : ' + str(self.y) + ' / assam . face : ' + str(self.face)



class carpet:
	def __init__(self , color ,number):
		self.color = color
		self.number = number
	def __str__(self):
		return self.color +  "  " + str(self.number)
	def __eq__(self, other):
		return ((self.color == other.color) and (self.number == other.number))


class player:
	def __init__(self , colorCarpet , numberCarpets):
		self . playerCarpet = [carpet(colorCarpet , i) for i in range(numberCarpets)]
	def get_player_carpet(self):
		hel = self.playerCarpet[0]
		self.playerCarpet.remove(0)
		return hel


class board:
	turn = 0
	round = 0
	def __init__(self , numberPlayers , detail = [[0 for i in range(7)] for i in range(7)]):
		self.numberPlayers = numberPlayers
		self.detail = detail
	def get_number_carpets(self):
		if (self.numberPlayers == 4):
			return 12
		else:
			return 15
	def get_detail_XY(self , x , y):
		return self.detail[x][y]
	def set_turn(self):
		if self.turn == 3:
			self.turn = 0
			self.round +=1
		else:
			self.turn += 1


myAssam = assam(1,2,6)
myAssam.move(3)
print myAssam