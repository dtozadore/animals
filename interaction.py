# -*- coding: utf-8 -*-
"""
Created on Thu May  4 16:14:07 2017

@author: dtozadore
"""

import sys
import datetime
import time
import cv2


from modules import vars
from modules import dialog as diag
from modules import motion as mt

#from modules import vision as vs


img=cv2.imread("yes-no.jpeg")
img= cv2.resize(img, (400, 200)) 





def main():
    
    
    
    start_time = datetime.datetime.now().replace(microsecond=0)
    
    vars.info("Starting program ")            
    vars.initializer();
   
    #vars.userName = raw_input("User Name: ")
    
    vars.info("Welcome dialog")
    introduction()  
    """"""
    vars.info("Starting Stories ")            
    maxStory=stories(0,12)
    #maxStory=3

    vars.info("Stories Finished Successfully")            
    print("Reach %d stories!" % (maxStory+1))    
    
    vars.info("Starting Evaluation")
    evaluation(maxStory)

    vars.info("Good Bye")    
    bye()

    end_time = datetime.datetime.now().replace(microsecond=0)
    
    vars.totalTime = end_time - start_time
    
    #print vars.hit
    fname = writeResults(maxStory)
    vars.info("Evaluation write in file " + fname )
    
    vars.info("Program Finished Successfully!")
    cv2.destroyAllWindows()
    
    
#------------------------ START FUNCTIONS -------------------------------------    
    

def introduction():
    
    diag.say("Olá, " + vars.userName)
    diag.say(diag.load_from_file("./txts/intro.txt"))
    

def bye():
    
    diag.say("Bom, então é isso, " + vars.userName)
    diag.say(diag.load_from_file("./txts/bye.txt"))    

def stories(start, end):
    
    for i in range(start,end):
        
        if vars.debug:
            print("\n----------------------------------------")            
            print("------ [INFO] Story number: %d ----------" % i)            
            print("----------------------------------------\n")            
            
        narratives(i)
        
        question(i)
        
        # Dont ask last time        
        if(i<end-1):
            diag.say("Fim dessa estória! Você gostaria que eu contasse mais uma estória de um animal diferente?")
            if( (myInput("Another story?:"))!=vars.Ykey):
                break
        
    return i

 
    
    

def narratives(i):
    
    #TROCAR PARA  ficar repetindo dps 
    repeat = vars.Ykey
    
    while (repeat==vars.Ykey):
        
        mt.run(vars.animals[i])
        diag.say(diag.load_from_file(vars.path+vars.animals[i]))
        
        
        """
        diag.setLang('English')
        diag.say("This was the story of animal:")
        time.sleep(0.5) 
        diag.say(vars.animals[i])
        """
        
        if(vars.animals[i]=='fish'):
            diag.say("Não é possível escutar o som desse animal pois ele vive embaixo dágua" )
        else:    
            diag.say(diag.sound())
            x = 1        
            #--PLAY SOUND
            time.sleep(x)
            diag.playSound(vars.animals[i])        
            time.sleep(x)
                    
        
        diag.say(diag.repeat())
        
        repeat=myInput("repeat?(SPACE for Y. Anything else for N):")
    
    
    
def question(i):
    """ Function to make loop in question if got wrong  answer  """

    aux = True
    while(aux):
        diag.say("Você sabe como se pronuncia o nome desse animal em inglês?")
        ans=myInput("Know the name?(SPACE for Y. Anything else for N)")
        
        if(ans!=vars.Ykey):
            diag.say("Sem Problemas. Eu sei e te conto")
            explain(i)
            
        diag.say("Ok. Entao me diga:")
        ans=myInput("Is the name right?(SPACE for Y. Anything else for N):")
        if(ans==vars.Ykey):
            diag.say("É Isso mesmo. Parabéns.")
            aux = False
        else:
            diag.say("Não é bem isso. Veja como é.")
            explain(i)
            diag.say("E agora?")
            aux = True
        
       
   
def explain(i):
    
    ans2=vars.Ykey
    while(ans2==vars.Ykey):
        
        diag.say("O nome desse animal em inglês é:")
        diag.setLang('English')
        diag.say(vars.animals[i], 'enus')
        diag.setLang('Brazilian')
        
        diag.say("Quer que eu repita?")
        ans2=myInput("Repeat?(SPACE for Y. Anything else for N):")
                
        
    
    
def myInput(str2say):
    
#==============================================================================
#     char = ''
#     while not char in ['y', 'n']:
#         char = raw_input(str2say)
#         if char == "q":
#             sys.exit(1)
#     return char
#     
#==============================================================================
    char = ''
    while not char in ['y', 'n', 'q']:
         
        cv2.imshow('image',img)
        char = cv2.waitKey(0)

        #print char
        
        if char == 1048697:
            return 'y'
        elif char == 1048686:    
            return 'n'
        elif char == 1048689:
            cv2.destroyAllWindows()
    
            sys.exit(1)

    
def evaluation(x):

    diag.say("Certo! Chega de estórias. Vamos ver o que você consegue se lembrar do que conversamos hoje.")

    for i in range(x+1):
      while True:
            diag.say("Me diga como se fala em ingles.")
            diag.say(vars.animals_pt[i])
            #diag.say("")
            ans=myInput("Repeat?(SPACE for Y. Anything else for N):")
            if(ans=="y"):
                diag.say("Muito bom! Acertou.")
                if i!=x:
                    diag.say( "Vamos pro próximo" )
                break
            else:
                diag.say("Poxa! Não é bem assim. O certo é:")
                diag.setLang('English')
                diag.say(vars.animals[i], 'enus')
                diag.setLang('Brazilian')
                diag.say("Agora que já sabe")
                vars.hit[i]=False






def writeResults(maxStory):
    
    if(vars.naoConeted):
        fname = "robot_results.txt"
    elif(vars.tablet):
        fname = "tablet_results.txt"
        
    f = open(fname,"a")

    #f.write( '{0:20} | '.format(vars.userName) + " | " +  str(sum(vars.hit[0:maxStory])) + "/" + str(maxStory) + " | " + str(vars.hit[0:maxStory]) + "\n" )
    #f.write( '{0:20} | {1:2} | {} \n'.format(vars.userName, str(vars.hit[0:maxStory]), str(maxStory), str(vars.hit[0:maxStory]) ) )
    f.write( '{0:15} | {1:2d}/{2:2d} | {3} | {4}\n'.format(vars.userName, sum(vars.hit[0:maxStory+1]),  maxStory+1, vars.totalTime, vars.hit[0:maxStory+1]) )

    f.close()

    return fname

    
if __name__ == "__main__":
    main()  