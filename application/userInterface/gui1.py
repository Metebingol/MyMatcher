from database.database import database
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import ttk
from tkinter import StringVar
from communcation.Networking import server
from tkinter import Text

class guiConnector():
    def __init__(self,root:Tk,data:database) -> None:
        self.root = root
        self.data = data
        self.server = server()
    def build(self):
        for feature in self.data.filerFeature:
            feature.destroy()
        self.root.update()
        # ---
        # Server feature
        self.label_A1 = Label(self.root,text="Device Information:")
        self.data.connectorFeature.append(self.label_A1)
        self.label_A2 = Label(self.root,text=f"  Hostname: {self.data.hostname}")
        self.data.connectorFeature.append(self.label_A2)
        self.label_A3 = Label(self.root,text=f"  IP: {self.data.IP}")
        self.data.connectorFeature.append(self.label_A3)
        self.label_A4 = Label(self.root,text="Server:")
        self.data.connectorFeature.append(self.label_A4)
        self.label_A5 = Label(self.root,text="  Port:")
        self.data.connectorFeature.append(self.label_A5)
        string = StringVar()
        self.entry_A1 = Entry(self.root,textvariable=string,borderwidth=0,border=0)
        self.entry_A1.insert("0",self.data.port)
        self.data.connectorFeature.append(self.entry_A1)
        self.button_A1 = Button(self.root,text="Make Server",width=10,bg="white",command=lambda:self.server.makeServer(self.text))
        self.data.connectorFeature.append(self.button_A1)
        self.button_A2 = Button(self.root,text="Accept",width=10,bg="white",command=lambda:self.server.acceptThread(self.entry_A1,self.data,self.text))
        self.data.connectorFeature.append(self.button_A2)
        self.text = Text(self.root,width=25,height=15)
        self.data.connectorFeature.append(self.text)
        # ---

        # ---
        # client feature
        self.label_A6 = Label(self.root,text="  Hostname:")
        self.data.connectorFeature.append(self.label_A6)
        self.label_A7 = Label(self.root,text="  IP:")
        self.data.connectorFeature.append(self.label_A7)
        self.label_A8 = Label(self.root,text="  Port:")
        self.data.connectorFeature.append(self.label_A8)
        self.label_A9 = Label(self.root,text="Client:")
        self.data.connectorFeature.append(self.label_A9)
        self.button_A3 = Button(self.root,text="Make Client",width=10,bg="white")
        self.data.connectorFeature.append(self.button_A3)
        self.button_A4 = Button(self.root,text="Connect",width=10,bg="white")
        self.data.connectorFeature.append(self.button_A4)
        # ---
        self.place()
    def place(self):
        self.label_A1.place(x=5,y=30)
        self.label_A2.place(x=5,y=55)
        self.label_A3.place(x=5,y=80)
        self.label_A4.place(x=5,y=120)
        self.label_A5.place(x=5,y=145)
        self.entry_A1.place(x=60,y=150)
        self.button_A1.place(x=10,y=170)
        self.button_A2.place(x=100,y=170)
        self.label_A9.place(x=5,y=220)
        self.label_A8.place(x=5,y=245)
        self.label_A7.place(x=5,y=270)
        self.label_A6.place(x=5,y=295)
        self.button_A4.place(x=10,y=320)
        self.button_A3.place(x=100,y=320)
        self.text.place(x=5,y=350)