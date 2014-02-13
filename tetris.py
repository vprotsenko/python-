#!/usr/bin/python
bif="bg.jpg"

import pygame, sys, time
from pygame.locals import *
from random import randint, choice

screen=pygame.display.set_mode((320,400),0,32)
background=pygame.image.load(bif).convert()



def fig1(x,y,p):
	if p==1:				
		size1=(10,20);
		size2=(10,10);
		part1=(x+10,y+10);
		part2=(x,y)

	screen.lock()
	pygame.draw.rect(screen, (140,240,130), Rect(part2, size2))
	screen.unlock()


def get_figure(x,y,p,fig_type):
	if fig_type==1:
		fig1(x,y,p)
	elif fig_type==2:
		f2=fig2(x,y,p)
	elif fig_type==3:
		f3=fig3(x,y,p)
	elif fig_type==4:
		f4=fig4(x,y,p)

while True:
	start_point=100
	position=randint(1,4)
	fig_type=randint(1,4)
	speed=4
	finish=True
	horizont=100

	while finish:

		start_point=start_point+10

	
		for i in range(5):
			screen.blit(background,(0,0))
			for event in pygame.event.get():
				if event.type ==QUIT:
					pygame.quit()
					sys.exit()
				if event.type==KEYDOWN:
					if event.key==K_UP:
						position=position+1				
					elif event.key==K_LEFT:
						horizont=horizont-10
					elif event.key==K_RIGHT:
						horizont=horizont+10
				
			if position>4:
				position=1

			get_figure(horizont,start_point,1,1)
			pygame.display.update()
			time.sleep(float(1/(float(speed)*5)))




		if start_point>380:
			finish=False