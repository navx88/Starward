import pygame
import sprites
import gameplay

pygame.init()

screen_size = 640
sprite_size = 64

screen = pygame.display.set_mode((screen_size,screen_size))
pygame.display.set_caption("Starborne")
clk = pygame.time.Clock()

background = "background.png"

player = sprites.Mercerite() # dis be the player

roster = []

enemy = sprites.enemy_mercerite_dmged1()
roster.append(enemy)
enemy = sprites.enemy_mercerite_dmged2()
roster.append(enemy) 
enemy = sprites.enemy_mercerite_dmged3()
roster.append(enemy)
enemy = sprites.enemy_mercerite()
roster.append(enemy)

gameplay.loop(screen, background, screen_size, sprite_size, clk, player, roster)

"""
Have one gameplay loop
-have some sort of roster for list of enemy sprites to spawn and pass into gameplay.loop()
	-should be 2d array
	-one row be sprite to spawn
	-other row be weight (how oft it spawn)ddddddd
"""

print("END")