#pygame basics try out

import pygame
pygame.init() # as the name suggests'

screen = pygame.display.set_mode((800, 600)) # creating a screen window, takes in tuples for screen (length, width)

pygame.display.set_caption("Title of the Screen(Window or Program, whatever you call it)")

# things dont appear directly on the screen in pygame, it appears on a CANVAS, which Normally, ppl set the Canvas SIZE the SAME AS THE SCREEN SIZE
background = pygame.Surface(screen.get_size()) # Surface method creates a CANVAS
# the screen.get_size()   gets us the size of our created screen object so the CANVAS can FILL IT UP
background = background.convert() # make a sub-version of itself, to ACCELERATE the speed of the background DISPLAY
# so it wont lag...

background.fill((255,0,0)) # fill the canvas up with some kind of color

screen.blit(background, (0,0)) # using blit method to show the CANVAS background object on the screen object, starting from the (0,0) position to fill the whole screen up
pygame.display.update() # updates the CANVAS so it can SHOW the things that happened to it recently

# use a while loop to check if the user clicks on the "X" button to terminate the pygame program
def userQuit():
	quit = False
	while not quit: # the loop to keep the pygame program running (so the screen stays ON!)
		for event in pygame.event.get():# gets the event
			if event.type == pygame.QUIT:  # the "X" quit button
				quit = True
	pygame.quit()

#===========================
import pygame
pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Winow")

canvas = pygame.Surface(window.get_size())
canvas = canvas.convert()

canvas.fill((255,255,255))

window.blit(canvas, (0,0))
pygame.display.update()



quit = False
while not quit:
	# the part that keeps the window alive
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit = True
pygame.quit()
