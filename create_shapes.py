import pygame

pygame.init()


display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.fill(black)

pixel_array = pygame.PixelArray(gameDisplay)
pixel_array[10][20] = green

pygame.draw.line(gameDisplay,blue,(100,200),(300,450),5)
pygame.draw.rect(gameDisplay,red,(400,400,50,50))
pygame.draw.circle(gameDisplay,green,(150,150),50)
pygame.draw.polygon(gameDisplay,white,((25,75),(76,125),(250,375),(400,25),(65,540)))


while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    pygame.display.update()