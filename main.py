import pygame, sys
from pygame.locals import *
from Gametools_exp import  Cell,Grid

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

winner = None

# class Grid:
# 	def __init__(self):
# 		self.Top, self.Left = 5, 5
# 		self.Width = 351
# 		self.Hieght = 489
# 		self.Bottom = self.Top + self.Hieght 
# 		self.Right = self.Left + self.Width

# 		self.grid_dimension_cell = 3

# 		self.cell_width =  self.Width//self.grid_dimension_cell
# 		self.cell_hieght = self.Hieght//self.grid_dimension_cell

# 		self.cells = [Cell(self.Top*i + self.cell_width * i, self.Left*j + self.cell_hieght * j, self.cell_width, self.cell_hieght, 5) for j in range(self.grid_dimension_cell) for i in range(self.grid_dimension_cell)]

		
# 		self.Buttons = [Cell(self.Right + 20, 250, 60, 30, text = "RESET"), Cell(self.Right + 20, 280, 60, 30, text= "QUIT")]

# 		self.commands = {
# 						"RESET": self.Reset,
# 						"QUIT" : self.Quit
# 						}

# 		self.cells += self.Buttons

# 		self.cell_values = [i.text for  i in self.cells[:-2]]

# 		self.moves = {"_X_": "_O_", "_O_":"_X_"}
# 		self.next_move = "_O_"

# 		self.winner = ""


# 	def Reset(self):
# 		for cell in self.cells[:-2]:
# 			cell.clicked = False
# 			cell.text = ""
		

# 	def Quit(self):
# 		pygame.quit()
# 		sys.exit()


# 	def Check_win(self):
# 		win_values = [(1,2,3),
# 					  (1,4,7),
# 					  (1,5,9),
# 					  (2,5,8),
# 					  (3,6,9),
# 					  (3,5,7),
# 					  (4,5,6),
# 					  (7,8,9)]
# 		#print(self.cell_values)

# 		for value in win_values:
# 			c1, c2, c3 = value
# 			if_anyone_present = (self.cell_values[c1-1] or self.cell_values[c2-1] or self.cell_values[c3-1])
# 			if_all_equal = (self.cell_values[c1-1] == self.cell_values[c2-1] and  self.cell_values[c2-1] == self.cell_values[c3-1])
# 			if if_anyone_present and if_all_equal:
# 				return(self.cell_values[c1-1])#+" WON")
# 			# 	self.winner = "X"#self.cell_values[c1-1]
# 			# else:
# 			# 	self.winner = ""



# 	def update(self):
# 		for i,cell in enumerate(self.cells):
# 			mousex,mousey = pygame.mouse.get_pos()

# 			if not cell.clicked and (cell.left < mousex < cell.left + cell.width) and (cell.top < mousey < cell.top + cell.hieght):
# 				cell.color = LIGHT_BLUE

# 				if Right_click:
# 					if cell.text == "" and not cell.clicked:
# 						self.next_move = self.moves[self.next_move]
# 						cell.text = self.next_move
# 						cell.clicked = True

# 					elif cell.text:
# 						self.commands[cell.text]()
					
# 					#print(cell.text)

# 			elif cell.clicked:
# 				cell.color = LIGHT_BLUE
# 			else:
# 				cell.color = DARK_BLUE



# 	def show(self):
# 		self.update()

# 		for i,cell in enumerate(self.cells):
# 			cell.show_cell()

# 		self.cell_values = [i.text for  i in self.cells[:-2]]

		#print(self.cell_values)
		# self.Check_win()
		# print(self.winner)
		# if x:
		# 	print(x+" won.", "Yo")


class Screen:
	def __init__(self):
		self.Play_again = Cell(Surf, 120, 250, 200, 30, text = "Play")#, clickable = True)
		self.QUIT = Cell(Surf, 250, 250, 60, 30, text= "QUIT")#, clickable = True)

		self.cells = [self.Play_again, self.QUIT]

	def show(self):
		for i,cell in enumerate(self.cells):
			cell.show_cell()




def game():
	main_grid = Grid(Surf)
	Finished = Screen()

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

		
		Winner = main_grid.Check_win()
		if Winner:
			Finished.show()
		else:
			main_grid.show()
		

		pygame.display.update()
		fpsclock.tick(FPS)

if __name__ == "__main__":
	game()
