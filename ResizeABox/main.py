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

mouse_x, mouse_y = 0,0

detection_offset = 5
#----------------------------------------------
def display_text(text):
    font = pygame.font.Font(None, 48)
    text = font.render(text,True,'WHITE')
    screen.blit(text, (200,250))
#----------------------------------------------
def detect_square_edges():
    global mouse_x, mouse_y
    global square_x, square_x_size, square_y, square_y_size
    # pt1 (100,100) pt2 (150,100) pt3 (100,150) pt4 (150,150)
    if (
        square_x < mouse_x < square_x + square_x_size and
        square_y - detection_offset <= mouse_y <= square_y + detection_offset
    ):
        display_text('Mouse on top edge')
    elif(
        square_y - detection_offset < mouse_y < square_y + square_y_size + detection_offset and
        square_x - detection_offset <= mouse_x <= square_x + detection_offset
    ):
        display_text('Mouse on left edge')
    elif(
        square_y - detection_offset < mouse_y < square_y + square_y_size + detection_offset and
        square_x + square_x_size - detection_offset <= mouse_x <= square_x + square_x_size + detection_offset
    ):
        display_text('Mouse on right edge')
    elif(
        square_x - detection_offset <= mouse_x <= square_x + square_x_size + detection_offset and
        square_y + square_y_size - detection_offset <= mouse_y <= square_y + square_y_size + detection_offset
    ):
        display_text('Mouse on bottom edge')
    else:
        display_text(' ')
#----------------------------------------------
def get_mouse_pos():
    global mouse_x, mouse_y
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # print(mouse_x, mouse_y)
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Left Click")
#----------------------------------------------
while running:
    
    event_handling()
    get_mouse_pos()

    screen.fill('black')

    draw_square()
    detect_square_edges()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()