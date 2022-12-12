from Focus import *
import pygame

bullet_list=[]
bullet_list2=[]
movement_speed=1.6

Tank1_x=100 #set back at 100
Tank1_y=250 #set back at 250

Tank2_x=850 #set back at 850
Tank2_y=250 #set back at 250

set_screen_size(1000,1000)
def display_bullet():

    for bullet in bullet_list:
        if bullet["y"]<0: #if the bullet moves out of the screen we arew going to delete it
            bullet_list.remove(bullet)
        bullet_obj=image("Imgs/Ammo.png",20,20,bullet["x"],bullet["y"])
        bullet["bullet_object"]=bullet_obj#updated line

def change():
    global bullet_list, movement_speed, Tank1_x, Tank1_y, bullet,Tank2_x,Tank2_y
    set_background(color_mid_night_blue)
    Tank1 = image("Imgs/Both_Tanks.png",50,50,Tank1_x,Tank1_y)
    Tank2 = image("Imgs/Tank2.png",50,50,Tank2_x,Tank2_y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys=get_keys_pressed()
    if keys[key_space]:
        bullet= {"x":"","y":"","bullet_object":""}
        bullet["x"]=Tank1_x
        bullet["y"]=Tank1_y
        bullet_list.append(bullet)
        print("bullet created")
    
    #if keys[key_0]:
        #bullet2={"x":"","y":"","bullet_object":""}
        #bullet2=["x"]=Tank2_x
        #bullet2=["y"]=Tank2_y


    if keys[key_up]:
        Tank1_y-=movement_speed
    if keys[key_down]:
        Tank1_y+=movement_speed
    if keys[key_left]:
        Tank1_x-=movement_speed
    if keys[key_right]:
        Tank1_x+=movement_speed
    if keys[key_w]:
        Tank2_y-=movement_speed
    if keys[key_a]:
        Tank2_x-=movement_speed
    if keys[key_s]:
        Tank2_y+=movement_speed
    if keys[key_d]:
        Tank2_x+=movement_speed

    
    display_bullet()

    for bullet in bullet_list:
        bullet["x"]+=15

draw(change)
