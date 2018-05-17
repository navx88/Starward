import pygame
import math
import random

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
transColor = pink

class bolt(pygame.sprite.Sprite):
	def __init__(self):
	    """ Graphic Sprite Constructor. """
	 
	    # Call the parent class (Sprite) constructor
	    super(Mercerite,self).__init__()
	 
	    # Load the image
	    self.image = pygame.image.load("bolt.png").convert()

	    self.rect = self.image.get_rect()
	 
	    # Set our transparent color
	    #self.image.set_colorkey(WHITE)

class Mercerite(pygame.sprite.Sprite):

	def __init__(self):
	    """ Graphic Sprite Constructor. """
	 
	    # Call the parent class (Sprite) constructor
	    super(Mercerite,self).__init__()
	 
	    # Load the image
	    self.image = pygame.image.load("Mercerite.png").convert()
	    self.image.set_colorkey(transColor)
	    self.size = 64

	    self.rect = self.image.get_rect()
	    self.hitbox = pygame.Rect(16,16,32,32)
	    self.hitbox_width = 32

	    self.cooldown_timer = 60 # def is 60, final is 15
	    self.cooldown = 0
	    self.hp = 4 # def is 4, final is 24
	    self.hp_max = 4
	    self.dmg = 1 # def is 1, final is 4
	    self.speed = 1 # def is 1, final is 4
	    self.bolt_speed = 3 # def is 3, final is 6
	 
	    # Set our transparent color
	    #self.image.set_colorkey(WHITE)

	def recalibrate(self):
		self.hitbox = (self.rect[0]+16, self.rect[1]+16)

	def set_healthbar(self):
		return pygame.Rect(0,624,27*self.hp,16)

	def set_healthbar_max(self):
		return pygame.Rect(0,624,27*self.hp_max,16)

class enemy_mercerite(pygame.sprite.Sprite):

	def __init__(self):
		""" Graphic Sprite Constructor. """

		# Call the parent class (Sprite) constructor
		super(enemy_mercerite,self).__init__()

		# Load the image
		self.image = pygame.image.load("enemy_kerra.png").convert()
		self.image.set_colorkey(transColor)
		self.image.convert_alpha()
		self.rect = self.image.get_rect()
		self.size = 64

		self.hp = 3
		self.dmg = 1
		self.speed = 1
		self.bolt_speed = 3

		self.spawn_counter_max = 500
		self.direction_counter_max = 100
		self.attack_counter_max = 100

		self.spawn_counter = 0
		self.direction_counter = 0
		self.attack_counter = 0

		self.direction = 0

		self.hitbox = pygame.Rect(16,16,32,32)
		self.hitbox_width = 32

		self.fire1_rect = (self.rect[0]+10,self.rect[1]+56)
		self.fire2_rect = (self.rect[0]+50,self.rect[1]+56)

		self.cannon_locations = []
		self.cannon_locations.append(self.fire1_rect)
		self.cannon_locations.append(self.fire2_rect)

	def recalibrate(self):
		self.hitbox = (self.rect[0]+16, self.rect[1]+16)
		self.cannon_locations[0] = (self.rect[0]+10,self.rect[1]+56)
		self.cannon_locations[1] = (self.rect[0]+50,self.rect[1]+56)

	def spawn(self):
		return enemy_mercerite()

class enemy_mercerite_dmged1(pygame.sprite.Sprite):

	def __init__(self):
		""" Graphic Sprite Constructor. """

		# Call the parent class (Sprite) constructor
		super(enemy_mercerite_dmged1,self).__init__()

		# Load the image
		self.image = pygame.image.load("enemy_mercerite_dmged1.png").convert()
		self.image.set_colorkey(transColor)
		self.image.convert_alpha()
		self.rect = self.image.get_rect()
		self.size = 64

		self.hp = 3
		self.dmg = 1
		self.speed = 1
		self.bolt_speed = 2

		self.spawn_counter_max = 1022
		self.direction_counter_max = 25
		self.attack_counter_max = 122

		self.spawn_counter = 0
		self.direction_counter = 0
		self.attack_counter = 0

		self.direction = 0

		self.hitbox = pygame.Rect(16,16,32,32)
		self.hitbox_width = 32

		self.fire1_rect = (self.rect[0]+10,self.rect[1]+56)
		self.fire2_rect = (self.rect[0]+50,self.rect[1]+56)

		self.cannon_locations = []
		self.cannon_locations.append(self.fire1_rect)
		self.cannon_locations.append(self.fire2_rect)

	def recalibrate(self):
		self.hitbox = (self.rect[0]+16, self.rect[1]+16)
		self.cannon_locations[0] = (self.rect[0]+10,self.rect[1]+56)
		self.cannon_locations[1] = (self.rect[0]+50,self.rect[1]+56)

	def spawn(self):
		return enemy_mercerite_dmged1()

class enemy_mercerite_dmged2(pygame.sprite.Sprite):

	def __init__(self):
		""" Graphic Sprite Constructor. """

		# Call the parent class (Sprite) constructor
		super(enemy_mercerite_dmged2,self).__init__()

		# Load the image
		self.image = pygame.image.load("enemy_mercerite_dmged2.png").convert()
		self.image.set_colorkey(transColor)
		self.image.convert_alpha()
		self.rect = self.image.get_rect()
		self.size = 64

		self.hp = 2
		self.dmg = 1
		self.speed = 1
		self.bolt_speed = 2

		self.spawn_counter_max = 622
		self.direction_counter_max = 50
		self.attack_counter_max = 322

		self.spawn_counter = 0
		self.direction_counter = 0
		self.attack_counter = 0

		self.direction = 0

		self.hitbox = pygame.Rect(16,16,32,32)
		self.hitbox_width = 32

		self.fire1_rect = (self.rect[0]+10,self.rect[1]+56)
		self.fire2_rect = (self.rect[0]+50,self.rect[1]+56)

		self.cannon_locations = []
		self.cannon_locations.append(self.fire1_rect)
		self.cannon_locations.append(self.fire2_rect)

	def recalibrate(self):
		self.hitbox = (self.rect[0]+16, self.rect[1]+16)
		self.cannon_locations[0] = (self.rect[0]+10,self.rect[1]+56)
		self.cannon_locations[1] = (self.rect[0]+50,self.rect[1]+56)

	def spawn(self):
		return enemy_mercerite_dmged2()

class enemy_mercerite_dmged3(pygame.sprite.Sprite):

	def __init__(self):
		""" Graphic Sprite Constructor. """

		# Call the parent class (Sprite) constructor
		super(enemy_mercerite_dmged3,self).__init__()

		# Load the image
		self.image = pygame.image.load("enemy_mercerite_dmged3.png").convert()
		self.image.set_colorkey(transColor)
		self.image.convert_alpha()
		self.rect = self.image.get_rect()
		self.size = 64

		self.hp = 1
		self.dmg = 1
		self.speed = 1
		self.bolt_speed = 2

		self.spawn_counter_max = 322
		self.direction_counter_max = 100
		self.attack_counter_max = 622

		self.spawn_counter = 0
		self.direction_counter = 0
		self.attack_counter = 0

		self.direction = 0

		self.hitbox = pygame.Rect(16,16,32,32)
		self.hitbox_width = 32

		self.fire1_rect = (self.rect[0]+10,self.rect[1]+56)
		self.fire2_rect = (self.rect[0]+50,self.rect[1]+56)

		self.cannon_locations = []
		self.cannon_locations.append(self.fire1_rect)
		self.cannon_locations.append(self.fire2_rect)

	def recalibrate(self):
		self.hitbox = (self.rect[0]+16, self.rect[1]+16)
		self.cannon_locations[0] = (self.rect[0]+10,self.rect[1]+56)
		self.cannon_locations[1] = (self.rect[0]+50,self.rect[1]+56)

	def spawn(self):
		return enemy_mercerite_dmged3()

class bolt(pygame.sprite.Sprite):

	def __init__(self):
	    """ Graphic Sprite Constructor. """
	 
	    # Call the parent class (Sprite) constructor
	    super(bolt,self).__init__()
	 
	    # Load the image
	    self.image = pygame.image.load("bolt.png").convert()
	    self.rect = self.image.get_rect()
	    self.hitbox = pygame.Rect(0,0,4,4)
	    self.speed = 2

	def recalibrate(self):
		self.hitbox = (self.rect[0], self.rect[1])