# This module contains all the variables and Initialization of those
import pygame
pygame.init()

width,height = 1200,700 # width and height of screen
ch_width,ch_height,o_width,o_height,restartimg_w,restartimg_h,coin_w,coin_h = 120,150,100,100,115,42,80,80 # Initialisng the width and height of characters, objects and icons
bg1color,bg2color = (0,0,0),(255,255,255) # Background color
screen = pygame.display.set_mode((width,height)) # Initialising screen
path='' #If there will be need to give absolute path to the images then use this variable
play_i = pygame.image.load(path+'n_games/play.png')
play_i = pygame.transform.scale(play_i, (300,300)).convert_alpha()
ch_1 = pygame.image.load(path+'n_games/ch_1.png')
ch_1 = pygame.transform.scale(ch_1, (ch_width+5,ch_height)).convert_alpha()
ch_2 = pygame.image.load(path+'n_games/ch_2.png')
ch_2 = pygame.transform.scale(ch_2, (ch_width+9,ch_height+2)).convert_alpha()
ch_3 = pygame.image.load(path+'n_games/ch_3.png')
ch_3 = pygame.transform.scale(ch_3, (ch_width-3,ch_height)).convert_alpha()
ch_4 = pygame.image.load(path+'n_games/ch_4.png')
ch_4 = pygame.transform.scale(ch_4, (ch_width-5,ch_height)).convert_alpha()
ch_5 = pygame.image.load(path+'n_games/ch_5.png')
ch_5 = pygame.transform.scale(ch_5, (ch_width, ch_height)).convert_alpha()
ch_6 = pygame.image.load(path+'n_games/ch_6.png')
ch_6 = pygame.transform.scale(ch_6, (ch_width+5,ch_height+3)).convert_alpha()
ch_7 = pygame.image.load(path+'n_games/ch_7.png')
ch_7 = pygame.transform.scale(ch_7, (ch_width-5,ch_height)).convert_alpha()
ch_8 = pygame.image.load(path+'n_games/ch_8.png')
ch_8 = pygame.transform.scale(ch_8, (ch_width-13,ch_height)).convert_alpha()
bgimg = pygame.image.load(path+'n_games/bc2.png')
bgimg = pygame.transform.scale(bgimg,(width,height)).convert_alpha()
bg2img = pygame.image.load(path+'n_games/after.png')
bg2img = pygame.transform.scale(bg2img, (width, height)).convert_alpha()
object = pygame.image.load(path+'n_games/object.png')
object = pygame.transform.scale(object,(o_width,o_height)).convert_alpha()
over = pygame.image.load(path+'n_games/game_over.png')
over = pygame.transform.scale(over, (300,300)).convert_alpha()
restartimg = pygame.image.load(path+'n_games/restartimg.png')
restartimg = pygame.transform.scale(restartimg, (restartimg_w,restartimg_h)).convert_alpha()
liftimg = pygame.image.load(path+'n_games/lift.png')
liftimg = pygame.transform.scale(liftimg,(o_width+100,o_height))
bang = pygame.image.load(path+'n_games/bang.png')
bang = pygame.transform.scale(bang, (100,100))
c_1 = pygame.image.load(path+'n_games/coin1.png')
c_1 = pygame.transform.scale(c_1, (coin_w,coin_h)).convert_alpha()
c_2 = pygame.image.load(path+'n_games/coin2.png')
c_2 = pygame.transform.scale(c_2, (coin_w,coin_h)).convert_alpha()
c_3 = pygame.image.load(path+'n_games/coin3.png')
c_3 = pygame.transform.scale(c_3, (coin_w, coin_h)).convert_alpha()
c_4 = pygame.image.load(path+'n_games/coin4.png')
c_4 = pygame.transform.scale(c_4, (coin_w,coin_h)).convert_alpha()
c_5 = pygame.image.load(path+'n_games/coin5.png')
c_5 = pygame.transform.scale(c_5, (coin_w, coin_h)).convert_alpha()
c_6 = pygame.image.load(path+'n_games/coin6.png')
c_6 = pygame.transform.scale(c_6, (coin_w, coin_h)).convert_alpha()
launch1 = pygame.image.load(path+'n_games/launch1.png')
launch1 = pygame.transform.scale(launch1,(ch_width-13,ch_height))
scate = pygame.image.load(path+'n_games/scate.png')
scate = pygame.transform.scale(scate, (ch_width+5,ch_height+20)).convert_alpha()
scate2 = pygame.image.load(path+'n_games/scate2.png')
scate2 = pygame.transform.scale(scate2, (ch_width+5, ch_height+20)).convert_alpha()


timetick = pygame.time.Clock()
play = False
num_i,num_j = 8,6
FPS,timer,time_of_over = 15,0,0
y0 = 374
i,j,t,remp,temp=0,1,10,5,0
he_of_jump = 55
chx,chy,bgx1,bgx2,obj_x,x,y,restartimgx,restartimgy = 300,y0,0,width,width,None,None,39,95 # Initializing positions of characters and icons
bg_speed,ch_speed,vy = -20,0,10 # Character speed and background speed
not_exit_game,jumping,fi_jump,game_over,restart,movement,restart,launching = True,False,True,False,False,True,False,False
listbg,listobj,listcoin,listlift = [bgx1,bgx2],[],[],[]
ind = width
rlift = False
not_in_lift = False
tenter = 0
ju = True
font_size = 40
score = 0
h_score_file,coin_file = path+'h_score.txt',path+'coins.txt'
scatek= False # By Initialising this variable, we mean that scateboard is not available for player yet, if this variable gets True then we will have scateboard
var = 0
coinposx = width-150 
