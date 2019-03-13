#This is a Script containing tools for Tic-tac-toe Game

import pygame, sys
from pygame.locals import *


Black = (0,0,0)
White = (255,255,255)
LIGHT_BLUE = (5,5,255)
DARK_BLUE = (5,5,155)
BLUE = (0,0,255)
GREEN = (0,255,0)




class Cell:

	def __init__(self, Surface, left, top, width, hieght, border = 1, text = ""):
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
		self.color_in = DARK_BLUE
		self.color_out = LIGHT_BLUE

		if self.text in ("_X_", "_O_", ""):
			self.isButton = False
		else:
			self.isButton = True


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
			self.color_in = LIGHT_BLUE
			if not self.isButton and not self.clicked:
				self.clicked = pygame.mouse.get_pressed()[0]
				

			elif self.isButton:
				self.clicked = pygame.mouse.get_pressed()[0]
				if self.clicked and self.text == "QUIT":
					pygame.quit()
					sys.exit()
				# if self.clicked:
				# 	print("Yes")
				
		else:
			self.color_in = DARK_BLUE

	def show(self):
		self.check_if_clicked_or_hovered()

		pygame.draw.rect(self.Surface, self.color_in, (self.left, self.top, self.width, self.hieght))
			
		if self.text == "_X_":
			self.symbol_x(self.left, self.top)
		elif self.text == "_O_":
			self.symbol_o(self.left, self.top, self.width, self.hieght)
		elif self.text == "":
			pass
		else:
			fontObj = pygame.font.Font("ariali.ttf", 25)
			textObj = fontObj.render(self.text, True, White) 
			textRectObj = textObj.get_rect()                 
			textRectObj.topleft = (self.left+10, self.top+2)                      
			self.Surface.blit(textObj,textRectObj)
			#self.width = 100


		pygame.draw.rect(self.Surface, self.color_out, (self.left, self.top, self.width, self.hieght), self.border)
		
		
class Grid:
	def __init__(self, Surface):
		self.Surface = Surface
		self.Top, self.Left = 5, 5
		self.Width = 351
		self.Hieght = 489
		self.Bottom = self.Top + self.Hieght 
		self.Right = self.Left + self.Width

		self.grid_dimension_cell = 3

		self.cell_width =  self.Width//self.grid_dimension_cell
		self.cell_hieght = self.Hieght//self.grid_dimension_cell

		self.cells = [Cell(self.Surface, self.Top*i + self.cell_width * i, self.Left*j + self.cell_hieght * j, self.cell_width, self.cell_hieght, 5) for j in range(self.grid_dimension_cell) for i in range(self.grid_dimension_cell)]

		
		self.Buttons = [Cell(self.Surface, self.Right + 20, 250, 100, 30, text = "RESET"), Cell(self.Surface, self.Right + 20, 280, 100, 30, text= "QUIT")]

		self.commands = {
						"RESET": self.Reset,
						"QUIT" : self.Quit
						}

		self.cells += self.Buttons

		self.cell_values = [i.text for  i in self.cells[:-2]]

		self.moves = {"_X_": "_O_", "_O_":"_X_"}
		self.next_move = "_O_"



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
		

		for value in win_values:
			c1, c2, c3 = value
			
			if_anyone_present = (self.cell_values[c1-1] or self.cell_values[c2-1] or self.cell_values[c3-1])

			if_all_equal = (self.cell_values[c1-1] == self.cell_values[c2-1] and  self.cell_values[c2-1] == self.cell_values[c3-1])
			if if_anyone_present and if_all_equal:
				#self.Reset()
				return(self.cell_values[c1-1])



	def update(self):
		for i,cell in enumerate(self.cells):
			if cell.clicked and not cell.isButton:
				if not cell.text:
					self.next_move = self.moves[self.next_move]
					cell.text = self.next_move
					
				else:
					pass
			elif cell.clicked and cell.isButton: 
				self.commands[cell.text]()





	def show(self):
		
		self.update()

		for i,cell in enumerate(self.cells):
			cell.show()

		self.cell_values = [i.text for  i in self.cells[:-2]]




# Play_again = Cell(Surf, 120, 250, 200, 30, text = "Play")
# QUIT = Cell(Surf, 250, 250, 60, 30, text= "QUIT")


class Screen(object):
	def __init__(self,Surf):
		self.Surf = Surf

		self.cells = []


	def Quit(self):
		pygame.quit()
		sys.exit()
		
	def show(self):
		for i,cell in enumerate(self.cells):
			# if cell.text == "QUIT" and cell.clicked:
			# 	self.Quit()
			cell.show()
			# if cell.clicked:
			# 	print(self.commands[cell.text])


class Intro_screen(Screen):

	def __init__(self, Surface):
		super().__init__(Surface)
		self.Play = Cell(self.Surf, 100, 250, 130, 30, text = "Play")
		self.QUIT = Cell(self.Surf, 250, 250, 80, 30, text= "QUIT")
		self.cells = [self.Play, self.QUIT]

	def get_state(self):
		if self.Play.clicked:
			self.Play.clicked = False
			return (True)
		else:
			return(False)


class Game_over_screen(Screen):

	def __init__(self, Surface):
		super().__init__(Surface)
		self.Play_again = Cell(self.Surf, 100, 250, 130, 30, text = "Play again")
		self.QUIT = Cell(self.Surf, 250, 250, 80, 30, text= "QUIT")
		self.cells = [self.Play_again, self.QUIT]
		

	def get_state(self):
		if self.Play_again.clicked:
			self.Play_again.clicked = False
			return (True)
		else:
			return(False)




	



"""For Testing Purposes"""


# def game():
# 	global Surf, BLUE, DARK_BLUE, LIGHT_BLUE, GREEN ,White, Black, Right_click, mousex, mousey

# 	Right_click = False
# 	mousex,mousey = (False,False)

# 	fpsclock = pygame.time.Clock()
# 	Black = (0,0,0)
# 	White = (255,255,255)
# 	LIGHT_BLUE = (5,5,255)
# 	DARK_BLUE = (5,5,155)
# 	BLUE = (0,0,255)
# 	GREEN = (0,255,0)


# 	FPS = 30

# 	pygame.init()
# 	display = (500, 500)
# 	#display = (1000,1000)
# 	Surf = pygame.display.set_mode(display)


# 	# main_grid = Grid()
# 	# Finished = Screen()

# 	c1 = Cell(Surf, 50, 100, 100, 30, border = 1, text = "Yes")#, clickable = True)
# 	c2 = Cell(Surf, 100, 200, 100, 30, border = 1, text = "")#, clickable = True)
# 	c3 = Cell(Surf, 50, 150, 100, 30, border = 1, text = "No")#, clickable = True)

# 	main = Grid(Surf)

# 	winner = None
	

# 	while True:
# 		Surf.fill(White)
# 		for event in pygame.event.get():
# 			if event.type == pygame.QUIT:
# 				pygame.quit()
# 				sys.exit()

# 			elif event.type == pygame.MOUSEBUTTONDOWN:
# 				if event.button == 1:
# 					mousex,mousey = pygame.mouse.get_pos()

# 		# c1.show_cell()
# 		# c2.show_cell()
# 		# c3.show_cell()
# 		main.show()

# 		pygame.display.update()
# 		fpsclock.tick(FPS)

# # if __name__ == "__main__":
# # 	game()