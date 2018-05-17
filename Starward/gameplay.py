import pygame, sys
from pygame.locals import *
import logic
import sprites
import ip
import gui

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

debug = True

def loop(screen, background, screen_size, sprite_size, clk, player, roster):

	all_sprites_list = pygame.sprite.Group() # group for all in-game sprites
	player_bolt_sprites_list = pygame.sprite.Group() # group for player projectiles
	enemy_bolt_sprites_list = pygame.sprite.Group() # group for enemy projectiles
	enemy_list = pygame.sprite.Group() # group for enemy sprites

	bg_1 = pygame.image.load(background).convert()
	bg_2 = pygame.image.load(background).convert()
	bg_y = 0

	all_sprites_list.add(player)

	player.rect = (screen_size/2 - sprite_size/2 , screen_size - sprite_size) # set player start location


	crash = False

	while not crash:

		#gui.scroll_background(screen, screen_size, bg_1, bg_2, bg_y) # fix pls
		screen.blit(bg_1, (0,bg_y))
		screen.blit(bg_2, (0,bg_y-screen_size))

		bg_y += 1
		if bg_y == screen_size:
			bg_y = 0

		gui.draw_healthbar(screen, player)

		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			crash = True 

		all_sprites_list.draw(screen)

		#spawn_mercerite = 180
		#logic.ai_spawn_mercerite(pygame.time, spawn_mercerite, enemy_list, all_sprites_list) # here is where we do the spawn stuff
		logic.ai_spawn(screen_size, roster, enemy_list, all_sprites_list)

		keys=pygame.key.get_pressed()

		ip.check_arrows(keys, player)
		ip.check_space(keys,player, all_sprites_list, player_bolt_sprites_list)
		#pygame.draw.rect(screen,green,player.hitbox,0)

		gui.draw_player_hitbox(screen, player)

		#print(event)

		logic.bolts_remove(all_sprites_list, player_bolt_sprites_list, enemy_bolt_sprites_list, screen_size)
		logic.bolts_move(player_bolt_sprites_list, enemy_bolt_sprites_list)

		# cooldown lowers
		if player.cooldown > 0:
			player.cooldown = player.cooldown-1

		for enemy in enemy_list:
			logic.ai_movement(enemy)
			logic.ai_attack(enemy,enemy_bolt_sprites_list, all_sprites_list)
			for bolt in player_bolt_sprites_list:
				if logic.check_sprite_vs_bolt(enemy, bolt):
					if enemy.hp > 1:
						enemy.hp = enemy.hp - player.dmg
						player_bolt_sprites_list.remove(bolt)
						all_sprites_list.remove(bolt)
					else:
						enemy_list.remove(enemy)
						player_bolt_sprites_list.remove(bolt)
						all_sprites_list.remove(enemy)
						all_sprites_list.remove(bolt)

		for bolt in enemy_bolt_sprites_list:
			if logic.check_sprite_vs_bolt(player, bolt):
				if player.hp > 1:
					player.hp = player.hp - enemy.dmg
					print(player.hp)
					enemy_bolt_sprites_list.remove(bolt)
					all_sprites_list.remove(bolt)
				else:
					enemy_bolt_sprites_list.remove(bolt)
					all_sprites_list.remove(bolt)
					print("YOU ARE LOSE!!!")
					crash = True

		pygame.display.update()

		#pygame.display.update()
		#pygame.display.flip()
		clk.tick(60)	