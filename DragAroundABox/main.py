import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Caption ???")

running = True
clock = pygame.time.Clock()

mousedown = False

#square parameters---------------------------------------
square_x = 100
square_y = 100
square_size = 50
#--------------------------------------------------------
def draw_square():
    pygame.draw.rect(
        screen,
        'red',
        (square_x,square_y,square_size,square_size)
    )
#---------------------------------------------------------
def get_mouse_position():
    global mousedown
    if mousedown:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        print(mouse_x, mouse_y)
#---------------------------------------------------------
def handle_events():
    global mousedown
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Left mouse button pressed")
                mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                print("Left mouse button released")
                mousedown = False
#---------------------------------------------------------
while running:
    
    handle_events()
    get_mouse_position()

    screen.fill("black")
    draw_square()
    pygame.display.flip()
    clock.tick(60)
#---------------------------------------------------------
pygame.quit()