# coding=UTF-8


import vars 
import random
import RobotClient as rc

#funtion say
def say(str2say, lang='ptbr'):
    """ Function to make the robot say (if connected) """
    
    print("[NAO SAYING]: " + str2say)
    print("")
    
    if(vars.naoConeted):
        vars.tts.say(str2say)
    
    elif(vars.tabletConected):
        vars.tablet.speakText(str2say,lang)
        
        
        
        
    
def setLang(lang):
        if(vars.naoConeted):
            vars.tts.setLanguage(lang)
    
    
    
def load_from_file(filename):
    """ Fucntion to load a serie of dialog form file name """
    
    reader = open(filename,"r")
    ret = reader.read()
    reader.close()
    return ret
    
    
    
def repeat():
    rd=random.randint(0,2)
    
    if(rd==0):
        return "Você gostaria que eu repetisse?"
        
    elif(rd==1):
        return "Se ficou confuso eu posso repetir pra você. Quer que eu repita?"
        
    else:
        return "Essa foi fácil. Mas posso repetir pra você. Voce quer?"
   

   
def sound():
    rd=random.randint(0,2)
    
    if(rd==0):
        return "Escute o som que emite esse animal"
        
    elif(rd==1):
        return "Esse animal faz assim"
        
    else:
        return "O som dele é mais ou menos isso"
             