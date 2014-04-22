##################################################################
# Seven Segments of Pi – OneTwoThree.py                          #
##################################################################
# Description:-                                                  #
# When PushButton is pressed                                     #
# GPIOs drive Seven Segment Display with numbers 1, 2, 3         #
# with 1 second delay between numbers as a simple Counter        #
##################################################################
#!/usr/bin/env python #allows program to be run from command line

import time #time package allows programmable delays in the software

import RPi.GPIO as GPIO #RPi.GPIO package allows control of GPIO by software

GPIO.setmode(GPIO.BOARD) #RPi.GPIO package numbers GPIO by their Raspberry Pi Connector pin number

GPIO.setwarnings(False) #Disables GPIO Warning Messages

GPIO.setup(7, GPIO.IN) #GPIO 7 is input from Push Button Switch
#                                                                           _______
GPIO.setup(11, GPIO.OUT) #GPIO 11 output illuminates Segment a             |   a   |
GPIO.setup(12, GPIO.OUT) #GPIO 12 output illuminates Segment b            f|       |b
GPIO.setup(13, GPIO.OUT) #GPIO 13 output illuminates Segment c             |_______|
GPIO.setup(15, GPIO.OUT) #GPIO 15 output illuminates Segment d             |   g   |
GPIO.setup(16, GPIO.OUT) #GPIO 16 output illuminates Segment e            e|       |c
GPIO.setup(18, GPIO.OUT) #GPIO 18 output illuminates Segment f             |_______|
GPIO.setup(22, GPIO.OUT) #GPIO 22 output illuminates Segment g                 d

def one(): # Define function 'one' which makes GPIO b,c = True to display number '1'
    GPIO.output(11, False) # a
    GPIO.output(12, True) # b
    GPIO.output(13, True) # c
    GPIO.output(15, False) # d
    GPIO.output(16, False) # e
    GPIO.output(18, False) # f
    GPIO.output(22, False) # g

def two(): # Define function 'two' which makes GPIO a,b,d,e,g = True to display number '2'
    GPIO.output(11, False) # a
    GPIO.output(12, False) # b
    GPIO.output(13, False) # c
    GPIO.output(15, False) # d
    GPIO.output(16, False) # e
    GPIO.output(18, False) # f
    GPIO.output(22, False) # g

def three(): # Define function 'three' which makes GPIO a,b,c,d,g = True to display number '3'
    GPIO.output(11, False) # a
    GPIO.output(12, False) # b
    GPIO.output(13, False) # c
    GPIO.output(15, False) # d
    GPIO.output(16, False) # e
    GPIO.output(18, False) # f
    GPIO.output(22, False) # g

def SevenSeg(x): # Define function 'SevenSeg' which calls function 'one' 'two' or 'three' depending on 'x'
    if x == 1:
        one()
    elif x == 2:
        two()
    elif x == 3:
        three()

poll = .1 # Define Constant for PushButton 'poll' delay

delay = 1 # Define Constant for Counter delay

# Start of Counter 1, 2, 3 Program Execution
print "Press PushButton to Start" # Printed on Raspberry Pi *Python Shell* Window

while True: # while True: means run this loop forever
    PushButton = GPIO.input(7) # Check PushButton input
    if PushButton == False: # if PushButton has not been pressed
        time.sleep(poll) # wait 0.1 of a second before checking (polling) again
    else: # else PushButton has been pressed, so
        print "One" # Print "One" on Raspberry Pi *Python Shell* Window
        SevenSeg(1) # Call function 'SevenSeg' with a value of x=1
        time.sleep(delay) # wait a second
        print "Two" # Print "Two" on Raspberry Pi *Python Shell* Window
        SevenSeg(2) # etc
        time.sleep(delay)
        print "Three"
        SevenSeg(3)
time.sleep(delay)
