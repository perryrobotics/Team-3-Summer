3#!/usr/bin/python
import os, sys
from wallaby import *

RED_PEOPLE = 2
Lmotor = 3
Rmotor = 0

Arm = 0
Arm_up = 1000
Arm_down = 500
Arm_top = 1050
Arm_st = 1800

Claw = 2
Claw_open = 1000
Claw_close = 2040

    
Side = 3
Side_Down = 1300
Side_Up = 300
    
Touch_port = 0
Line_port = 0
Side_port = 1
Thresh = 2500
    
def move(speed, ticks):
	cmpc(Lmotor)
	mav(Lmotor, speed);
	mav(Rmotor, speed);
	while gmpc(Lmotor) < ticks:
		pass
	ao()
            
def move_back(speed, ticks):
	cmpc(Lmotor)
	mav(Lmotor, -speed);
	mav(Rmotor, -speed);
	while gmpc(Lmotor) > -ticks:
		pass
	ao()

def move_left(speed, ticks):
	cmpc(Rmotor)
  	cmpc(Lmotor)
	mav(Lmotor,-speed)
	mav(Rmotor, speed)
	while gmpc(Rmotor) < ticks:
		pass
	ao()

def move_right(speed, ticks):
	cmpc(Lmotor)
	mav(Lmotor, speed)
	mav(Rmotor, -speed)
	while gmpc(Lmotor) < ticks:
		pass
	ao()
            
def drive_to_black(speed):
	mav(Rmotor, speed)
  	mav(Lmotor, speed)
  	while analog(Line_port) < Thresh:
		pass
	ao()
      
def back_to_black(speed):
	mav(Rmotor, -speed)
  	mav(Lmotor, -speed)
  	while analog(Line_port) < Thresh:
		pass
	ao()
            
def drive_to_white(speed):
	mav(Rmotor, speed)
  	mav(Lmotor, speed)
  	while analog(Line_port) > Thresh-1000:
		pass
	ao()   
            
def back_to_white(speed):
	mav(Rmotor, -speed)
  	mav(Lmotor, -speed)
  	while analog(Line_port) > Thresh-1000:
		pass
	ao()  
            
def line_follow(speed, distance):
	cmpc(Rmotor)
	cmpc(Lmotor)
	while gmpc(Lmotor)<distance:
		if analog(Line_port)> Thresh:
			mav(Rmotor, speed)
			mav(Lmotor, speed-200)
		elif analog(Line_port)<Thresh:
			mav(Rmotor, speed-100)
			mav(Lmotor, speed)
	mav(Lmotor, 0)
	mav(Rmotor, 0)
                
def side_follow(speed, distance):
	cmpc(Rmotor)
	cmpc(Lmotor)
	while gmpc(Lmotor)<distance:
		if analog(Side_port)> Thresh:
			mav(Rmotor, speed)
			mav(Lmotor, speed-200)
		elif analog(Side_port)<Thresh:
			mav(Rmotor, speed-100)
			mav(Lmotor, speed)
	mav(Lmotor, 0)
	mav(Rmotor, 0)
            
def move_to_hit(speed):
	mav(Rmotor, speed)
  	mav(Lmotor, speed)
	while digital(Touch_port) ==0:
		pass
	ao()
            
def right_to_black(speed):
	mav(Lmotor, speed)
	mav(Rmotor, -speed)
	while analog(Line_port) < Thresh:
		pass
	ao()   
            
def left_to_black(speed):
	mav(Lmotor, -speed)
	mav(Rmotor, speed)
	while analog(Line_port) < Thresh:
		pass
	ao()  
      
def right_to_white(speed):
	mav(Lmotor, speed)
	mav(Rmotor, -speed)
	while analog(Line_port) > Thresh:
		pass
	ao() 
            
def left_to_white(speed):
	mav(Lmotor, -speed)
	mav(Rmotor, speed)
	while analog(Line_port) > Thresh:
		pass
	ao()  
            
def center_red():
	camera_open()
	for x in range (15):
		camera_update()
		msleep(100)
 	point = get_object_center(RED_PEOPLE, 0)
  	while(point.x < 100 or point.x > 120):
		camera_update()
		point = get_object_center(RED_PEOPLE, 0)
		print("X: ", point.x,"DIR: ")
		if point.x < 100:
			mav(Lmotor, -100)
			mav(Rmotor, 100)
			print("Left \n")
		elif point.x>120:
			mav(Lmotor, 100)
			mav(Rmotor, -100)
			print("Right: \n")
		else:
			mav(Lmotor,0)
			mav(Rmotor,0)
			print ("CENTERED!!")
			break
            
            
def move_servo_slow(port, start_pos, end_pos, step):
	if  end_pos < start_pos:
		step=-step
  	for pos in range(start_pos, end_pos, step):
		set_servo_position(port, pos)
		msleep(50)
 	set_servo_position(port, end_pos)

def open_claw(step):
	move_servo_slow(Claw, get_servo_position(Claw), Claw_open, step)            
   
def close_claw(step):
  	move_servo_slow(Claw, get_servo_position(Claw), Claw_close, step)
        
def half_claw(step):
  	move_servo_slow(Claw, get_servo_position(Claw), Claw_half, step)
        
def almost_claw(step):
	move_servo_slow(Claw, get_servo_position(Claw), Claw_almost, step)
        
def up_side(step):
	move_servo_slow(Side, get_servo_position(Side), Side_Up, step)
        
def down_side(step):
	move_servo_slow(Side, get_servo_position(Side), Side_Down, step)
        
def down_arm(step):
	move_servo_slow(Arm, get_servo_position(Arm), Arm_down, step)
        
def up_arm(step):
	move_servo_slow(Arm, get_servo_position(Arm), Arm_up, step)
        
def top_arm(step):
	move_servo_slow(Arm, get_servo_position(Arm), Arm_top, step)
        
def st_arm(step):
	move_servo_slow(Arm, get_servo_position(Arm), Arm_st, step)