import sprites
import pygame, sys, random 
from pygame.locals import *

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

def scroll_background(screen, screen_size, bg_1, bg_2, bg_y):
	screen.blit(bg_1, (0,bg_y))
	screen.blit(bg_2, (0,bg_y-screen_size))

	bg_y += 1
	if bg_y == screen_size:
		bg_y = 0

def draw_healthbar(screen, player):
	pygame.draw.rect(screen, red, player.set_healthbar(), 0)
	pygame.draw.rect(screen, blue, player.set_healthbar_max() ,2)

def draw_player_hitbox(screen, player):

	point_size = 4

	pygame.draw.rect(screen, green, (player.hitbox[0],player.hitbox[1],point_size,point_size), 0)
	pygame.draw.rect(screen, green, (player.hitbox[0]+player.hitbox_width-point_size,player.hitbox[1],point_size,point_size), 0)
	pygame.draw.rect(screen, green, (player.hitbox[0]+player.hitbox_width-point_size,player.hitbox[1]+player.hitbox_width+point_size,point_size,point_size), 0)
	pygame.draw.rect(screen, green, (player.hitbox[0],player.hitbox[1]+player.hitbox_width+point_size,point_size,point_size), 0)