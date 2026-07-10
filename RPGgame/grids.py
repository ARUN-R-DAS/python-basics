import pygame

class Game:
    pygame.init()

    WIDTH = 800
    HEIGHT = 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    def draw(self):
        for i in range(1,7):
            for j in range(1,6):
                x = i * 100
                y = j * 100 - 50
                width = 100
                height = 100
                rect = pygame.Rect(x, y, width, height)
                pygame.draw.rect(self.screen,'red',rect, 2)

    def handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def run(self):
        while self.running:
            self.handle_events()

            self.screen.fill('black')
            
            self.draw()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

game = Game()
game.run()