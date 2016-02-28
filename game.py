import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A Bit Racey')
clock = pygame.time.Clock()

carImage = pygame.image.load('./images/racecar.png')
pygame.display.set_icon(carImage)

car_width = 73

pause = False


def things_dogded(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dogded : " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    gameDisplay.blit(carImage, (x, y))


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surface, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(text_surface, text_rect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash():
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surface, text_rect = text_objects("You crashed", large_text)
    text_rect.center = ((display_width / 2), (display_height / 2))
    # putting text on the window
    gameDisplay.blit(text_surface, text_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        button("Play Again!", 150, 450, 100, 50, green, bright_green, 20, "freesansbold.ttf", game_loop)
        button("QUIT!", 550, 450, 100, 50, red, bright_red, 20, "freesansbold.ttf", quitgame)

        # update the display with all the elements
        pygame.display.update()
        # clock tick for repeating this loop
        clock.tick(15)


def button(msg, x_cord, y_cord, width, height, inactive_color, active_color, font_size, font_type, action=None):
    # get mouse position
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # create button for play and quit
    if x_cord + width > mouse[0] > x_cord and y_cord + height > mouse[1] > y_cord:
        pygame.draw.rect(gameDisplay, active_color, (x_cord, y_cord, width, height))
        if click[0] == 1 and action:
            action()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x_cord, y_cord, width, height))

    small_text = pygame.font.Font(font_type, font_size)
    text_surface, text_rect = text_objects(msg, small_text)
    text_rect.center = (x_cord + (width / 2), y_cord + (height / 2))
    gameDisplay.blit(text_surface, text_rect)


def unpause():
    global pause
    pause = False


def paused():
    # text for starting the game
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surface, text_rect = text_objects("PAUSED", large_text)
    text_rect.center = ((display_width / 2), (display_height / 2))
    # putting text on the window
    gameDisplay.blit(text_surface, text_rect)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        button("Continue!", 150, 450, 100, 50, green, bright_green, 20, "freesansbold.ttf", unpause)
        button("QUIT!", 550, 450, 100, 50, red, bright_red, 20, "freesansbold.ttf", quitgame)

        # update the display with all the elements
        pygame.display.update()
        # clock tick for repeating this loop
        clock.tick(15)


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        # filling the window with white color
        gameDisplay.fill(white)
        # text for starting the game
        large_text = pygame.font.Font('freesansbold.ttf', 115)
        text_surface, text_rect = text_objects("A bit racey", large_text)
        text_rect.center = ((display_width / 2), (display_height / 2))
        # putting text on the window
        gameDisplay.blit(text_surface, text_rect)

        button("GO!", 150, 450, 100, 50, green, bright_green, 20, "freesansbold.ttf", game_loop)
        button("QUIT!", 550, 450, 100, 50, red, bright_red, 20, "freesansbold.ttf", quitgame)

        # update the display with all the elements
        pygame.display.update()
        # clock tick for repeating this loop
        clock.tick(15)


def game_loop():
    car_x = display_width * 0.45
    car_y = display_height * 0.8
    x_change = 0
    global pause
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
    dogded = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        car_x = car_x + x_change

        gameDisplay.fill(white)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        car(car_x, car_y)
        things_dogded(dogded)

        if car_x > display_width - car_width or car_x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dogded += 1
            thing_speed += 1
            thing_width += (dogded * 1.2)

        if car_y < thing_starty + thing_height:
            if car_x > thing_startx and car_x < thing_startx + thing_width or car_x + car_width > thing_startx and car_x + car_width < thing_startx + thing_width:
                crash()

        pygame.display.update()
        clock.tick(60)


def quitgame():
    pygame.quit()
    quit()


game_intro()
game_loop()
