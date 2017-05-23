# -*- coding: utf-8 -*-
"""
Created on Fri May 19 12:57:40 2017

@author: caetano
"""
import socket

SERVER_IP = "192.168.1.101"
SERVER_PORT = 9999

class RobotClient:
    def __init__(self, serverIp, serverPort):
        self.robotSocket = None
        self.setIp(serverIp, serverPort)
        
    def setIp(self, serverIp, serverPort):
        self.serverIp = serverIp
        self.serverPort = serverPort
    
    def connect(self):
        print('Creating ServerSocket...')
        self.robotSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Attempting to connect at ' + self.serverIp + '...')
        self.robotSocket.connect((self.serverIp, self.serverPort))
        print('Connected!')

    def speakSentence(self, sentence, language):
        self.connect()
        print('Sending language...')
        self.robotSocket.send((language+'\n').encode('utf-8'))
        print('Sending sentence...')
        self.robotSocket.send((sentence+'\n').encode('utf-8'))
        print('Done!')
    
    def speakText(self, text, language):
        sentencesList = text.split('.')
        for sentence in sentencesList:
            if sentence != '':
                self.speakSentence(sentence + '.', language);
    
    def playSound(self, sound):
        self.connect()
        print('Sending sound command...')
        self.robotSocket.send(u'sound\n'.encode('utf-8'))
        print('Sending name of the animal...')
        self.robotSocket.send((sound+'\n').encode('utf-8'))
        print('Done!')




# SAMPLE CODE
if __name__ == '__main__':
    robotClient = RobotClient(serverIp=SERVER_IP, serverPort=SERVER_PORT)
    robotClient.speakText('Este é um texto com várias frases.'+
                           'É interessante fazer essa experiência, para verificar que ele separa corretamente.'+
                           'Só evite ? e !. Sim. Esses símbolos de pontuação não estão definidos.', 'ptbr')
    robotClient.playSound('duck')
    robotClient.speakText('See, this is how a duck sounds.','enus')