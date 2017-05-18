# -*- coding: utf-8 -*-
"""
Created on Thu May  4 16:14:07 2017

@author: dtozadore
"""

from modules import vars
from modules import dialog as diag
from modules import motion as mt
#from modules import vision as vs
#import time


def main():
    
    if vars.debug:
            print("[INFO] Starting program ")            
            
    
    vars.initializer();
    
    if vars.debug:
            print("[INFO] Starting Stories ")            
      
    maxStory=stories(7,11)


    if vars.debug:
            print("[INFO] Stories Finished Successfully")            
      
    
    
    print("Reach %d stories!" % (maxStory+1))    
    
    
    
    
    
    """    
    
    Timeline:
        -Introducao
        -historias
            narrativa
            sabe nome?
                sim: me 
      
    toSay = "Hello, my name is goku!"
    path = "/home/dtozadore/Projects/NaoPyTest/foo/animals/"
    
    #diag.say(vars.teste)
    
        
    #animals=['fish', 'cat', 'dog', 'bear', 'wolf','whale', 'fox', 'chicken', 'cow', 'duck']
    
    animals=['cow', 'chicken', 'pig', 'birds', 'fish', 'duck', 
             'horse', 'sheep', 'frog', 'bear', 'wolf', 'seal']

   
    vars.tts.setLanguage('Brazilian')
    diag.say("Vamos dizer comigo o nome dos animais em ingles?")    

    vars.tts.setLanguage('English')    
    for ani in animals:    
        diag.say(ani)    
""
    for ani in animals:    
        vars.tts.setLanguage('Brazilian')
        diag.say(diag.load_from_file(path+ani))    
        
        vars.tts.setLanguage('English')
        diag.say("This was the story of animal:")
        time.sleep(0.5) 
        diag.say(ani)
"""



def stories(start, end):
    
    for i in range(start,end):
        
        if vars.debug:
            print("\n----------------------------------------")            
            print("------ [INFO] Story number: %d ----------" % i)            
            print("----------------------------------------\n")            
            
        narratives(i)
        
        #question(i)
        
        # Dont ask last time        
        if(i<end-1):
            diag.say("Fim dessa estória! Você gostaria que eu contasse mais uma estória de um animal diferente?")
            if( (raw_input("Another story?:"))!=vars.Ykey):
                break
        
    return i

 
    
    

def narratives(i):
    
    repeat = vars.Ykey
    while (repeat==vars.Ykey):
        
        #diag.setLang('Brazilian')
        mt.run(vars.animals[i])
        diag.say(diag.load_from_file(vars.path+vars.animals[i]))
        
        
        """
        diag.setLang('English')
        diag.say("This was the story of animal:")
        time.sleep(0.5) 
        diag.say(vars.animals[i])
        """
        
        #diag.setLang('Brazilian')
        diag.say(diag.sound())
        #--PLAY SOUND
        diag.say(diag.repeat())
        repeat=raw_input("repeat?(SPACE for Y. Anything else for N):")
    
    
    
def question(i):
    """ Function to make loop in question if got wrong  answer  """

    aux = True
    while(aux):
        diag.say("Você sabe como se pronuncia o nome desse animal em inglês?")
        ans=raw_input("Know the name?(SPACE for Y. Anything else for N)")
        
        if(ans!=vars.Ykey):
            diag.say("Sem Problemas. Eu sei e te conto")
            explain(i)
            
        diag.say("Ok. Entao me diga:")
        ans=raw_input("Is the name right?(SPACE for Y. Anything else for N):")
        if(ans==vars.Ykey):
            diag.say("É Isso mesmo. Parabéns.")
            aux = False
        else:
            diag.say("Nao é bem isso. Veja como é.")
            explain(i)
            diag.say("E agora?")
            aux = True
        
       
   
def explain(i):
    
    ans2=vars.Ykey
    while(ans2==vars.Ykey):
        
        diag.say("O nome desse animal em inglês é:")
        diag.setLang('English')
        diag.say(vars.animals[i])
        diag.setLang('Brazilian')
        
        diag.say("Quer que eu repita?")
        ans2=raw_input("Repeat?(SPACE for Y. Anything else for N):")
                
        
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()  