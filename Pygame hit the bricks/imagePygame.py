import pygame
pygame.init()

window = pygame.display.set_mode((800, 540))
pygame.display.set_caption("Drawing a Smilly wheeeee")

canvas = pygame.Surface(window.get_size())
canvas = canvas.convert()
canvas.fill((255,255,255))

image = pygame.image.load("JULIA.jpg")
image.convert()
canvas.blit(image, (0,0)) # have to blit the image on the canvas first, then blit it canvas on the window... samge logic

font = pygame.font.SysFont("simhei", 24) # create font object first
text = font.render("JULIA boobs are gorgeous!", True, (0,0,255),(0,255,0))
canvas.blit(text, (500, 500))

window.blit(canvas, (0,0))

pygame.display.update()

quit=False
while not quit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit = True
pygame.quit()
