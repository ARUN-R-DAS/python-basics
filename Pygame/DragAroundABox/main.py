import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move a Square")

running = True
clock = pygame.time.Clock()

mousedown = False

square_x = 100
square_y = 100
square_size = 50

mouse_x, mouse_y = 0,0

dragging = False
#--------------------------------------------------------
def move_sqaure():
    global dragging
    global mouse_x, mouse_y
    global square_x, square_y
    if dragging:
        square_x = mouse_x - square_size // 2
        square_y = mouse_y - square_size // 2
#--------------------------------------------------------
def draw_square():
    pygame.draw.rect(
        screen,
        'red',
        (square_x,square_y,square_size,square_size)
    )
#---------------------------------------------------------
def get_mouse_position():
    global mouse_x, mouse_y
    mouse_x, mouse_y = pygame.mouse.get_pos()
#---------------------------------------------------------
def was_square_clicked():
    global dragging
    if (
            square_x < mouse_x < square_x + square_size and
            square_y < mouse_y < square_y + square_size
        ):
            print("Clicked inside square")
            dragging = True
            print("Started dragging")
#---------------------------------------------------------
def handle_events():
    global mousedown
    global running
    global dragging
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Left mouse button pressed")
                mousedown = True
                was_square_clicked()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                print("Left mouse button released")
                mousedown = False
                if dragging:
                    dragging = False
                    print("Stopped dragging")
                
#---------------------------------------------------------
while running:
    
    handle_events()
    get_mouse_position()

    screen.fill("black")
    move_sqaure()
    draw_square()

    pygame.display.flip()
    clock.tick(60)
#---------------------------------------------------------
pygame.quit()