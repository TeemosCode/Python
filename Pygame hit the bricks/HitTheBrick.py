import pygame, random, math, time

class Ball(pygame.sprite.Sprite):
	speedX = 0
	speedY = 0
	x = 0
	y = 0
	direction = 0
	speed = 0

	def __init__(self, sp, srx, sry ,radium, color):
		pygame.sprite.Sprite.__init__(self)
		self.speed = sp
		self.x = srx
		self.y = sry
		self.image = pygame.Surface([radium*2, radium*2])
		self.image.fill((255,255,255))
		pygame.draw.circle(self.image, color, (radium,radium), radium, 0)
		self.rect = self.image.get_rect()
		self.rect.center = (srx,sry)
		self.direction = random.randint(40, 70)


	def update(self):
		radian = math.radians(self.direction)
		self.speedX = self.speed * math.cos(radian)
		self.speedY = self.speed * math.sin(radian)
		self.x += self.speedX
		self.y += self.speedY
		self.rect.x = self.x
		self.rect.y = self.y
		if self.rect.left <= 0 or self.rect.right >= (screen.get_width()- 10):
			self.horizontalBounce()
		elif self.rect.top <= 10:
			self.rect.top = 15
			self.verticalBounce()

		if self.rect.bottom >= (screen.get_height()-10):
			# fell beneath the pad, gameover! dead!
			return True
		else:
			return False

	def verticalBounce(self):
		self.direction = 360 - self.direction
	def horizontalBounce(self):
		self.direction = (180 - self.direction) % 360

class Brick(pygame.sprite.Sprite):
	def __init__(self, color, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([38, 13]) # the size of the bircks are 38 X 13
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Pad(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		# ===============================
		self.image = pygame.Surface((60,10))
		self.image.fill((0,0,0))
		self.image.convert()
		# ================================
		self.rect = self.image.get_rect()
		self.rect.x = int((screen.get_width() - self.rect.width) / 2)
		self.rect.y = screen.get_height() - self.rect.height - 20

	def update(self):
		pos = pygame.mouse.get_pos()
		self.rect.x = pos[0]
		if self.rect.x > screen.get_width() - self.rect.width:
			self.rect.x = screen.get_width() - self.rect.width # dont let the pad move out of the border

def gameover(message):
	global running
	text = font1.render(message, 1 , (255,0,255))
	screen.blit(text, (screen.get_width()/2-100, screen.get_height()/2-20))
	pygame.display.update()
	time.sleep(3)
	running = False





pygame.init()
score = 0
font = pygame.font.SysFont("SimHei", 20)
font1 = pygame.font.SysFont("SimHei", 32)
#soundhit = pygame.mixer.Sound("media/hit.wav")
#soundpad = pygame.mixer.Sound("media/pad.wav")
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Hit The Brick Game")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
allsprite = pygame.sprite.Group()
bricks = pygame.sprite.Group()
ball = Ball(10, 300, 350, 10, (255,0,0))
allsprite.add(ball)
pad = Pad()
allsprite.add(pad)

clock = pygame.time.Clock()
for row in range(4):
	for col in range(15):
		if row == 0 or row == 1:
			brick = Brick((0,255,0), col * 40 + 1, row * 15 + 1)
		if row == 2 or row == 3:
			brick = Brick((0,0,255), col * 40 + 1, row * 15 + 1)
		bricks.add(brick)
		allsprite.add(brick)
msgstr = "Press the Mouse to Begin!"
playing = False
running = True


while running:
	clock.tick(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	buttons =  pygame.mouse.get_pressed()
	if buttons[0]:
		playing = True

	if playing == True:
		screen.blit(background, (0,0))
		fail = ball.update()
		if fail:
			gameover("GameOver!")
		pad.update()

		hitbrick = pygame.sprite.spritecollide(ball, bricks, True) # if hit, delete the hit object in the sprite group
		if len(hitbrick) > 0:
			score += len(hitbrick)
	    	#soundhit.play()
			ball.rect.y += 20
			ball.verticalBounce()
			if len(bricks) == 0:
				gameover("Congratualtions, you WON!")

		hitpad = pygame.sprite.collide_rect(ball, pad)
		if hitpad:
			#soundpad.play()
			ball.verticalBounce()
		allsprite.draw(screen)
		msgstr = "Score: " + str(score)
	msg = font.render(msgstr, 1 , (255,0,255))
	screen.blit(msg, ((screen.get_width())/2-60, screen.get_height()-20))
	pygame.display.update()
pygame.quit()