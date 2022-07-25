import socket as sc
import tkinter as tk
import threading as tr
import sys
from tkinter import ttk


class connector():
    def __init__(self) -> None:
        self.hostName = sc.gethostname()
        self.IP = sc.gethostbyname(self.hostName)
        self.port = 80
        self.condition = "Stable"
    def makeServer(self,feature:tk.Label):
        self.addressFamily = sc.AF_INET 
        self.protocol = sc.SOCK_STREAM
        self.socketObejct = sc.socket(self.addressFamily,self.protocol)
        feature.configure(text="Server")
        feature.update()
    def acceptThreading(self,feature:tk.Label,feature2:ttk.Treeview,listAccepted:list,port):
        feature.configure(text="Accept")
        feature.update()
        self.a = tr.Thread(target=self.accept,args=(listAccepted,port,feature2,))
        self.a.start()
    def accept(self,listAccepted:list,port,feature2:ttk.Treeview):
        try:
            if port == self.port:
                pass
            else: self.port = port
            address = (self.IP,self.port)
            self.socketObejct.bind(address)
            self.socketObejct.listen(10)
            Info:tuple
            object ,Info=self.socketObejct.accept()
            HostName = sc.gethostbyaddr(Info[0])
            listInfo=list(Info)
            listInfo.append(HostName[0])
            listAccepted.append([object,listInfo])
            feature2.insert("",tk.END,tk.END,values=(object,Info[1],Info[0],HostName[0]))
            feature2.update()
        except:
            sys.exit()
    def close(self):
        if self.a.is_alive():
            self.a.join()
    def makeClient(self):
        self.ip_v4 = sc.AF_INET
        self.tcp = sc.SOCK_STREAM
        self.clinetSocket = sc.socket(self.ip_v4,self.tcp)
    def connect(self,HostName,IP,port,object:sc.socket):
        ipCheck = sc.gethostbyname(HostName)
        print(ipCheck)
        if ipCheck == IP:
            self.clinetSocket.connect((IP,port))
            object = self.clinetSocket