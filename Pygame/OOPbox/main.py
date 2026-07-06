import pygame
class Rect:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Game:
    def __init__(self):
        pygame.init()

        self.WIDTH = 800
        self.HEIGHT = 600

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Practice_class_box')

        self.clock = pygame.time.Clock()
        self.running = True

        self.R1 = Rect(100, 100, 50, 50, 'red')
    
    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def run(self):
        while self.running:
            self.event_handling()

            self.screen.fill('black')
            self.R1.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()

game = Game()
game.run()