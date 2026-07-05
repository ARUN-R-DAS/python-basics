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

current_edge = None
dragging = False

old_square =  {
    'sq_x':0,
    'sq_y':0,
    'sq_x_size':0,
    'sq_y_size':0
}
#----------------------------------------------
def resize_square():
    global current_edge
    global dragging
    global square_y,square_y_size
    global old_square

    if dragging:
        if current_edge == 'top':
            square_y = mouse_y
            square_y_size = (old_square['sq_y'] + old_square['sq_y_size']) - square_y
#----------------------------------------------
def display_text(text):
    font = pygame.font.Font(None, 48)
    text = font.render(text,True,'WHITE')
    screen.blit(text, (200,250))
#----------------------------------------------
def detect_square_edges():
    global mouse_x, mouse_y
    global square_x, square_x_size, square_y, square_y_size
    global current_edge
    # pt1 (100,100) pt2 (150,100) pt3 (100,150) pt4 (150,150)
    if (
        square_x < mouse_x < square_x + square_x_size and
        square_y - detection_offset <= mouse_y <= square_y + detection_offset
    ):
        display_text('Mouse on top edge')
        current_edge = 'top'
    elif(
        square_y - detection_offset < mouse_y < square_y + square_y_size + detection_offset and
        square_x - detection_offset <= mouse_x <= square_x + detection_offset
    ):
        display_text('Mouse on left edge')
        current_edge = 'left'
    elif(
        square_y - detection_offset < mouse_y < square_y + square_y_size + detection_offset and
        square_x + square_x_size - detection_offset <= mouse_x <= square_x + square_x_size + detection_offset
    ):
        display_text('Mouse on right edge')
        current_edge = 'right'
    elif(
        square_x - detection_offset <= mouse_x <= square_x + square_x_size + detection_offset and
        square_y + square_y_size - detection_offset <= mouse_y <= square_y + square_y_size + detection_offset
    ):
        display_text('Mouse on bottom edge')
        current_edge = 'bottom'
    else:
        display_text(' ')
        if dragging == False:
            current_edge = None
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
    global dragging
    global old_square
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Left Click Pressed")

                if current_edge:
                    dragging = True
                    # storing old square values for resizing
                    old_square['sq_x'] = square_x
                    old_square['sq_y'] = square_y
                    old_square['sq_x_size'] = square_x_size
                    old_square['sq_y_size'] = square_y_size

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                print("Left Click Released")
                dragging = False
                
#----------------------------------------------
while running:
    
    event_handling()
    get_mouse_pos()

    screen.fill('black')

    draw_square()
    detect_square_edges()
    resize_square()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()