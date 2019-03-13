import pygame, sys
from pygame.locals import *
from Gametools_exp import  Cell, Grid, Screen, Intro_screen, Game_over_screen

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


FPS = 10

pygame.init()
display = (500, 500)
#display = (1000,1000)
Surf = pygame.display.set_mode(display)


main_game = Grid(Surf)
Intro = Intro_screen(Surf)
Over = Game_over_screen(Surf)


def game():
	Winner_found = False
	Started = False
	Play_again = False
	Overed = False

	while True:

		Surf.fill(White)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()


		if not Started:
			Intro.show()
			Started = Intro.get_state()
			if Started:
				pygame.time.delay(300)

		else:
			if not Winner_found:
				main_game.show()
				Winner_found = main_game.Check_win()
				if Winner_found:
					Overed = True
					Play_again = False
			elif Overed and not Play_again:
				Over.show()
				Play_again = Over.get_state()
				if Play_again:
					Overed = False
					Winner_found = False
					main_game.Reset()
					pygame.time.delay(300)
			

		pygame.display.update()
		fpsclock.tick(FPS)

if __name__ == "__main__":
	game()
