import pygame, sys
from pygame.locals import *
from Gametools import  Cell, Grid, Screen

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


FPS = 20

pygame.init()
display = (500, 500)
#display = (1000,1000)
Surf = pygame.display.set_mode(display)

main_grid = Grid(Surf)
Finished = Screen(Surf)
Winner = False

def game():

	while True:

		Surf.fill(White)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		
		Winner_found = main_grid.Check_win()

		if Winner_found:
			Finished.show()
		else:
			main_grid.show()
		

		pygame.display.update()
		fpsclock.tick(FPS)

if __name__ == "__main__":
	game()
