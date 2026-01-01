import pygame
pygame.init()

width = 800
heigth = 600
x = 0
y = 300
movement = 100
size = 40
down_movement = 0.2

screen = pygame.display.set_mode((width,heigth))
pygame.display.set_caption("ATHARVS FLOPY BIRD")


flopy = pygame.image.load("image/flopy.png")
flopy = pygame.transform.scale(flopy,(100,140))

game_on = True

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False 
        if event.type == pygame.KEYDOWN:      
           if event.key == pygame.K_SPACE:
                y -= movement
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                pass

    y += down_movement
    x += 0.01
    if y >= 550:
        y = 0
    if x >= 750:
        x=0    
    screen.fill((255, 255 ,255))
    screen.blit(flopy,(x , y))
    # pygame.draw.rect(screen,(255, 0 ,0),( x, y, size, size))
    pygame.display.update()


pygame.quit()           