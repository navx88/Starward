import sprites
import pygame, sys, random 
from pygame.locals import *

random.seed(17)
global move_counter 
global move_counter_max 
global rand_num 

move_counter = 0
move_counter_max = 60
rand_num = 0

def check_sprite_vs_bolt(sprite, bolt):
	
	if bolt.rect[0] >= sprite.hitbox[0] and bolt.rect[0] <= sprite.hitbox[0]+sprite.hitbox_width and bolt.rect[1] >= sprite.hitbox[1] and bolt.rect[1] < sprite.hitbox[1]+sprite.hitbox_width:
		return True

def bolts_move(player_bolt_sprites_list, enemy_bolt_sprites_list):

	for bolt in player_bolt_sprites_list:
		bolt.rect = (bolt.rect[0],bolt.rect[1]-bolt.speed)
		bolt.recalibrate()

	for bolt in enemy_bolt_sprites_list:
		bolt.rect = (bolt.rect[0],bolt.rect[1]+bolt.speed)
		bolt.recalibrate()

def bolts_remove(all_sprites_list , player_bolt_sprites_list, enemy_bolt_sprites_list, screen_size):

	for bolt in player_bolt_sprites_list:
		if bolt.rect[1] < 0:
			player_bolt_sprites_list.remove(bolt)
			all_sprites_list.remove(bolt)

	for bolt in enemy_bolt_sprites_list:
		if bolt.rect[1] > screen_size:
			enemy_bolt_sprites_list.remove(bolt)
			all_sprites_list.remove(bolt)

def ai_movement(sprite): 

	if sprite.direction_counter == sprite.direction_counter_max:
		sprite.direction = random.randint(0,3)
		sprite.direction_counter = 0
	else:
		sprite.direction_counter += 1

	if sprite.direction==0 and sprite.rect[0] > 0:
		sprite.rect = (sprite.rect[0]-sprite.speed,sprite.rect[1])
	if sprite.direction==1 and sprite.rect[0] < 576:
		sprite.rect = (sprite.rect[0]+sprite.speed,sprite.rect[1])
	if sprite.direction==2 and sprite.rect[1] > 0:
		sprite.rect = (sprite.rect[0],sprite.rect[1]-sprite.speed)
	if sprite.direction==3 and sprite.rect[1] < 576:
		sprite.rect = (sprite.rect[0],sprite.rect[1]+sprite.speed)

	sprite.recalibrate()

def ai_attack(sprite, enemy_bolt_sprites_list, all_sprites_list): # rehaul (be more automagic)

	if sprite.attack_counter == sprite.attack_counter_max:
		for cannon in sprite.cannon_locations:
			bolt = sprites.bolt()
			bolt.rect = cannon
			bolt.speed = sprite.bolt_speed
			all_sprites_list.add(bolt)
			enemy_bolt_sprites_list.add(bolt)

		sprite.attack_counter = 0
	else:
		sprite.attack_counter += 1

def ai_spawn(screen_size, roster, enemy_list, all_sprites_list):

	for enemy in roster:
		if enemy.spawn_counter == enemy.spawn_counter_max:
			new_enemy = enemy.spawn()
			new_enemy.rect = (random.randint(0,screen_size - new_enemy.size),0)
			enemy_list.add(new_enemy)
			all_sprites_list.add(new_enemy)

			enemy.spawn_counter = 0
		else:
			enemy.spawn_counter += 1