'''
Pygame Python module should be installed for starting game.
 http://www.pygame.org/download.shtml

http://youtu.be/Jwhobv8UyX4?t=8s      <----Watch it on youtube
'''

import pygame, sys, os, time
from pygame.locals import *
from random import randint, choice
import numpy

speed=1
rows, cols = 25, 15
matrix = [[ 0 for c in range(cols)] for r in range(rows)]	# Size of the game matrix
screen=pygame.display.set_mode((cols*10,rows*10),0,32)		# Size of the game window
background = pygame.Surface(screen.get_size()) 			#Background of game
background = background.convert()
background.fill((10, 10, 10))					#Background color
#-----------Functions block------------------
def DisplayGame(): #Responsible for displaying position of figures on game field
	screen.lock()
	for c in range(rows):							
		for b in range(cols):						
			if matrix[c][b]==1 or matrix[c][b]==2:	
				pygame.draw.rect(screen, (120,240,130), Rect((b*10,c*10+10), (9,9))) #Description and position of basic figure
	pygame.display.update()
	screen.unlock()
def move_cube(l,r,xscale,yscale): # Change position of basic figure  
	xscale=xscale+l+r
	if l+r==0: matrix[yscale][xscale]=2 # No left/right movements
	elif l+r==1: matrix[yscale][xscale-1]=2 #move right
	elif l+r==-1: matrix[yscale][xscale+1]=2 #move left
def attach_fig_to_body(yes):	# Internal operation (not visible for gamer)
	if yes==False:				# When figure touch button it converts from "2" to "1"
		for r in range(rows):
			for c in range(cols):
				if matrix[r][c]==2:	matrix[r][c]=1
def clean_up():					# This function clean previous position of figure 
	for r in range(rows):
		for c in range(cols):
			if matrix[r][c]==2:	matrix[r][c]=0
def vertical_limit(v_position): # Let the figure feel button
	if v_position==rows-1: 
		return True
	for r in range(rows):
		for c in range(cols):
			if matrix[r][c]==2:
				if r<rows-2:
					if matrix[r+1][c]==1:
						return True	
				else:
					return True
def horisontal_limit(): # Check horisont before making next left/right movement
	for r in range(rows):
		for c in range(cols):
			if matrix[r][c]==2 and matrix[r][c-1]==1:
				return 1
			elif matrix[r][c]==2 and matrix[r][c+1]==1:
				return 2
			elif  matrix[r][0]==2:
				return 1
			elif  matrix[r][cols-1]==2:
				return 2
def position_limit(p): # This function limit possible number of figure positions (1-4)
	if p>4:
		p=1 
		return p
	elif p<1:
		p=4
		return p
	else:
		return p
def fig1(l,r,h,v,p):
	if p==1:   move_cube(l,r,h,v), move_cube(l,r,h,v-1), move_cube(l,r,h+1,v), move_cube(l,r,h-1,v)	
	elif p==2: move_cube(l,r,h,v), move_cube(l,r,h,v-1), move_cube(l,r,h,v+1), move_cube(l,r,h+1,v)		 #
	elif p==3: move_cube(l,r,h,v), move_cube(l,r,h,v+1), move_cube(l,r,h+1,v), move_cube(l,r,h-1,v)		###	
	elif p==4: move_cube(l,r,h,v), move_cube(l,r,h,v-1), move_cube(l,r,h,v+1), move_cube(l,r,h-1,v)	
def fig2(l,r,h,v,p):
	if p==1:   move_cube(l,r,h,v), move_cube(l,r,h,v-1),move_cube(l,r,h-1,v),move_cube(l,r,h-1,v+1)		#
	elif p==2: move_cube(l,r,h,v), move_cube(l,r,h-1,v-1), move_cube(l,r,h,v-1),move_cube(l,r,h+1,v)	#
	elif p==3: move_cube(l,r,h,v), move_cube(l,r,h,v-1),move_cube(l,r,h-1,v),move_cube(l,r,h-1,v+1)		##
	elif p==4: move_cube(l,r,h,v), move_cube(l,r,h-1,v-1), move_cube(l,r,h,v-1),move_cube(l,r,h+1,v)
def fig3(l,r,h,v,p):
	if p==1:   move_cube(l,r,h,v), move_cube(l,r,h,v-1), move_cube(l,r,h,v+1), move_cube(l,r,h-1,v+1)	 #
	elif p==2: move_cube(l,r,h,v), move_cube(l,r,h+1,v), move_cube(l,r,h-1,v), move_cube(l,r,h-1,v-1)	 #
	elif p==3: move_cube(l,r,h,v), move_cube(l,r,h,v-1), move_cube(l,r,h,v+1), move_cube(l,r,h+1,v-1)	##
	elif p==4: move_cube(l,r,h,v), move_cube(l,r,h-1,v), move_cube(l,r,h+1,v), move_cube(l,r,h+1,v+1)	
def fig4(l,r,h,v,p):
	if p==1:   move_cube(l,r,h,v), move_cube(l,r,h,v-1), move_cube(l,r,h,v+1), move_cube(l,r,h+1,v+1)	#
	elif p==2: move_cube(l,r,h,v), move_cube(l,r,h+1,v), move_cube(l,r,h-1,v), move_cube(l,r,h-1,v+1)	##
	elif p==3: move_cube(l,r,h,v), move_cube(l,r,h,v-1), move_cube(l,r,h,v+1), move_cube(l,r,h-1,v-1)	 #
	elif p==4: move_cube(l,r,h,v), move_cube(l,r,h+1,v), move_cube(l,r,h-1,v), move_cube(l,r,h+1,v-1)
def fig5(l,r,h,v,p):
	if p==1:   move_cube(l,r,h,v), move_cube(l,r,h,v-1), move_cube(l,r,h,v+1), move_cube(l,r,h-1,v+1)	 #
	elif p==2: move_cube(l,r,h,v), move_cube(l,r,h+1,v), move_cube(l,r,h-1,v), move_cube(l,r,h-1,v-1)	##
	elif p==3: move_cube(l,r,h,v), move_cube(l,r,h,v-1), move_cube(l,r,h,v+1), move_cube(l,r,h+1,v-1)	#
	elif p==4: move_cube(l,r,h,v), move_cube(l,r,h+1,v), move_cube(l,r,h-1,v), move_cube(l,r,h+1,v+1)
def fig6(l,r,h,v,p):
	if p==1:   move_cube(l,r,h,v), move_cube(l,r,h,v-1), move_cube(l,r,h,v+1)  #stick  
	elif p==2: move_cube(l,r,h,v), move_cube(l,r,h+1,v), move_cube(l,r,h-1,v)
	elif p==3: move_cube(l,r,h,v), move_cube(l,r,h,v-1), move_cube(l,r,h,v+1)	###
	elif p==4: move_cube(l,r,h,v), move_cube(l,r,h+1,v), move_cube(l,r,h-1,v)
def fig7(l,r,h,v,p):
	move_cube(l,r,h,v), move_cube(l,r,h,v-1), move_cube(l,r,h+1,v-1),move_cube(l,r,h+1,v) #   cube																						  ##
def rotation(h,v): # Check posibility to rotate figure
	if h<cols-1:
		if matrix[v][h+1]!=1:
			if matrix[v][h-1]!=1 and matrix[v-1][h-1]!=1 and matrix[v-1][h]!=1 and matrix[v-1][h+1]!=1 and matrix[v+1][h-1]!=1 and matrix[v+1][h]!=1 and matrix[v+1][h+1]!=1:
				return True
			else:
				return False
	else:
		return False
def get_figure(l,r,h,v,p,n): 
	if n==1: fig1(l,r,h,v,p)
	elif n==2: fig2(l,r,h,v,p)
	elif n==3: fig3(l,r,h,v,p)
	elif n==4: fig4(l,r,h,v,p)
	elif n==5: fig5(l,r,h,v,p)
	elif n==6: fig6(l,r,h,v,p)
	elif n==7: fig7(l,r,h,v,p)
def search_full_line(): # Making searsh for full line and killing it
	for i in range(rows):
		a=0
		for c in range(cols):
			if matrix[i][c]!=0 and matrix[i][c]!=2:
				a=a+matrix[i][c]
				if a==cols:
					del matrix[i]
					zero=[0 for s in range(cols)]
					matrix.insert(0,zero)
#--------Start code---------------------------
right=left=0 
GameOver=True
#---First level loop--------------------------
while GameOver:
	vertical=0 		# y scale start position
	horizont=cols/2 	# x scale start position
	speed_up=1 		# increasing speed during KEY_DOWN
	yes=True		
	figure=randint(1,7)		# Get next figure	
	position=randint(0,4)	# Get start position of next figure
	#---Second level loop--------------------------
	while yes:
		vertical=vertical+1
		horisontal_limit()
		#---Third level loop--------------------------
		for z in range(5):
			screen.blit(background,(0,0))
			for event in pygame.event.get():
				screen.blit(background,(0,0))
				if event.type ==QUIT:
					pygame.quit()
					sys.exit()
				if event.type==KEYDOWN:
					if event.key==K_UP:
						if rotation(horizont,vertical)==True:
							position=position+1
					elif event.key==K_LEFT:
						left=-1					
					elif event.key==K_RIGHT:
						right=1
					elif event.key==K_DOWN:
						speed_up=10
			rotation(horizont,vertical)
			if horisontal_limit()==1:
				left=0
			elif horisontal_limit()==2:
				right=0
			clean_up()
			time.sleep(float(0.1)/speed/speed_up)
			position=position_limit(position)
			get_figure(left,right,horizont,vertical,position,figure)
			horizont=horizont+left+right
			left=right=0
			DisplayGame()
		if vertical_limit(vertical)==True:
			yes=False
		attach_fig_to_body(yes)
		search_full_line()
	if vertical==1:
		print "Game over"
		time.sleep(20)
		GameOver=False
