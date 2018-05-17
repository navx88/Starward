import pygame
import game
import sprites

def check_arrows(keys, player):

	if keys[pygame.K_LEFT] and player.rect[0] > 0:
		player.rect = (player.rect[0]-player.speed,player.rect[1])
	if keys[pygame.K_RIGHT] and player.rect[0] < 576:
		player.rect = (player.rect[0]+player.speed,player.rect[1])
	if keys[pygame.K_UP] and player.rect[1] > 0:
		player.rect = (player.rect[0],player.rect[1]-player.speed)
	if keys[pygame.K_DOWN] and player.rect[1] < 576:
		player.rect = (player.rect[0],player.rect[1]+player.speed)

	player.recalibrate()
	


def check_space(keys,player, all_sprites_list, player_bolt_sprites_list):
	if keys[pygame.K_SPACE]:
		if player.cooldown == 0:
			# set cooldown of cannons
			player.cooldown = player.cooldown_timer
			# create the two bolts
			bolt1 = sprites.bolt()
			bolt2 = sprites.bolt()
			bolt1.speed = player.bolt_speed
			bolt2.speed = player.bolt_speed
			# set bolt locations
			bolt1.rect = (player.rect[0]+10,player.rect[1]+4)
			bolt2.rect = (player.rect[0]+50,player.rect[1]+4)
			# add bolts to all sprites group
			all_sprites_list.add(bolt1)
			all_sprites_list.add(bolt2)
			# add bolts to bolts list for player
			player_bolt_sprites_list.add(bolt1)
			player_bolt_sprites_list.add(bolt2)