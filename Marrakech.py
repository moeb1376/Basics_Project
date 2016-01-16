#This folder for all class and function
class assam :
	def __init__(self , face = 1 , x = 3 , y = 3):
		self.face = face
		self.x = x
		self.y = y
	def move(self , dice):
		if self.face == 1:
			hel = self.x + dice
			if self.y != 0:
				self.x = hel - (hel - 6 + hel % 7 ) * int(hel > 6)
				self.y += (-1)**(self.y+1) * (hel // 7)
				self.face += 2 * (hel // 7)
			else:
				self.x = hel - (hel % 7 + 1) * (hel // 7)
				self.y += (hel % 7 ) * (hel // 7)
				self.face += 3 * (hel // 7)
		elif self.face == 2:
			hel = self.y - dice
			if self.x != 6:
				self.y = (2 * abs(hel) + hel/abs(hel) -1) / 2
				self.x += (-1) ** (self.x) * int(hel < 0)
				self.face += 2 * int(hel < 0)
			else:
				self.y = hel * int(hel > 0)
				self.x = 6 + (hel+1) * int(hel < 0)
				self.face += int(hel < 0)
		elif self.face == 3:
			hel = self.x - dice
			if self.y != 6:
				self.x = (2 * abs(hel) + hel/abs(hel) -1) / 2
				self.y += (-1) ** (self.y) * int(hel < 0)
				self.face -= 2 * int(hel < 0)
			else:
				self.x = hel * int(hel > 0)
				self.y = 6 + (hel+1) * int(hel < 0)
				self.face -= int(hel < 0)
		else:
			hel = self.y + dice
			if self.x != 0:
				self.y = hel - (hel - 6 + hel % 7 ) * int(hel > 6)
				self.x += (-1)**(self.x+1) * (hel // 7)
				self.face -= 2 * (hel // 7)
			else:
				self.y = hel - (hel % 7 + 1) * (hel // 7)
				self.x += (hel % 7 ) * (hel // 7)
				self.face -= 3 * (hel // 7)
	def __str__(self):
		return 'assam . x : ' + str(self.x) + ' / assam . y : ' + str(self.y) + ' / assam . face : ' + str(self.face)

class player:
	def __init__(self , colorCarpet , numberCarpets):
		self . playerCarpet = [carpet(colorCarpet , i) for i in range(numberCarpets)]
class board:
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
class carpet:
	def __init__(self , color ,number):
		self.color = color
		self.number = number
myAssam = assam(4,0,2)
myAssam.move(6)
print myAssam