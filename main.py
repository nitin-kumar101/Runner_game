# Importing modules
import pygame
import sys
from math import *
from random import *
from variables import *
from functions import *
from time import *
pygame.mixer.init()

#pygame.mixer.music.load('Sounds/BackgroundSound.mp3')
jumpsound = pygame.mixer.Sound(path+'Sounds/launching.wav')

pygame.init() #Initialisation of Pygame module
pygame.display.set_caption("Unknown") # Displaying the name of game in Caption as "Unknown"

num_coin = initial_list(listlift,listobj,listcoin,ind) # This 


while not_exit_game:  # This loop will run until the game stops
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            not_exit_game = False
        if event.type == pygame.MOUSEMOTION:
            x,y = event.pos
 #           print(x,":",y)
        if event.type == pygame.MOUSEBUTTONDOWN and x>456 and x<743 and y>284 and y<401:
            play = True # When the player clicks on the given position then the interface will change and the variable "play" will change to true meaning the running window is about to open
            play_i = pygame.transform.scale(play_i, (295, 295)).convert_alpha()
            screen.blit(play_i, (452, 200))
        if event.type == pygame.MOUSEBUTTONDOWN and game_over==True and time_of_over>2 and x > restartimgx and x < restartimgx+restartimg_w and restartimgy < y and restartimgy+restartimg_h > y:
            restart = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                he_of_jump = 75 # This is the height till which player can jump after pressing the "j" key
                jumping = True
                movement = False
            if event.key == pygame.K_s: # When player press 's' key then he gets scateboard if number of coins is greter than 50 and after using it there will be reduction of 50 coins
              if num_coin>=50:
                scatek = True
                chy = y0-ch_height
                temp = 1
                num_coin = num_coin-50
            if event.key == pygame.K_q: # 'q' for short jump
                jumping = True # This variable determines whether player is in jumping mode or not
                movement = False # This is for determining the running status of the player
            if event.key == pygame.K_l: # 'l' for launching jetpack
                if num_coin>=50:
                    he_of_jump = 95
                    jumping = True
                    movement = False
                    jumpsound.play(1,0)
                    launching = True
                    num_coin -= 50
            if event.key == pygame.K_RETURN: # when the player hits the enter key on welcome window then game starts
                play = True
            if event.key == pygame.K_RETURN and game_over==True and time_of_over>2: # when player hits the enter key after game over then it restarts
                restart = True

    if play == False and game_over == False:  
        welcome_window()   # first of all we will see the welcome window whcich is because the variables "play" and "game_over" are False            
        
    elif play == True and game_over == False: # after the welcome windo game starts after clicking the play button or hitting the 'enter' key as these variables hold these values which are given in this condition
        back_display_music(listbg, timer)
        Time,chx,timer = int(timer/pow(FPS,2)),chx+ch_speed,timer+FPS
        if scatek == True:
            if temp == 1:
                 var = Time
            k = int(Time-var+1)
            text_screen(f"{k}",(255,255,255),width/2,20)
            temp += 1
            if k > 10:
                temp = 0
                scatek = False
                jumping = True
                movement = False
                i = sqrt(he_of_jump)+1
    
        if jumping: # when "jumping" is true then below code helps to jump the character 
            t += 1
            i += 1
            vy = jump(chy, vy, fi_jump, i, he_of_jump,launching) # upward velocity of character
            if scatek == True:
                scatek = False
            if vy < 0:
                fi_jump = False
            if vy==0:
               # jumpsound.stop()
                if launching:
                    launching = False
                if he_of_jump>55:
                    he_of_jump = 55
                fi_jump = True
                jumping = False
                movement = True
                i = 0
                chy = y0
            chy = chy-vy # vertical position of the player is modifying with time
        # description of followingfunctions given in functions module
        listcoin = coin(listcoin,timer,chx,chy) 
        num_coin = incre_coin(num_coin, chx, chy, listcoin)
        text_screen(f"Coins:{num_coin}", (254, 238, 0),coinposx,20)
        listcoin = chaal(listcoin, chx, chy)
        coin_movement(timer,listcoin)
        listobj = rodie(listobj)
        character_movement(timer, chx, chy, jumping, movement,he_of_jump,scatek)
        listlift = lift_rodie(listlift,listobj)
        game_over = gm_ovr(listobj, listlift, chx, chy,vy,score)

        for value in listlift:
            if chx>(value-(ch_width/2)) and chx<(value+o_width+80) and chy<(((y0-20)-ch_height)+50) and chy>(((y0-20)-ch_height)-20):
                tenter += 1
                rlift = True
                if tenter==1 and ju == True:
              #      jumpsound.stop()
                    jumping = False
                    movement = True
                    chy = 354-ch_height-4
                    i = 0
                    fi_jump = True
                    vy = 0
                print(tenter)
            elif chx>(value+o_width+100) and chx<(value+o_width+130) and chy<=((y0-20)-ch_height+50) and chy>((y0-20)-ch_height-20) and jumping == False:
                   jumping = True
                   movement = False
                   i = sqrt(he_of_jump)+1
                   tenter = 0
          
        if jumping==True and tenter>0:
            tenter = 0
            ju = False
        else:
            ju = True
         
        score = score_board(score,timer)
        h = h_score_screen(score)
    
    elif game_over == True: # when "game_over" variable gets "True" then the screen changes, all the variables are initialised to their initial values, list of objects are cleaned and restart button, score and other things being showed
        pygame.mixer.music.stop()
        jumpsound.stop()
        if time_of_over>2:
          screen.blit(bg2img,(0,0))
          font_size = 80
          text_screen(f"Score:{score}",(255,255,255),(width/2)-150,height/2-50)
          text_screen(f"High Score:{h}", (255, 255, 255),(width/2)-150, height/2)
          text_screen(f"Coins:{num_coin}", (255, 255,255), (width/2)-150, height/2+50)
          if restart==True:
             play = True
             timer,time_of_over = 0,0
             i,j,t,remp=0,1,10,5
             not_exit_game,jumping,fi_jump,game_over,restart,movement,restart = True,False,True,False,False,True,False
             ind = width
             listbg, listobj, listcoin, listlift = [bgx1, bgx2], [], [], []
             rlift = False
             not_in_lift = False
             tenter = 0
             ju = True
             score = 0
             chy = y0
             initial_list(listlift, listobj,listcoin,ind)
             with open(coin_file, 'r') as f_object:
                    num_coin = int(f_object.read())

             ind = width
             for value in range(5):
                  ind = ind+randint(300, width)
                  listcoin.append(ind)

        else:
          time_of_over += 1/FPS
          game_over_window()

    pygame.display.update()
    timetick.tick(FPS)
