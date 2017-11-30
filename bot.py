from irc import *
import os
from random import *
import time

channel = "#channel_name"
server = "chat.freenode.net"
nickname = "the_bot"
 
irc = IRC()
irc.connect(server, channel, nickname)
 
while 1:
    text = irc.get_text()
    print text
    first=randint(1,254)
    second=randint(1,254)
    third=randint(1,254)
    fourth=randint(1,254)
    myarrayint=randint(0,2)
    #sleeparray=randint(10,20)
    rando=randint(1,50)
    myarray=['wait','download evil.exe','scan for other hosts']

    if 20 <= rando <=30:
    	irc.send(channel,"Message received from {0}.{1}.{2}.{3} - instructions: {4}".format(first,second,third,fourth,myarray[myarrayint]))
    if "JOIN" in text and "self" not in text:
		  excl=text.index("!")
		  handle=text[1:excl]
		irc.send(channel,"Welcome to the show {0}, awaiting input...".format(handle)) 
		#if "PRIVMSG" in text and channel in text and "hello" in text:
    if "hello" in text:
    	irc.send(channel, "hello to you!")
    if "help" in text:
	    irc.send(channel, "Sorry! No HELP options here")
