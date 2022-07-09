# Importing module and sounds
import pygame
from math import *
from random import *
from variables import *
pygame.init()
pygame.mixer.init()
cointake = pygame.mixer.Sound(path+'Sounds/CoinPickSound.wav')
deathsound = pygame.mixer.Sound(path+'Sounds/DeathSound.wav')
font = pygame.font.SysFont(None,font_size)

def welcome_window(): # This function is for welcome window which player incounters first of all 
    screen.fill((0,0,0))
    screen.blit(play_i,(450,200)) # This fuction illustrates about the position of "play" button in welcome window

def initial_list(listlift,listobj,listcoin,ind): # This function is for appending the positions of moving objects in the game as the game progresses
    for value in range(5):
       ind = ind+randint(300, width)
       listobj.append(ind)

    ind = width
    for value in range(1):
       ind = ind+randint(300, width)
       listlift.append(ind) # appending the position of new lifts
    ind = width
    
    for value in range(1):
       ind = ind+randint(300, width)
       listcoin.append(ind) # appendin the positions of new coins

    with open(coin_file, 'r') as f_object:
         num_coin = int(f_object.read())
    return num_coin

def text_screen(text,color,x,y): # This fuction is for displaying the "text" (sentence assigned to this variable) on screen
    screen_text = font.render(text,True,color)
    screen.blit(screen_text,[x, y])




def character_movement(timer,chx,chy,jumping,movement,he_of_jump,scatek):
    # There are eight images which are changing in every frame while character is running
        if (timer+(num_i-1)*FPS) % (num_i*FPS) == 0 and movement == True and scatek != True:
            screen.blit(ch_1, (chx, chy))
        elif (timer+(num_i-1)*FPS) % (num_i*FPS) == FPS and movement == True and scatek != True:
            screen.blit(ch_2, (chx, chy))
        elif (timer+(num_i-1)*FPS) % (num_i*FPS) == 2*FPS and movement == True and scatek != True:
            screen.blit(ch_3, (chx, chy))
        elif (timer+(num_i-1)*FPS) % (num_i*FPS) == 3*FPS and movement == True and scatek != True:
            screen.blit(ch_4, (chx, chy))
        elif (timer+(num_i-1)*FPS) % (num_i*FPS) == 4*FPS and movement == True and scatek != True:
            screen.blit(ch_5, (chx, chy))
        elif (timer+(num_i-1)*FPS) % (num_i*FPS) == 5*FPS and movement == True and scatek != True:
            screen.blit(ch_6, (chx, chy-1))
        elif (timer+(num_i-1)*FPS) % (num_i*FPS) == 6*FPS and movement == True and scatek != True:
            screen.blit(ch_7, (chx, chy))
        elif (timer+(num_i-1)*FPS) % (num_i*FPS) == 7*FPS and movement == True and scatek != True:
            screen.blit(ch_8, (chx, chy))
    # When we press for jump then the movement variable get "False" and depending on the jump type maximum height of jump which is stored in "he_of_jump" variable gets it value and the image of character changes accordingly.
        elif movement == False and he_of_jump<80: 
            screen.blit(ch_5, (chx, chy))
        elif movement == False and he_of_jump>80:
            screen.blit(launch1,(chx,chy))
    # When scatek is equal to "true" this means that the player pressed the key for scateboard then this condition changes the image of th character with scateboard
        elif scatek==True and jumping!=True:
            screen.blit(scate2,(chx,chy-20))

# In this function, we change the image of a coin in every frame so we get the illusion of rotating coin
def coin_movement(timer,listcoin): 
    for value in listcoin:
        if (timer+(num_j-1)*FPS) % (num_j*FPS) == 0:
            screen.blit(c_1,(value,y0+ch_height-coin_h))
        elif (timer+(num_j-1)*FPS) % (num_j*FPS) == FPS:
            screen.blit(c_2, (value,y0+ch_height-coin_h))
        elif (timer+(num_j-1)*FPS) % (num_j*FPS) == 2*FPS:
            screen.blit(c_3, (value,y0+ch_height-coin_h))
        elif (timer+(num_j-1)*FPS) % (num_j*FPS) == 3*FPS:
            screen.blit(c_4, (value,y0+ch_height-coin_h))
        elif (timer+(num_j-1)*FPS) % (num_j*FPS) == 4*FPS:
            screen.blit(c_5, (value,y0+ch_height-coin_h))
        elif (timer+(num_j-1)*FPS) % (num_j*FPS) == 5*FPS:
            screen.blit(c_6, (value,y0+ch_height-coin_h))
     
def back_display_music(listbg,timer):
    screen.fill((0,0,0))
    for value in range(2):
        screen.blit(bgimg,(listbg[value],0))
    listbg[0],listbg[1] = listbg[0]+bg_speed,listbg[1]+bg_speed
    if listbg[1]<j:
            listbg[0] = 0
            listbg[1] = width
    if timer==0:
        pass#  pygame.mixer.music.play(-1,0.0)

# This function is to jump the character 
def jump(chy,vy,fi_jump,i,he_of_jump,launching):
     if fi_jump:
         return he_of_jump-i*i
     elif fi_jump == False and chy>y0-50 and launching == False:
         return 0
     elif fi_jump == False and chy>y0-100 and launching == True:
         return 0 
     else:
         return -i*i/7

# This function moves the objects (Rocks on the ground) with background speed
def move_object(listobj,bg_speed):
    iterator = -1
    for value in listobj:
       iterator += 1
       value += bg_speed
       listobj[iterator] = value
    for value in listobj:
       screen.blit(object,(value,y0+ch_height-o_height))
    return listobj 

# this function is for moving the coin
def move_coin(listcoin,bg_speed,timer):
    iterator = -1
    for value in listcoin:
        iterator += 1
        value += bg_speed
        listcoin[iterator] = value
    coin_movement(timer,listcoin)
    return listcoin


# For moving the lifts
def move_lift(listlift,bg_speed):
    iterator = -1
    for value in listlift:
        iterator += 1
        value += bg_speed
        listlift[iterator] = value
    for value in listlift:
        screen.blit(liftimg,(value,y0-20))
    return listlift

# this function is for deleting the objects like lifts,coins etc after their number increases beyond 15
def del_lo(list):
    if len(list) > 15:
        for value in range(5):
            del list[value]
    return list

# This function checks that the last object (rocks,lifts,coins) in the list is far enough (width/1.5) from the end of screen, if it is, then it appends new positions for new member in the list
def check_object(list):
    if list[-1] < width/1.5:
        ind = width+randint(0, width)
        list.append(ind)
        ind = width
    return list

# This does similar work as mentioned above for "check_object()" function
def check_objectl(list):
    if list[-1] < width/1.2:
        ind = width+randint(0,300)
        list.append(ind)
        ind = width
    return list

def check_lift(listlift):
    if listlift[-1]<0:
        ind = width+randint(600,2*width)
        listlift.append(ind)
        ind = width
    return listlift

# when game overs then this function does its work by playing the death sound and showing the image of crash
def gm_ovr(listobj,listlift,chx,chy,vy,score):
    flag = False
    for value in listobj:
        if abs(chx-value)<100 and abs(chy-y0)<80:
            flag = True
            screen.blit(bang,(value,y0))
            deathsound.play()
            break
    for value in listlift:
        if chx>(value-100) and chx<(value+o_width) and chy<=y0 and chy>y0-50:
            screen.blit(bang,(value,y0+25))
            flag = True
            deathsound.play()
            break
    return flag

# After completion of work of above function this function does its work by showing the game over window
def game_over_window():
    screen.fill((255,255,255))
    screen.blit(over,(450,200))
    
def c_lift(listlift,listobj):   
      iterator = 0
      for value_l in listlift:
         for value_o in listobj:
             if (value_l-value_o)<300 and (value_l-value_o)>0:
                 listlift[iterator] = value_o+600
      return listlift            

# returns the coordinate of rocks
def rodie(listobj):
    listobj = move_object(listobj,bg_speed)
    listobj = check_object(listobj)
    listobj = del_lo(listobj)
    return listobj

#This function determines whether character has touched the coin or not and if it touched then coin disappears and coin taking music is played
def chaal(listcoin,chx,chy):
    iterator = 0
    for value in listcoin:
        if abs(value-chx)<120 and ((y0+ch_height-coin_h)-(chy+ch_height+10))<0:
            del listcoin[iterator]
            cointake.play()
    return listcoin

# This function is for incremanting the number of coins after touching the coin by character.
def incre_coin(num_coin,chx,chy,listcoin):
    iterator = 0
    for value in listcoin:
        if abs(value-chx)<130 and ((y0+ch_height-coin_h)-(chy+ch_height))<0:
            num_coin += 1
            with open(coin_file, 'w') as file_o:
                  file_o.write(str(num_coin))
    return num_coin

# This function returns the posion of coins after modifying the positions according to speed and checking with check function
def coin(listcoin,timer,chx,chy): 
    listcoin = move_coin(listcoin,bg_speed,timer)
    listcoin = check_objectl(listcoin)
    return listcoin

# This function returns the position of lifts
def lift_rodie(listlift,listobj):
    listlift = move_lift(listlift, bg_speed)
    listlift = check_lift(listlift)
    listlift = c_lift(listlift, listobj)
    listlift = del_lo(listlift)
    return listlift

# This function creates the scoreboard
def score_board(score,timer):
    if timer%500*FPS == 0:
        score+=1
    text_screen(f"Score:{score}",(254,238,0), 10,20)
    return score

# This function determines if the scores gained by player are high scores or not if yes then it replaces the high score in the h_score.txt file 
def h_score_screen(score):
    with open(h_score_file, 'r') as f_object:
        h_scores = f_object.read()
        text_screen(f"High Score: {h_scores}", (254, 238, 0),10,50)
    if int(h_scores) < score:
        with open(h_score_file,'w') as file_o:
           file_o.write(str(score))
           h_scores = score
    return h_scores
    

