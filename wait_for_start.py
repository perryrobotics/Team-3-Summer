#!/usr/bin/python
import os, sys
from wallaby import *

def wait_for_start(port):   
	#START CALIBRATION WITH LIGHT OFF
	print "LIGHT OFF NOW!!!.  Press A when light is off!"
  	while not a_button():
		off = analog(port)
		#print ("OFF: ",analog(port) )
 	print ("LIGHT OFF VALUE: ", off)
	if off <1500:
		print ("BAD CALIBRATION!!!  DO NOT RUN!!!")
		return False
	
	#NOW CLIBRATE WITH LIGHT ON
	print("LIGHT ON NOW!!!.  Press B when light is on!")
  	while not b_button():
		on = analog(port)
		#print ("ON: ",analog(port) )
 	print ("LIGHT ON VALUE: ", on)
	if on >1000:
		print ("BAD CALIBRATION!!!  DO NOT RUN!!!")
		return False

	print ("TURN LIGHT OFF NOW!!!! PRESS C WHEN READY")
  	while c_button()==0:
		pass
   	#NOW CALCULATE THE THRESHHOLD VALUE 
	thresh = (off + on)/2
	if thresh < 1000:
		print "BAD CALIBRATION!!!!DO NOT RUN!!!"
		return False
	
	print("GOOD CALIBRATION!  LETS GO!!!")
	print("ON VAL:",on)
	print("OFF VAL: ", off)
	print("THRESH: ", thresh)
	print ("WAITING FOR LIGHT!!!")
	while analog(port) > thresh:
		pass
	return True