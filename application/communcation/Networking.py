from socket import socket as soc
from socket import AF_INET
from socket import SOCK_STREAM
from telnetlib import IP
from tkinter import Entry
from database.database import database
from threading import Thread as thr
from tkinter import Text
from tkinter import END

class server():
    def __init__(self) -> None:
        self.addressFamily = AF_INET 
        self.protocol = SOCK_STREAM
    def makeServer(self,text:Text):
        self.serverObject = soc(self.addressFamily,self.protocol)
        text.insert(END,"=>Server is created succesfully\n")
    def accept(self,entry:Entry,data:database,text:Text):
        try:
            port = int(entry.get())
            IP = data.IP
        except:
            text.insert(END,"=>Port number or IP address is not valid\n")
        try:
            self.serverObject.bind((IP,port))
            self.serverObject.listen(10)
        except:
            text.insert(END,"=>Server cannot dive into network\n")
        try:
            object, [ipClient,portClient]= self.serverObject.accept()
        except:
            text.insert(END,"=>Server cannnot accept any client\n")
        data.clientConnected.append([object,ipClient,portClient])
        text.insert(END,"=>Server accept the client succcesfully")
    def acceptThread(self,entry:Entry,data:database,text):
        function = thr(target=self.accept,args=(entry,data,text,))
        function.start()




