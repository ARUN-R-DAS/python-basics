import os
import pygame

from actor import Actor
from weapons import AVAILABLE_WEAPONS

player = Actor('Player', 100, 100, 100, 100)
enemy = Actor('Goblin', 200, 100, 80, 80)

class Game:
    def __init__(self):
        pygame.init()

        self.WIDTH = 800
        self.HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption('RPG Game')

        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            keys = pygame.key.get_pressed()
            speed = 10

            if keys[pygame.K_a]:
                player.x -= speed
            if keys[pygame.K_d]:
                player.x += speed
            if keys[pygame.K_w]:
                player.y -= speed
            if keys[pygame.K_s]:
                player.y += speed
    
    def clamp_player_pos(self):
        player.x = max(30, min(player.x, self.WIDTH - 30 - 32))
        player.y = max(30, min(player.y, 400 - 32))

    def handle_draw(self):
        self.screen.fill('black')

        pygame.draw.rect(self.screen, 'green', (player.x, player.y, 32, 32))
        pygame.draw.rect(self.screen, 'red', (enemy.x, enemy.y, 32, 32))

        pygame.display.flip()
        self.clock.tick(60)

    def run(self):
        while self.running:
            self.handle_events()
            
            # print(pygame.mouse.get_pos())
            self.clamp_player_pos()

            self.handle_draw()

        pygame.quit()

game = Game()
game.run()