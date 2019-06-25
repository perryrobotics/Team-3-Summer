#!/usr/bin/python
import os, sys
from wallaby import *
from library import *
from wait_for_start import *
from left import *
from right import *

YELLOW = 0
RED = 1
RIGHT = 0
LEFT = 1

sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
enable_servos()
open_claw(50)
up_arm(50)
msleep(5000)
#wait_for_start(1)
move_back(1500,2000)
close_claw(50)
down_arm(50)
#away from create
move_back(1500,7000)
move(1000,900)
move_right(1500,1500)
move_back(1500,3000)
move(1500, 4500)
up_arm(50) #avoid PVC
#left_to_black(1500)
#left_to_white(1000)
move_left(1500,2200)
move_back(1500,3000)
down_arm(50)
open_claw(50)
#set to get supplies
line_follow(1000,15000)
#move(1500, 7000)
#move_left(1000, 500)
#move(1500, 7000)
 
camera_open()
side = RIGHT
for x in range(15):
	camera_update()
	msleep(50)

for pic in range(15):
	camera_update()
	if get_object_count(YELLOW) > 0 and get_object_count(RED) > 0:
		area = get_object_area(YELLOW, 0)
		print "AREA: ", area
		if area > 50:
			side = LEFT

camera_close()

if side == RIGHT:
	print ("RIGHT BURNING!\n")
	right_path()
else:
	print("LEFT BURNING!!\n")
	left_path()

