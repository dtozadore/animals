# -*- coding: utf-8 -*-
"""
Created on Thu May  4 16:06:04 2017

@author: dtozadore
"""

robotIp="169.254.206.242"
#robotIp="192.168.1.118"

from naoqi import ALProxy


#variable to check if the robot is conected
naoConeted= True

tts = ALProxy("ALTextToSpeech", robotIp, 9559)
behavior = ALProxy("ALBehaviorManager", robotIp, 9559)
motors =  ALProxy("ALMotion", robotIp, 9559)
posture = ALProxy("ALRobotPosture", robotIp, 9559)

debug = True

Ykey = 'y'


# Default Language
defaultLanguage = 'Brazilian'

path = "/home/dtozadore/Projects/NaoPyTest/foo/animals/"
    
    
#animals=['fish', 'cat', 'dog', 'bear', 'wolf','whale', 'fox', 'chicken', 'cow', 'duck']

animals=['cow', 'chicken', 'pig', 'birds', 'fish', 'duck', 
         'horse', 'sheep', 'frog', 'bear', 'wolf', 'seal']


def initializer():
    
    print ("INIT")
    
    info("HEYYYY")
    
    if(naoConeted):
        #tts = ALProxy("ALTextToSpeech", robotIp, 9559)
#        tts = ALProxy("ALTextToSpeech", robotIp, 9559)
#        behavior = ALProxy("ALBehaviorManager", robotIp, 9559)
#        motors =  ALProxy("ALMotion", robotIp, 9559)
#        posture = ALProxy("ALRobotPosture", robotIp, 9559)
        
        tts.setLanguage(defaultLanguage)
        motors.wakeUp()




def finisher():
    
    print "FORA"
    if(naoConeted):
        print "HELLOOOO"
        motors.rest()



def info(stringToPrint):   
    
    
    if debug:
            print("[INFO ]: "+ stringToPrint)            
