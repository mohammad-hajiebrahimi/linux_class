import pygame
import random
pygame.init()

disp = pygame.display.set_mode((800,600))

done = False
x = [0]*10
y = [0]*10
dx = [1]*10
dy = [1]*10
for i in range(10):
    x[i] = random.randint(0,800)
    y[i] = random.randint(0,600)
while not done:
    for i in range(10):
        x[i]+= dx[i]
        y[i]+= dy[i]
    for i in range(10):
        if x[i]<0 or x[i]>800:
            dx[i]*=(-1)
            dy[i]*=(-1)
        if y[i]<0 or y[i]>600:
            dy[i]*=(-1)
            dx[i]*=(-1)
    disp.fill((100,100,100))
    for i in range(10):
        pygame.draw.circle(disp,(255,0,0),(x[i],y[i]),40,20)
    pygame.display.update()
    pygame.time.Clock().tick(240)
