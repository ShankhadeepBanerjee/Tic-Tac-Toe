#This is a Script containing tools for Tic-tac-toe Game

import pygame, sys
from pygame.locals import *

# global Surf, BLUE, DARK_BLUE, LIGHT_BLUE, GREEN ,White, Black, Right_click, mousex, mousey

# Right_click = False
# mousex,mousey = (False,False)

# fpsclock = pygame.time.Clock()
Black = (0,0,0)
White = (255,255,255)
LIGHT_BLUE = (5,5,255)
DARK_BLUE = (5,5,155)
BLUE = (0,0,255)
GREEN = (0,255,0)


# FPS = 50

# pygame.init()
# display = (500, 500)
# # #display = (1000,1000)
# Surf = pygame.display.set_mode(display)


class Cell:
	#global Right_click

	def __init__(self, Surface, left, top, width, hieght, border = 1, text = "", clickable = False):
		self.Surface = Surface
		self.top = top
		self.left = left
		self.text = text
		self.width = width
		self.hieght = hieght
		self.right = self.left + self.width
		self.bottom = self.top + self.hieght
		self.border = border
		self.clicked = False
		self.color = DARK_BLUE
		self.clickable = clickable


	def symbol_x(self, left, top):
		pygame.draw.line(self.Surface, White, (left+20,top+20), (left+100,top+140), 10)
		pygame.draw.line(self.Surface, White, (left+20,top+140), (left+100,top+20), 10)

	def symbol_o(self, left, top, cell_width, cell_hieght):
		center = (left+cell_width//2,top+cell_hieght//2)
		radius = cell_width//2 - 5
		pygame.draw.circle(self.Surface, White, center, radius, 10)

	def check_if_clicked_or_hovered(self):
		mousex,mousey = pygame.mouse.get_pos()

		if (self.left < mousex < self.left + self.width) and (self.top < mousey < self.top + self.hieght):
			self.color = LIGHT_BLUE
			if self.clicked and self.text == "":# and not self.clicked:
				self.text = "_X_"
				self.clicked = True
		else:
			self.color = DARK_BLUE


	def show_cell(self):

		self.check_if_clicked_or_hovered()
		
		if self.clickable:
			mousex,mousey = pygame.mouse.get_pos()


			pygame.draw.rect(self.Surface, self.color, (self.left, self.top, self.width, self.hieght))
		
			if self.text == "_X_":
				self.symbol_x(self.left, self.top)
			elif self.text == "_O_":
				self.symbol_o(self.left, self.top, self.width, self.hieght)
			elif self.text == "":
				pass
			else:
				fontObj = pygame.font.Font("ariali.ttf", 25)#self.hieght)
				textObj = fontObj.render(self.text, True, White) 
				textRectObj = textObj.get_rect()                 
				textRectObj.topleft = (self.left+10, self.top+2)                      
				self.Surface.blit(textObj,textRectObj)
				self.width = 100


			pygame.draw.rect(self.Surface, BLUE, (self.left, self.top, self.width, self.hieght), self.border)

		else:
			pygame.draw.rect(self.Surface, self.color, (self.left, self.top, self.width, self.hieght))
			
			if self.text == "_X_":
				self.symbol_x(self.left, self.top)
			elif self.text == "_O_":
				self.symbol_o(self.left, self.top, self.width, self.hieght)
			elif self.text == "":
				pass
			else:
				fontObj = pygame.font.Font("ariali.ttf", 25)#self.hieght)
				textObj = fontObj.render(self.text, True, White) 
				textRectObj = textObj.get_rect()                 
				textRectObj.topleft = (self.left+10, self.top+2)                      
				self.Surface.blit(textObj,textRectObj)
				self.width = 100


			pygame.draw.rect(self.Surface, BLUE, (self.left, self.top, self.width, self.hieght), self.border)

class Grid:
	#global Right_click
	def __init__(self, Surface):#, Right_click): #This
		self.Surface = Surface
		self.Right_click = Right_click
		self.Top, self.Left = 5, 5
		self.Width = 351
		self.Hieght = 489
		self.Bottom = self.Top + self.Hieght 
		self.Right = self.Left + self.Width

		self.grid_dimension_cell = 3

		self.cell_width =  self.Width//self.grid_dimension_cell
		self.cell_hieght = self.Hieght//self.grid_dimension_cell

		self.cells = [Cell(self.Surface, self.Top*i + self.cell_width * i, self.Left*j + self.cell_hieght * j, self.cell_width, self.cell_hieght, 5) for j in range(self.grid_dimension_cell) for i in range(self.grid_dimension_cell)]

		
		self.Buttons = [Cell(self.Surface, self.Right + 20, 250, 60, 30, text = "RESET"), Cell(self.Surface, self.Right + 20, 280, 60, 30, text= "QUIT")]

		self.commands = {
						"RESET": self.Reset,
						"QUIT" : self.Quit
						}

		self.cells += self.Buttons

		self.cell_values = [i.text for  i in self.cells[:-2]]

		self.moves = {"_X_": "_O_", "_O_":"_X_"}
		self.next_move = "_O_"

		self.winner = ""


	def Reset(self):
		for cell in self.cells[:-2]:
			cell.clicked = False
			cell.text = ""
		

	def Quit(self):
		pygame.quit()
		sys.exit()


	def Check_win(self):
		win_values = [(1,2,3),
					  (1,4,7),
					  (1,5,9),
					  (2,5,8),
					  (3,6,9),
					  (3,5,7),
					  (4,5,6),
					  (7,8,9)]
		#print(self.cell_values)

		for value in win_values:
			c1, c2, c3 = value
			if_anyone_present = (self.cell_values[c1-1] or self.cell_values[c2-1] or self.cell_values[c3-1])
			if_all_equal = (self.cell_values[c1-1] == self.cell_values[c2-1] and  self.cell_values[c2-1] == self.cell_values[c3-1])
			if if_anyone_present and if_all_equal:
				return(self.cell_values[c1-1])#+" WON")
			# 	self.winner = "X"#self.cell_values[c1-1]
			# else:
			# 	self.winner = ""



	def update(self):
		for i,cell in enumerate(self.cells):
			mousex,mousey = pygame.mouse.get_pos()

			if not cell.clicked and (cell.left < mousex < cell.left + cell.width) and (cell.top < mousey < cell.top + cell.hieght):
				cell.color = LIGHT_BLUE

				if cell.clicked:
					if cell.text == "":
						self.next_move = self.moves[self.next_move]
						cell.text = self.next_move
						cell.clicked = True

					elif cell.text:
						self.commands[cell.text]()
					
					#print(cell.text)

			elif cell.clicked:
				cell.color = LIGHT_BLUE
			else:
				cell.color = DARK_BLUE



	def show(self):
		self.update()

		for i,cell in enumerate(self.cells):
			cell.show_cell()

		self.cell_values = [i.text for  i in self.cells[:-2]]




def game():
	global Surf, BLUE, DARK_BLUE, LIGHT_BLUE, GREEN ,White, Black, Right_click, mousex, mousey

	Right_click = False
	mousex,mousey = (False,False)

	fpsclock = pygame.time.Clock()
	Black = (0,0,0)
	White = (255,255,255)
	LIGHT_BLUE = (5,5,255)
	DARK_BLUE = (5,5,155)
	BLUE = (0,0,255)
	GREEN = (0,255,0)


	FPS = 50

	pygame.init()
	display = (500, 500)
	#display = (1000,1000)
	Surf = pygame.display.set_mode(display)


	main_grid = Grid(Surf)
	# Finished = Screen()

	c1 = Cell(Surf, 50, 100, 100, 30, border = 1, text = "Yes", clickable = True)
	c2 = Cell(Surf, 100, 200, 100, 30, border = 1, text = "", clickable = True)
	c3 = Cell(Surf, 50, 150, 100, 30, border = 1, text = "No", clickable = True)

	winner = None
	

	while True:
		Right_click = False

		Surf.fill(White)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					Right_click = True
					mousex,mousey = pygame.mouse.get_pos()

		#mousex,mousey = pygame.mouse.get_pos()

		# c1.show_cell()
		# c2.show_cell()
		# c3.show_cell()
		main_grid.show()

		
		# Winner = main_grid.Check_win()
		# if Winner:
		# 	Finished.show()
		# 	#break
		# 	#Finished.show()

		# 	# print(Winner+" WON")
		# 	# break
		# else:
		# 	main_grid.show()
		# 	#Finished.show()
		# #print(main_grid.winner)
		

		pygame.display.update()
		fpsclock.tick(FPS)

if __name__ == "__main__":
	game()