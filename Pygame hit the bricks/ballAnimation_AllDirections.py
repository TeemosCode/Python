import pygame, random, math
pygame.init()

screen = pygame.display.set_mode((640,320))
pygame.display.set_caption("Ball Animation All Directions")

canvas = pygame.Surface(screen.get_size())
canvas = canvas.convert()
canvas.fill((255,255,255))
#create the ball canvas
ball = pygame.Surface((30,30)) ####!!!!!!!
ball.fill((255,255,255))
pygame.draw.circle(ball, (0,0,255), (15,15), 15, 0) # draw the ball
rect = ball.get_rect() # get the rectangular area of the ball cnavas
rect.center = (320, 160) # where to first place the ball canvas on the whole big canvas
x, y = rect.topleft  # the topleft coordinates of the ball

# give it random starting angle
direction = random.randint(20, 70) 
radianAngle = math.radians(direction) # turn it to radians cause the sin and cos takes in radians
speedX = 5 * math.cos(radianAngle) # set the speed in the middle to 5
speedY = 5 * math.sin(radianAngle) # these are the x and y vertex of the speed
# because on a computer, going up means to be minusing the y cordinate, so we give speedY a "-5"!

clock = pygame.time.Clock()

quit = False
while not quit:
	clock.tick(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit = True

	screen.blit(canvas, (0,0))
	x += speedX # change horizontal speed
	y += speedY # change vertical speed
	rect.center = (x, y)
	if rect.left <= 0 or rect.right >= screen.get_width():
	    # if ball reaches horizontal edges
	    speedX *= -1 # change its speed direction
	elif rect.top <= 5 or rect.bottom >= screen.get_height() - 5: 
		#if ball reaches horizontal edges
		speedY *= -1 # same thing, change the speed direction
	screen.blit(ball, rect.topleft)
	pygame.display.update()
pygame.quit()


