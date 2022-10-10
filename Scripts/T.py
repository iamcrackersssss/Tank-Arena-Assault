from Focus import *
import pygame

bullet_list=[]

movement_speed=1.6

Tank1_x=250
Tank1_y=450

def display_bullet():

    for bullet in bullet_list:
        if bullet["y"]<0: #if the bullet moves out of the screen we arew going to delete it
            bullet_list.remove(bullet)
        bullet_obj=image("Imgs/Ammo.png",20,20,bullet["x"],bullet["y"])
        bullet["bullet_object"]=bullet_obj#updated line

def change():
    global bullet_list, movement_speed, Tank1_x, Tank1_y, bullet
    set_background(color_mid_night_blue)
    Tank1 = image("Imgs/Player1and2.png",50,50,Tank1_x,Tank1_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys=get_keys_pressed()
    if keys[key_s]:
        bullet= {"x":"","y":"","bullet_object":""}
        bullet["x"]=Tank1_x
        bullet["y"]=Tank1_y
        bullet_list.append(bullet)
        print("bullet created")

    if keys[key_up]:
        Tank1_y-=movement_speed
    if keys[key_down]:
        Tank1_y+=movement_speed
    if keys[key_left]:
        Tank1_x-=movement_speed
    if keys[key_right]:
        Tank1_x+=movement_speed
    
    display_bullet()

    for bullet in bullet_list:
        bullet["y"]-=15

draw(change)