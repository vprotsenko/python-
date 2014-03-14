'''In process of development'''

import pygame, sys, os, time
from pygame.locals import *
from random import randint, choice
import numpy

speed=1
rows, cols = 25, 25
matrix = [[ 0 for c in range(cols)] for r in range(rows)]	
screen=pygame.display.set_mode((cols*10,rows*10),0,32)		
background=pygame.image.load(bif).convert()					
def DisplayGame(): 
	screen.lock()
	for c in range(rows):							
		for b in range(cols):						
			if matrix[c][b]==1 or matrix[c][b]==2:	
				pygame.draw.rect(screen, (120,240,130), Rect((b*10,c*10+10), (9,9))) 
	pygame.display.update()
	screen.unlock()

GameOver=True
while GameOver:
	vertical=0 		
	horizont=cols/2  		
	yes=True		

	x_positions=[5,6,7,8]
	y_positions=[5,5,5,5]

	direct=4
	yscale=5
	xscale=5
	while yes:
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
			time.sleep(float(0.05))

		for i in range(len(x_positions)):
			matrix[y_positions[i]][x_positions[i]]=0
		x_positions.append(xscale)
		y_positions.append(yscale)
		
		if len(x_positions)>1:
			del x_positions[0]
			del y_positions[0]
		print x_positions, y_positions, len(x_positions)
		
		if direct==1:
			yscale=yscale-1
		elif direct==2:
			xscale=xscale-1
		elif direct==3:
			xscale=xscale+1
		elif direct==4:
			yscale=yscale+1
		for i in range(len(x_positions)):
			matrix[y_positions[i]][x_positions[i]]=1

		DisplayGame()
