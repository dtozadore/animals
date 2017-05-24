# -*- coding: utf-8 -*-
"""
Created on Thu May  4 16:06:04 2017

@author: dtozadore
"""

#robotIp="169.254.206.242"
robotIp="169.254.148.90"

from naoqi import ALProxy
import RobotClient as rc

#variable to check if the robot is conected
naoConeted= False
tabletConected = True



"""
tts = ALProxy("ALTextToSpeech", robotIp, 9559)
behavior = ALProxy("ALBehaviorManager", robotIp, 9559)
motors =  ALProxy("ALMotion", robotIp, 9559)
posture = ALProxy("ALRobotPosture", robotIp, 9559)
aup = ALProxy("ALAudioPlayer",  robotIp, 9559)
"""

tablet = rc.RobotClient()


userName = "teste"
totalTime = 0

debug = True

Ykey = 'y'


# Default Language
defaultLanguage = 'Brazilian'

path = "./animals/"
    
    
#animals=['fish', 'cat', 'dog', 'bear', 'wolf','whale', 'fox', 'chicken', 'cow', 'duck']

animals=['cow', 'chicken', 'pig', 'birds', 'fish', 'duck', 
         'horse', 'sheep', 'frog', 'bear', 'wolf', 'seal']

animals_pt=['vaca', 'frango', 'porco', 'pássaro', 'peixe', 'pato', 
         'cavalo', 'ovelha', 'sapo', 'urso', 'lobo', 'foca']


hit = [True] * len(animals)


def initializer():
    
    #print ("INIT")
    
    #info("HEYYYY")
    
    if(naoConeted):
        #tts = ALProxy("ALTextToSpeech", robotIp, 9559)
#        tts = ALProxy("ALTextToSpeech", robotIp, 9559)
#        behavior = ALProxy("ALBehaviorManager", robotIp, 9559)
#        motors =  ALProxy("ALMotion", robotIp, 9559)
#        posture = ALProxy("ALRobotPosture", robotIp, 9559)
        
        tts.setLanguage(defaultLanguage)
        motors.wakeUp()




def finisher():
    
    
    if(naoConeted):
        
        motors.rest()



def info(stringToPrint):   
    
    
    if debug:
            print("[INFO ]: "+ stringToPrint)            
