import time #time package allows programmable delays in the software

import RPi.GPIO as GPIO #RPi.GPIO package allows control of GPIO by software

import pygame #imports the modules needed to play sound

import random

randomNumber = 0

pygame.init() #initialises pygame
pygame.mixer.pre_init(44100,-16,2,512)
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

def blank(): # Define function 'one' which makes all GPIO's  = False to display blank
    GPIO.output(11, False) # a
    GPIO.output(12, False) # b
    GPIO.output(13, False) # c
    GPIO.output(15, False) # d
    GPIO.output(16, False) # e
    GPIO.output(18, False) # f
    GPIO.output(22, False) # g

def one(): # Define function 'one' which makes GPIO b,c = True to display number '1'
    GPIO.output(11, False) # a
    GPIO.output(12, True) # b
    GPIO.output(13, True) # c
    GPIO.output(15, False) # d
    GPIO.output(16, False) # e
    GPIO.output(18, False) # f
    GPIO.output(22, False) # g

def two(): # Define function 'two' which makes GPIO a,b,d,e,g = True to display number '2'
    GPIO.output(11, True) # a
    GPIO.output(12, True) # b
    GPIO.output(13, False) # c
    GPIO.output(15, True) # d
    GPIO.output(16, True) # e
    GPIO.output(18, False) # f
    GPIO.output(22, True) # g

def three(): # Define function 'three' which makes GPIO a,b,c,d,g = True to display number '3'
    GPIO.output(11, True) # a
    GPIO.output(12, True) # b
    GPIO.output(13, True) # c
    GPIO.output(15, True) # d
    GPIO.output(16, False) # e
    GPIO.output(18, False) # f
    GPIO.output(22, True) # g
    
def four(): # Define function 'three' which makes GPIO b,c,f,g = True to display number '4'
    GPIO.output(11, False) # a
    GPIO.output(12, True) # b
    GPIO.output(13, True) # c
    GPIO.output(15, False) # d
    GPIO.output(16, False) # e
    GPIO.output(18, True) # f
    GPIO.output(22, True) # g

def five(): # Define function 'three' which makes GPIO a,c,d,f,g = True to display number '5'
    GPIO.output(11, True) # a
    GPIO.output(12, False) # b
    GPIO.output(13, True) # c
    GPIO.output(15, True) # d
    GPIO.output(16, False) # e
    GPIO.output(18, True) # f
    GPIO.output(22, True) # g

def six(): # Define function 'three' which makes GPIO a,c,d,e,f,g = True to display number '6'
    GPIO.output(11, True) # a
    GPIO.output(12, False) # b
    GPIO.output(13, True) # c
    GPIO.output(15, True) # d
    GPIO.output(16, True) # e
    GPIO.output(18, True) # f
    GPIO.output(22, True) # g
    
def SevenSeg(x): # Define function 'SevenSeg' which calls function 'one' 'two' or 'three' depending on 'x'
    
    if x == 0:
        blank()
    elif x == 1:
        one()
    elif x == 2:
        two()
    elif x == 3:
        three()
    elif x == 4:
        four()
    elif x == 5:
        five()
    elif x == 6:
        six()

def playSound(): #Plays a sound announcing the number         
        randomNumber = str(random.randint(1,6)) # Creates a random number and turns it into a string
        dice=int(randomNumber) # Turns string back in to number for use on display
        SevenSeg(dice) # Calls function to display rolled number 
        sound=("Number"+randomNumber+".ogg") # Assigns the correct audio file to variable sound after concatenating filename and number
        pygame.mixer.music.load(sound) # Loads the correct sound file
        pygame.mixer.music.play() # Plays the sound file
        print("Dice rolled a "+randomNumber) # Prints message on *Python Shell* Window
        
poll = .1 # Define Constant for PushButton 'poll' delay

delay = 0.2 # Define Constant for Counter delay

SevenSeg(0)
# Start of Counter 1, 2, 3 Program Execution
print "Press PushButton to Start" # Printed on Raspberry Pi *Python Shell* Window

while True: # while True: means run this loop forever
    PushButton = GPIO.input(7) # Check PushButton input
    if PushButton == False: # if PushButton has not been pressed
        time.sleep(poll) # wait 0.1 of a second before checking (polling) again
    else: # else PushButton has been pressed, so
        SevenSeg(0)
        time.sleep(0.5)
        print "Rolling the dice" # Print "Rolling the dice" on Raspberry Pi *Python Shell* Window
        sound=("Roll.ogg")
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()
        count=0
        while count !=10:
            rollNumber=random.randint(1,6)
            SevenSeg(rollNumber) # Call function 'SevenSeg' with randomly generated number
            time.sleep(delay) # Delay in between displaying numbers
            count=count+1 # Increment counter
        
        playSound() #Call function 'playSound' to announce number
        


