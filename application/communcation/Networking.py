from socket import socket as soc
from socket import AF_INET
from socket import SOCK_STREAM
from telnetlib import IP
from tkinter import Entry, IntVar, ttk
from database.database import database
from threading import Thread as thr
from tkinter import Text
from tkinter import END
from socket import gethostbyaddr
from socket import gethostbyname
class server():
    def __init__(self) -> None:
        self.addressFamily = AF_INET 
        self.protocol = SOCK_STREAM
    def makeServer(self,text:Text):
        self.serverObject = soc(self.addressFamily,self.protocol)
        text.insert(END,"=>Server is created succesfully\n")
    def accept(self,entry:Entry,data:database,text:Text,table:ttk.Treeview):
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
        table.insert("",END,values=(gethostbyaddr(ipClient)[0],ipClient,portClient))
        data.clientConnected.append([object,gethostbyaddr(ipClient),ipClient,portClient])
        text.insert(END,"=>Server accept the client succcesfully\n")
    def acceptThread(self,entry:Entry,data:database,text,table:ttk.Treeview):
        function = thr(target=self.accept,args=(entry,data,text,table,))
        function.start()


class client():
    def __init__(self) -> None:
        self.addressFamily = AF_INET 
        self.protocol = SOCK_STREAM
    def makeClient(self,text:Text):
        self.clinetSocket = soc(self.addressFamily,self.protocol)
        text.insert(END,"=>Client is created succesfully\n")
    def connect(self,entry1:Entry,entry2:Entry,entry3:Entry,integer:IntVar,table:ttk.Treeview,data:database,text:Text):
        if int(integer.get()) == 1:
            try:
                ip = str(entry2.get())
                port = int(entry3.get())
                self.clinetSocket.connect((ip,port))
                table.insert("",END,values=(gethostbyaddr(ip)[0],entry2.get(),entry3.get()))
                text.insert(END,"=>Connected to server\n")
                data.serverConnected.append([self.clinetSocket,gethostbyaddr(ip)[0],entry2.get(),entry3.get()])
            except:
                text.insert(END,"=>Server you try to connect is not answering\n")
        else:
            try:
                ip = gethostbyname(str(entry1.get()))
                port = int(entry3.get())
                self.clinetSocket.connect((ip,port))
                table.insert("",END,values=(entry1.get(),entry2.get(),entry3.get()))
                text.insert(END,"=>Connected to server\n")
                data.serverConnected.append([self.clinetSocket,entry1.get(),ip,entry3.get()])
            except:
                text.insert(END,"=>Server you try to connect is not answering\n")