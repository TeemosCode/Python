import pygame
pygame.init()

window = pygame.display.set_mode((640, 320))
pygame.display.set_caption("Drawing a Smilly wheeeee")

canvas = pygame.Surface(window.get_size())
canvas = canvas.convert()
canvas.fill((255,255,255))

pygame.draw.circle(canvas, (0,0,0), (150,150), 130, 4)
pygame.draw.circle(canvas, (0,0,255), (100,120), 25, 0)# 0: means a filled up shape, no width of the lines
pygame.draw.circle(canvas, (0,0,255), (200,120), 25, 0)
pygame.draw.ellipse(canvas, (255,0,255),[135,130,20, 80], 0)
pygame.draw.arc(canvas, (255,0,0), [80,130,150,120],3.4, 6.1, 9)


window.blit(canvas, (0,0)) # draw the FINAL CANVAS on for it to show
pygame.display.update()

quit=False
while not quit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit = True
pygame.quit()


