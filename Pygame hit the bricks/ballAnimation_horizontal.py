import pygame
pygame.init()

window = pygame.display.set_mode((640, 320))
pygame.display.set_caption("Animation")

canvas = pygame.Surface(window.get_size())
canvas.fill((255,255,255))

ball = pygame.Surface((30,30))
ball.fill((255,255,255))
pygame.draw.circle(ball, (0,0,255), (15,15), 15, 0) # draw the ball
rect = ball.get_rect() # get the rectangular area of the ball cnavas
rect.center = (320, 45) # # where to first place the ball canvas on the whole big canvas
x, y = rect.topleft  # the topleft coordinates of the ball
speed = 3 # the movement speed, the larger the number the faster it runs (or changes its coordinates), but puts more pressure on the CPU
clock = pygame.time.Clock() # the clock object to set animations in pygame
running = True
while running:
	clock.tick(30) # happens 30 times each SECOND
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	window.blit(canvas, (0,0)) # wipe out the screen so the new stuff could be put on to make it like individual pictures moving real fast to show an animation effect
	
	x += speed  # adding speed to the x-axis of the ball (changing x-axis to make it look like its moving)
	rect.center = (x,y) # recenter the ball
	if rect.left <= 0 or rect.right >= window.get_width(): # if the ball reaches the very left or very right of the screen borders
		speed *= -1 # make speed the oposite of itself (means its going the over way)
	window.blit(ball, rect.topleft)
	pygame.display.update()
pygame.quit()




