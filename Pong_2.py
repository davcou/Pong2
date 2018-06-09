import pygame
import time
import random

pygame.init()

""" define colours and other static entities"""
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

#Define display height and width
display_width = 800
display_height  = 600

#Define paddel height and width. higher means easier. Also velocity.
paddle_width = 10
paddle_height = 140
paddle_vel = 10

#reate display slash surface
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pong')

clock = pygame.time.Clock()

block_size = 10
FPS = 30
font = pygame.font.SysFont(None, 25)

#class ball():

#    def __init__(self)
#
#    def update(posX, posY, velX, velY):
#    	if posY<0:
#	    velY = -velY
#    	if posX == 0 + paddle_width:
#	    #check if crash or not
#   	 if posX == display_width - paddle_width:
#	    #Check if crash or not
#  	 else:
#	    posX += velX
#	    posY += velY


def update_ball(pos, vel):
    """ Function to update the ball """
    if pos[1]<0 or pos[1]>display_height-10:
	vel[1] = -vel[1]
	pos[0] += vel[0]
	pos[1] += vel[1]
	return pos, vel
	
    if pos[0] <= 0 + paddle_width:
	vel[0] = -vel[0]
	pos[0] += vel[0]
	pos[1] += vel[1]
	return pos, vel
    if pos[0] >= display_width - 2*paddle_width:
	vel[0] = -vel[0]
	pos[0] += vel[0]
	pos[1] += vel[1]
	return pos, vel
    else:
	pos[0] += vel[0]
	pos[1] += vel[1]
	return pos, vel


def message_to_screen(msg,color):
    """Function that prints to screen"""
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])


def gameLoop():
    gameExit = False
    gameOver = False

    """Spawn ball. Velocity is not working right at the moment"""
    pos = [0, 0]
    pos[0] = display_width/2
    pos[1] = display_height/2
    vel = [0,0]
    vel[0] = random.randrange(-10, 11, 20)
    vel[1] = random.randrange(-10, 11, 20)
    ball = pygame.draw.rect(gameDisplay, red, [pos[0], pos[1], block_size,block_size])

    pad1pos = display_height/2
    pad2pos = display_height/2
    padvel = 40

    while not gameExit:

	while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()

	    for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

	#Define event handlers for paddle movement.
	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
                gameExit = True
	    if event.type == pygame.KEYDOWN:		   
	        if event.key == pygame.K_UP:
		    pad1pos += -padvel
 		if event.key == pygame.K_DOWN:
		    pad1pos += padvel
	        if event.key == pygame.K_w:
		    pad2pos += -padvel
	        if event.key == pygame.K_s:
		    pad2pos += padvel
	        if event.type == pygame.K_o:
		    gameExit = True
		    gameOver = False

	#Update ball
	print(pos)
	print(pad1pos)
	print(pad1pos+ paddle_height/2)
	print(pad1pos- paddle_height/2)
	print(pad2pos)
	print(pad2pos+ paddle_height/2)
	print(pad2pos- paddle_height/2)
	pos, vel = update_ball(pos, vel)
	
	#Check collision
	if pos[0] == 0 + paddle_width:
	    if pad1pos - paddle_height/2 <= pos[1] <= pad1pos + paddle_height/2:
		print("Hit")
	    elif pos[1] > pad1pos + paddle_height/2:
		gameOver = True
		print("miss", pos[1], pad1pos)
	    elif pos[1] < pad1pos - paddle_height/2:
		gameOver = True
		print("miss", pos[1], pad1pos-paddle_height)

	if pos[0] == display_width - 2*paddle_width:
	    if pad2pos - paddle_height/2 <= pos[1] <= pad2pos+paddle_height/2:
		print("Hit")
	    elif pos[1] > pad2pos+paddle_height/2:
		gameOver = True
		print("miss")
		print(pad2pos)
		print(pad2pos- paddle_height)
	    elif pos[1] < pad2pos - paddle_height/2:
		gameOver = True
		print("miss")
		print(pad2pos)
		print(pad2pos- paddle_height)


	
	
	#Draw everything
	gameDisplay.fill(white)
	pygame.draw.rect(gameDisplay, red, [pos[0], pos[1], block_size,block_size])
	pygame.draw.rect(gameDisplay, green, [0, pad1pos-paddle_height/2, paddle_width,paddle_height])
	pygame.draw.rect(gameDisplay, red, [display_width-paddle_width, pad2pos-paddle_height/2, paddle_width,paddle_height])
	pygame.display.update()
	

	clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()



