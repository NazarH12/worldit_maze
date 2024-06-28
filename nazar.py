import pygame
import os
pygame.init()

clock = pygame.time.Clock()
display = pygame.display.set_mode((650, 650)) 

geroi = pygame.Rect(400, 55, 30, 30)
go_right = False
go_left = False
go_up = False
go_down = False

dir_path = os.path.dirname(__file__)
img_path = os.path.abspath(dir_path + "/textures")
gate = pygame.image.load(img_path + "/gate.png")
wood = pygame.image.load(img_path + "/wood.png")
wall_electro = pygame.image.load(img_path + "/wall_electro.png")
food = pygame.image.load(img_path + "/food.png")
hero = pygame.image.load(img_path + "/hero.png")
hero = pygame.transform.scale(hero, (30, 30))
textures = [     
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,2,2,2,3,2,1],
    [1,2,3,3,3,3,2,2,2,2,3,2,1],
    [1,2,1,1,1,1,1,2,2,2,2,2,1],
    [1,2,1,1,1,1,1,1,1,1,1,3,1],
    [1,2,2,2,2,2,2,2,2,2,2,1,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,1],
    [1,3,3,3,3,2,2,2,3,2,2,2,1],
    [1,1,1,1,3,3,1,2,2,3,2,2,1],
    [1,4,1,1,2,2,2,2,2,3,2,2,1],
    [1,2,2,3,2,2,3,3,3,3,2,3,1],
    [1,3,2,2,2,3,3,2,2,3,2,3,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1]

]


rects = []
rects_textures = []
bad_rects = [] 
good_rects = []
x = 0
y = 0
for texture in textures:
    for i in texture:
        kvadrat = pygame.Rect(x, y, 50, 50)
        rects.append(kvadrat)
        rects_textures.append(i)
        if i == 1 or i == 3 :
            bad_rects.append(kvadrat)
        if i == 4:
            good_rects.append(kvadrat)
            
        
        x += 50
    y += 50
    x = 0
    
font = pygame.font.SysFont("Arial", 50)
text = font.render("YOU WIN!", True, (0,0,255))

game = True 

while game:

    display.fill((200, 0, 0))

    for i in range(169):
        if rects_textures[i] == 1:
            display.blit(gate, rects[i])
        if rects_textures[i] == 2:
            display.blit(wood, rects[i])
        if rects_textures[i] == 3:
            display.blit(wall_electro, rects[i])    
        if rects_textures[i] == 4:
            display.blit(food, rects[i])    
        if rects_textures[i] == 5:
            display.blit(hero, rects[i])    
    display.blit(hero, geroi)
    
    for bad in bad_rects:
        if geroi.colliderect(bad):
            geroi.x = 400
            geroi.y = 55

    for good in good_rects:
        if geroi.colliderect(good):
            display.fill((0, 0, 0))
            display.blit(text, (200,200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                go_right = True
            if event.key == pygame.K_a:
                go_left = True
            if event.key == pygame.K_w:
                go_up = True
            if event.key == pygame.K_s:
                go_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                go_right = False
            if event.key == pygame.K_a:
                go_left = False
            if event.key == pygame.K_w:
                go_up = False
            if event.key == pygame.K_s:
                go_down = False

    if go_right == True:
        geroi.x += 5
    if go_left == True:
        geroi.x -= 5
    if go_up == True:
        geroi.y -= 5
    if go_down == True:
        geroi.y += 5

    pygame.display.flip()
    clock.tick(60)