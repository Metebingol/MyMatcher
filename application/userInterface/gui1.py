from database.database import database
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import ttk
from tkinter import StringVar


class guiConnector():
    def __init__(self,root:Tk,data:database) -> None:
        self.root = root
        self.data = data
    def build(self):
        for feature in self.data.filerFeature:
            feature.destroy()
        self.root.update()
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
        self.data.connectorFeature.append(self.entry_A1)
        self.button_A1 = Button(self.root,text="Make Server",width=10,bg="white")
        self.data.connectorFeature.append(self.button_A1)
        self.button_A2 = Button(self.root,text="Accept",width=10,bg="white")
        self.data.connectorFeature.append(self.button_A2)
        self.place()
    def place(self):
        self.label_A1.place(x=5,y=25)
        self.label_A2.place(x=5,y=55)
        self.label_A3.place(x=5,y=85)
        self.label_A4.place(x=5,y=120)
        self.label_A5.place(x=5,y=150)
        self.entry_A1.place(x=60,y=155)
        self.button_A1.place(x=10,y=180)
        self.button_A2.place(x=100,y=180)