import pygame, sys
from pygame.locals import *




class Cell:

	def __init__(self, left, top, width, hieght, border = 1, text = ""):
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

	def symbol_x(self, left, top):
		pygame.draw.line(Surf, White, (left+20,top+20), (left+100,top+140), 10)
		pygame.draw.line(Surf, White, (left+20,top+140), (left+100,top+20), 10)

	def symbol_o(self, left, top, cell_width, cell_hieght):
		center = (left+cell_width//2,top+cell_hieght//2)
		radius = cell_width//2 - 5
		pygame.draw.circle(Surf, White, center, radius, 10)



	def show_cell(self):
		# mousex,mousey = pygame.mouse.get_pos()

		# if (self.left < mousex < self.left + self.width) and (self.top < mousey < self.top + self.hieght):
		# 	color = LIGHT_BLUE
		# 	if Right_click and self.text == "" and not self.clicked:
		# 		self.text = "_X_"
		# 		self.clicked = True
		# 	 	#Right_click = False
		# else:
		# 	color = DARK_BLUE

		

		pygame.draw.rect(Surf, self.color, (self.left, self.top, self.width, self.hieght))
		
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
			Surf.blit(textObj,textRectObj)
			self.width = 100


		pygame.draw.rect(Surf, BLUE, (self.left, self.top, self.width, self.hieght), self.border)



class Grid:
	def __init__(self):
		self.Top, self.Left = 5, 5
		self.Width = 351
		self.Hieght = 489
		self.Bottom = self.Top + self.Hieght 
		self.Right = self.Left + self.Width

		self.grid_dimension_cell = 3

		self.cell_width =  self.Width//self.grid_dimension_cell
		self.cell_hieght = self.Hieght//self.grid_dimension_cell

		self.cells = [Cell(self.Top*i + self.cell_width * i, self.Left*j + self.cell_hieght * j, self.cell_width, self.cell_hieght, 5) for j in range(self.grid_dimension_cell) for i in range(self.grid_dimension_cell)]

		
		self.Buttons = [Cell(self.Right + 20, 250, 60, 30, text = "RESET"), Cell(self.Right + 20, 280, 60, 30, text= "QUIT")]

		self.commands = {
						"RESET": self.Reset,
						"QUIT" : self.Quit
						}

		self.cells += self.Buttons

		self.moves = {"_X_": "_O_", "_O_":"_X_"}
		self.next_move = "_O_"


	def Reset(self):
		for cell in self.cells[:-2]:
			cell.text = ""
			cell.clicked = False
		

	def Quit(self):
		pygame.quit()
		sys.exit()

	def update(self):
		for i,cell in enumerate(self.cells):
			mousex,mousey = pygame.mouse.get_pos()

			if not cell.clicked and (cell.left < mousex < cell.left + cell.width) and (cell.top < mousey < cell.top + cell.hieght):
				cell.color = LIGHT_BLUE

				if Right_click:
					if cell.text == "" and not cell.clicked:
						self.next_move = self.moves[self.next_move]
						cell.text = self.next_move
						cell.clicked = True
					# elif cell.text == "RESET":
					# 	self.Reset()
					# elif cell.text == "QUIT":
					# 	self.Quit()
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


	main_grid = Grid()
	

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

		main_grid.show()
		

		pygame.display.update()
		fpsclock.tick(FPS)

if __name__ == "__main__":
	game()
