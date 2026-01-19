import pygame , random ,math
pygame.init()

def hit(ex,ey,bulletx,bullety):
    distance = math.sqrt(math.pow(ex-bulletx +10,2) + math.pow(ey-bullety,2))
    if distance < 40:
        return True
    else:
        return False

ex = random.randint(500, 800)
ey  = random.randint(400,450)
ex1 = ex   #random.randint(500, 800)
ey1  = 0 
width = 800
heigth = 600
x = 100
y = 300
movement = 150
size = 40
exsize = 50
eysize = 500
ex1size = 50
ey1size = random.randint(150, 200)
down_movement = 0.2
# ex = random.randint(500, 800)
# ey  = random.randint(250,400)
# ex1 = random.randint(500, 800)
# ey1  = random.randint(0,250) 

screen = pygame.display.set_mode((width,heigth))
pygame.display.set_caption("ATHARVS FLOPY BIRD")


flopy = pygame.image.load("images/flopy.png")
flopy = pygame.transform.scale(flopy,(100,140))

bg = pygame.image.load("images/back.png")
bg = pygame.transform.scale(bg,(800,600))

pipe1 = pygame.image.load("images/pipe.png")
pipe1 = pygame.transform.scale(pipe1,(ex1size,ey1size))

pipe2 = pygame.image.load("images/pipe2.png")
pipe2 = pygame.transform.scale(pipe2,(exsize,eysize))



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
    ex -= down_movement
    ex1 -= down_movement
    if ex  <= 0:
        ex =random.randint(800, 900) 
    if ex1  <= 0:
        ex1 = ex
    if y >= 550:
        y = 0
    if x >= 750:
        x=0    
    screen.blit(bg,(0,0))
    screen.blit(flopy,(x , y))
    screen.blit(pipe1,(ex1,ey1))
    screen.blit(pipe2,(ex,ey))
    # pygame.draw.rect(screen,(0, 0 ,0),( ex,ey, exsize, eysize))
    # pygame.draw.rect(screen,(255, 0 ,0),( ex1,ey1, ex1size, ey1size))
    pygame.display.update()


pygame.quit()           
