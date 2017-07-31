import pygame
pygame.init()
#adding in keyboard events (pygame.key.get_pressed())
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

playing = False
running = True
while running:
	clock.tick(30) # happens 30 times each SECOND
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	# wipe out the screen so the new stuff could be put on to make it like individual pictures moving real fast to show an animation effect
	
	"""the keyboard events""" #can't eat anything, might be because of the OS
	'''
	keys = pygame.key.get_pressed()# returns a list of all buttons status "Booleans"
	if keys[pygame.K_SPACE] and rect.right < window.get_width(): # the 'a' button key and still within the window right border
		x += speed
		
	elif keys[pygame.K_LSHIFT] and rect.left > 0:
		x -= speed
	rect.center = (x,y)
	'''
	"""==================="""
	"""Mouse Events"""
	buttons = pygame.mouse.get_pressed()# list with 3 elements, index 0, 1 ,2 : left, scroller, left mouse buttons
	if buttons[0]:
		#left click
		playing = True
	elif buttons[1]:
		#right click
		playing = False
	if playing == True:
		mouses = pygame.mouse.get_pos()
		#returns a list of the x, y coordinates of the mouse when clicked
		x = mouses[0]
		y = mouses[1]
		rect.center = (x,y)
	"""============"""
	
	window.blit(canvas, (0,0))
	window.blit(ball, rect.topleft)
	pygame.display.update()
pygame.quit()