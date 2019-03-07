# -*- coding: utf-8 -*- 

import telepot
from telepot.loop import MessageLoop
import time

 
def handle(msg):
     content_type, chat_type, chat_id = telepot.glance(msg)
        
     if content_type == 'text':
         command = msg['text']
	 print ('Nova mensagem: %s' % command)

     if  'Oi' in command:
         text = 'Ola, como voce esta?'
    	 bot.sendMessage(chat_id, text)
	 print ('Resposta: %s' %text)
         print ('Esperando novas mensagens . . .')          

     if 'Boa noite' in command:
    	 bot.sendMessage(chat_id, "Boa noite, como voce esta?")	
        
# Cria um bot com a API key disponibilizada pelo BotFather
TOKEN = '413319684:AAHCyBCCoQeqS_aS4QJFgziOCTKLyCWek-M'
bot = telepot.Bot(TOKEN)

#Adiciona a função handle para ser chamada sempre que uma nova mensagem for recebida
MessageLoop(bot, handle).run_as_thread()
print('Esperando novas mensagens ...')

#Mantém o programa rodando
while 1:
    time.sleep(10)
