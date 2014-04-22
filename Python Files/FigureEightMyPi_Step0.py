#####################################################################
# Seven Segments of Pi - FigureEightMyPi_Step0.py                   #
#####################################################################
# Description:-                                                     #
# Seven Segments of Pi Challenge                                    #
# Software for the Game "Figure Eight My Pi"                        #
# Runs on Seven Segments of Pi Games Console                        #
# When PushButton is pressed                                        #
# GPIOs drive Seven Segment Display Segments a,b,c,d,e,f in turn    #
# with each Segment illuminated for 0.5 seconds                     #
# so "PiSeg" appears to go round in a clockwise "Figure Zero"       #
#####################################################################

#!/usr/bin/env python    #allows program to be run from command line

import time              #time package allows programmable delays in the software
import RPi.GPIO as GPIO  #RPi.GPIO package allows control of GPIO by software
GPIO.setmode(GPIO.BOARD) #Sets RPi.GPIO package to number GPIO by their Raspberry Pi Connector pin number
GPIO.setwarnings(False)  #Disables GPIO Warning Messages

GPIO.setup(7, GPIO.IN)   #GPIO 7 is input from Push Button Switch
                         #                                          _______
GPIO.setup(11, GPIO.OUT) #GPIO 11 output illuminates Segment a     |   a   |
GPIO.setup(12, GPIO.OUT) #GPIO 12 output illuminates Segment b    f|       |b
GPIO.setup(13, GPIO.OUT) #GPIO 13 output illuminates Segment c     |_______|
GPIO.setup(15, GPIO.OUT) #GPIO 15 output illuminates Segment d     |   g   |
GPIO.setup(16, GPIO.OUT) #GPIO 16 output illuminates Segment e    e|       |c
GPIO.setup(18, GPIO.OUT) #GPIO 18 output illuminates Segment f     |_______|
GPIO.setup(22, GPIO.OUT) #GPIO 22 output illuminates Segment g         d
        
poll = .1                           # Define Constant for PushButton 'poll' delay
delay = .5                          # Define Constant for step delay

###################################################
# Start of "Figure Eight My Pi" Program Execution #
###################################################

# start with all Segments off
GPIO.output(11, False)              # a 
GPIO.output(12, False)              # b
GPIO.output(13, False)              # c
GPIO.output(15, False)              # d
GPIO.output(16, False)              # e
GPIO.output(18, False)              # f
GPIO.output(22, False)              # g

print "Press PushButton to Start"   # Printed on Raspberry Pi *Python Shell* Window
PushButton = False                  # wait until PushButton has been pressed before starting main state machine
while PushButton == False:          # if PushButton has been pressed...
    PushButton = GPIO.input(7)      # Check PushButton input
    time.sleep(poll)                # if not, wait for 0.1 second before checking PushButton again
state = "a"                         # Start State Machine in state "a"

# start of main state machine
while True:                         # while True: means run this loop forever
    
    if state == "a":                ####### state "a" ######
        print state                 # prints name of state - comment this line out once it is working
        GPIO.output(11, True)       # turn on Segment 'a'
        time.sleep(delay)           # after a delay
        GPIO.output(11, False)      # turn off Segment 'a'
        state = "b"                 # then move to state 'b' which is the next Segment clockwise

    if state == "b":                ####### state "b" ######
        print state                 # prints name of state - comment this line out once it is working
        GPIO.output(12, True)       # turn on Segment 'b'
        time.sleep(delay)           # after a delay
        GPIO.output(12, False)      # turn off Segment 'b'
        state = "c"                 # then move to state 'c' which is the next Segment clockwise

    if state == "c":                ####### state "c" ######
        print state                 # prints name of state - comment this line out once it is working
        GPIO.output(13, True)       # turn on Segment 'c'
        time.sleep(delay)           # after a delay
        GPIO.output(13, False)      # turn off Segment 'c'
        state = "d"                 # then move to state 'd' which is the next Segment clockwise

    if state == "d":                ####### state "d" ######
        print state                 # prints name of state - comment this line out once it is working
        GPIO.output(15, True)       # turn on Segment 'd'
        time.sleep(delay)           # after a delay
        GPIO.output(15, False)      # turn off Segment 'd'
        state = "e"                 # then move to state 'e' which is the next Segment clockwise
        
    if state == "e":                ####### state "e" ######
        print state                 # prints name of state - comment this line out once it is working
        GPIO.output(16, True)       # turn on Segment 'e'
        time.sleep(delay)           # after a delay
        GPIO.output(16, False)      # turn off Segment 'e'
        state = "f"                 # then move to state 'f' which is the next Segment clockwise

    if state == "f":                ####### state "f" ######
        print state                 # prints name of state - comment this line out once it is working
        GPIO.output(18, True)       # turn on Segment 'f'
        time.sleep(delay)           # after a delay
        GPIO.output(18, False)      # turn off Segment 'f'
        state = "a"                 # then move back to state 'a' which is the next Segment clockwise



