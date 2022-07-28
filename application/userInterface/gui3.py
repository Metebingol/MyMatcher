from tkinter import Tk 
from tkinter import Button
from database.database import database
from userInterface.gui1 import guiConnector
from userInterface.gui2 import guiFiler
class mainRoot():
    def __init__(self,name,data:database) -> None:
        self.name = name
        self.database = data
    def mainRootConfig(self,root:Tk):
        self.root = root
        self.connector = guiConnector(self.root,self.database)
        self.filer = guiFiler(self.root,self.database)
        self.root.geometry("800x600")
        self.root.resizable(False,False)
        self.root.iconbitmap("C:/Studies/projeler/MyMatcher/MyMatcher/application/codest.ico")
        self.root.title(self.name)
        self.build()
    def build(self):
        self.button_A1 = Button(self.root,text="MyConnect",width=11,borderwidth=0,border=0,bg="light gray",command=self.connector.build)
        self.button_A2 = Button(self.root,text="MyShare",width=11,borderwidth=0,border=0,bg="light gray",command=self.filer.build)
        self.place()
    def place(self):
        self.button_A1.place(x=0,y=0)
        self.button_A2.place(x=80,y=0)





