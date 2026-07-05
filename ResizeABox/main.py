import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ResizeABox")

clock = pygame.time.Clock()

running = True

square_x = 100
square_y = 100
square_x_size = 50
square_y_size = 50
#----------------------------------------------
def draw_square():
    pygame.draw.rect(
        screen,
        'red',
        (square_x, square_y, square_x_size, square_y_size)
    )
#----------------------------------------------
def event_handling():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#----------------------------------------------
while running:
    
    event_handling()
    screen.fill('black')

    draw_square()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()