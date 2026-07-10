import pygame

class Game:
    def __init__(self):
        pygame.init()

        self.WIDTH = 800
        self.HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.player_pos = None

    def update_player_pos(self):
        if not self.player_pos:
            self.player_pos = list(self.centers[0])
        

    def draw_grid(self):
        self.centers = []

        for i in range(1,7):
            for j in range(1,6):
                x = i * 100
                y = j * 100 - 50
                width = 100
                height = 100
                rect = pygame.Rect(x, y, width, height)
                self.centers.append(rect.center)

                pygame.draw.rect(self.screen,'red',rect, 2)
    
    def draw_player(self):
        pygame.draw.circle(self.screen, 'green', self.player_pos, 10)

    def handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.player_pos[1] += 100
                    if event.key == pygame.K_UP:
                        self.player_pos[1] -= 100

    def run(self):
        while self.running:
            self.handle_events()

            self.screen.fill('black')
            
            self.draw_grid()
            self.update_player_pos()
            self.draw_player()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

game = Game()
game.run()