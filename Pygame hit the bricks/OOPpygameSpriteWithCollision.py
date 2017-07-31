import pygame, math, random

class Ball(pygame.sprite.Sprite):
	# cause we using speed and cordinates on all methods in the Ball object, so we make them the Balls' attributes
	speedX = 0
	speedY = 0 #ball speed
	x = 0
	y = 0 # ball coordinates

	def __init__(self, speed, srx, sry, radium, color):
		pygame.sprite.Sprite.__init__(self)
		self.x = srx
		self.y = sry
		#creating the ball magic
		self.image = pygame.Surface([radium*2, radium*2]) # creating ball canvas
		self.image.fill((255,255,255))
		pygame.draw.circle(self.image, color, (radium,radium), radium, 0)
		self.rect = self.image.get_rect() # getting the balls zone
		self.rect.center = (srx, sry) # where to put the ball canvas on the actual window canvas
		#ball stuff
		direction = random.randint(20, 70)# moving angle
		radian = math.radians(direction) # degree to radian
		self.speedX = speed * math.cos(radian) # horizontal speed
		self.speedY = -speed * math.sin(radian) # horizontal speed (moving upwards with a '-' negative sign)

	# for changing the ball status
	def update(self):
		self.x += self.speedX
		self.y += self.speedY
		self.rect.x = self.x # updating
		self.rect.y = self.y

		if self.rect.left <= 0 or self.rect.right >= screen.get_width():
			self.speedX *= -1
		elif self.rect.top <= 5 or self.rect.bottom >= (screen.get_height() - 5):
			self.speedY *= -1
	####For COLLISION!!!
	def collidebounce(self):
		self.speedX *= -1  # bounce em back from the x condinate vector


# in order to draw objects on canvas in pygame, we need to put all objects into the sprite.Group() first with add()
sprites = pygame.sprite.Group() # creating sprite group for objects
ball_1 = Ball(8, 100, 100, 20, (0,0,255))# instantiate a ball object with ...... blablabla
sprites.add(ball_1) # add the ball_1 into sprite group
ball_2 = Ball(6, 200, 250, 20, (255,255,0))
sprites.add(ball_2)

screen = pygame.display.set_mode((640, 320))
pygame.display.set_caption("OOP Sprite Animation")

canvas = pygame.Surface(screen.get_size())
canvas.fill((255,255,255))

clock = pygame.time.Clock()

quit = False
while not quit:
	clock.tick(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit = True

	screen.blit(canvas, (0,0))
	
	ball_1.update() # update the objects with their own update() method
	ball_2.update()

	sprites.draw(screen) # use sprite Group's .draw() method to draw the objects in the group on the designated window
	#!!!!Collision
	result = pygame.sprite.collide_rect(ball_1, ball_2) # the api of collision in pygame sprite.collide_rect(obj1, obj2)
	# the method returns "Boolean" value to see if the objects collide or not
	if result == True: # if collided, returns True, so then we use the our Ball method .collidebounce()
		ball_1.collidebounce()
		ball_2.collidebounce()
	#Collision!!!
	pygame.display.update()
pygame.quit()