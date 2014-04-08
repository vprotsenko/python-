
import pygame, sys, os, time
from pygame.locals import *
from random import randint, choice



speed=1
rows, cols = 15, 25


matrix = [[ 0 for c in range(cols)] for r in range(rows)]	
screen=pygame.display.set_mode((cols*10,rows*10),0,32)		
background = pygame.Surface(screen.get_size()) 			#Background of game
background = background.convert()
background.fill((10, 10, 10))					
def DisplayGame(): 
	screen.lock()
	for c in range(rows):							
		for b in range(cols):						
			if matrix[c][b]==1:	
				pygame.draw.rect(screen, (120,240,130), Rect((b*10,c*10), (9,9)))
			if matrix[c][b]==2:
				pygame.draw.rect(screen, (220,40,230), Rect((b*10,c*10), (9,9)))
	pygame.display.update()
	screen.unlock()

def frame(x,y):
	if x==cols or x==-1 or y==-1 or y==rows:
		print x, y
		return False
	else:
		return True
def food():
	count=0
	for r in range(rows-1):							
		for c in range(cols):						
			if matrix[r][c]==2:
				count=1
	if count==0:
		a=randint(0,rows-1)
		b=randint(0,cols-1)
		matrix[a][b]=2
def claenOldStep(x_positions,y_positions,xscale,yscale):
	for i in range(len(x_positions)):
		matrix[y_positions[i]][x_positions[i]]=0

	x_positions.append(xscale)
	y_positions.append(yscale)
	if direct==1:
		if matrix[yscale-1][xscale]!=2:
			print xscale,yscale
			del x_positions[0]
			del y_positions[0]
	if direct==2:
		if matrix[yscale][xscale-1]!=2:
			print xscale,yscale
			del x_positions[0]
			del y_positions[0]
	if direct==3:
		if matrix[yscale][xscale+1]!=2:
			print xscale,yscale
			del x_positions[0]
			del y_positions[0]
	if direct==4:
		if matrix[yscale+1][xscale]!=2:
			print xscale,yscale
			del x_positions[0]
			del y_positions[0]			
def newPosition(x_positions,y_positions):
		for i in range(len(x_positions)):
			matrix[y_positions[i]][x_positions[i]]=1

GameOver=True
while GameOver:

	x_positions=[10]
	y_positions=[10]

	count=0
	direct=3
	yscale=x_positions[0]
	xscale=y_positions[0]


	while GameOver:
		for i in range(15):
			screen.blit(background,(0,0))
			for event in pygame.event.get():
				screen.blit(background,(0,0))
				if event.type ==QUIT:
					pygame.quit()
					sys.exit()
				if event.type==KEYDOWN:
					if event.key==K_UP:
						if direct!=4:
							direct=1
					elif event.key==K_LEFT:
						if direct!=3:
							direct=2						
					elif event.key==K_RIGHT:
						if direct!=2:	
							direct=3
					elif event.key==K_DOWN:
						if direct!=1:
							direct=4
			time.sleep(float(0.02))


		claenOldStep(x_positions,y_positions,xscale,yscale)

		if direct==1: #UP
			yscale=yscale-1
		elif direct==2: #Left
			xscale=xscale-1
		elif direct==3: #Right
			xscale=xscale+1
		elif direct==4: #Down
			yscale=yscale+1





		newPosition(x_positions,y_positions)
		food()
		GameOver=frame(xscale,yscale)
		DisplayGame()
		#debug
		print "+++++++++++++++++++++++++++++++++++++++++++++++"
		for c in range(rows):							
			print matrix[c]
