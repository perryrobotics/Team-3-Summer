#!/usr/bin/python
import os, sys
from wallaby import *
from library import *

def left_path():
	move_back(1500, 50)
	close_claw(50)
	move_back(1500, 700)
	move_right(1000, 50)
	right_to_white(1000)
	move_right(750, 150)
	move(1500, 300)
	top_arm(50)
	move(1500, 1300)
	open_claw(50)
	move_back(1000, 3000)
	up_arm(50)
	move_right(1000, 250)
	down_arm(50)