# -*- coding: utf-8 -*-
"""
Created on Fri May 12 16:23:58 2017

@author: dtozadore
"""


import vars



def run(behaviorName):
    
    vars.posture.goToPosture("Crouch", 1.0)
    taskId = vars.behavior.post.runBehavior(behaviorName)
    vars.posture.goToPosture("Crouch", 1.0)
    
    return taskId 
    


def setMotor(state):
    #""" Set motor ON if state is True or motto off if state is False """"
    
    if(state):
        vars.motors.wakeUp()
    else:
        vars.motors.rest()
        
            