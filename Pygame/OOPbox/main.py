import pygame
#-----------------------------------------------------------------------------------
class Box:
    def __init__(self, color, screen, corner1 = (100,100), corner2 = (150,150)):
        # create rectangle obj using 2 coordinates (topLeft & bottom_right)
        self.color = color
        self.screen = screen
        
        self.corner1 = corner1
        self.corner2 = corner2
        # find x, y, width, height from coordinates
        x = corner1[0]
        y = corner1[1]
        width = corner2[0] - corner1[0]
        height = corner2[1] - corner1[1]
        #create pygame.Rect object
        self.box = pygame.Rect(x, y, width, height)
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.box)
#-----------------------------------------------------------------------------------
class Game:
    def __init__(self):
        pygame.init()

        self.WIDTH = 800
        self.HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.running = True
        self.clock = pygame.time.Clock()

        pygame.display.set_caption('Practice OOP principles')

        self.b1 = Box('red', self.screen, (100,100), (200,200))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # if x pressed, make the box larger
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    print('x key pressed')
                    

    def run(self):
        while self.running:
            self.handle_events()

            self.screen.fill('black')
            self.b1.draw()

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

game = Game()
game.run()