from tkinter import IntVar
from database.database import database
from tkinter import Checkbutton, Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import ttk
from tkinter import StringVar
from communcation.Networking import server,client
from tkinter import Text
from tkinter import NO
class guiConnector():
    def __init__(self,root:Tk,data:database) -> None:
        self.root = root
        self.data = data
        self.server = server()
        self.client = client()
    def build(self):
        for feature in self.data.filerFeature:
            feature.destroy()
        self.root.update()
        # ---

        # ---
        self.table1 = ttk.Treeview(self.root,columns=("1","2","3"))
        self.table1.column("#0",width=0,stretch=NO)
        self.table1.column("1",width=180)
        self.table1.column("2",width=180)
        self.table1.column("3",width=180)
        self.table1.heading("1",text="Hostname")
        self.table1.heading("2",text="IP")
        self.table1.heading("3",text="Port")

        self.table2 = ttk.Treeview(self.root,columns=("1","2","3"))
        self.table2.column("#0",width=0,stretch=NO)
        self.table2.column("1",width=180)
        self.table2.column("2",width=180)
        self.table2.column("3",width=180)
        self.table2.heading("1",text="Hostname")
        self.table2.heading("2",text="IP")
        self.table2.heading("3",text="Port")
        self.button_A6 = Button(self.root,text="Trust ")
        self.data.connectorFeature.append(self.button_A6)
        self.button_A7 = Button(self.root,text="UnTrust")
        self.data.connectorFeature.append(self.button_A7)
        self.button_A8 = Button(self.root,text="Save")
        self.data.connectorFeature.append(self.button_A8)
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
        self.button_A2 = Button(self.root,text="Accept",width=10,bg="white",command=lambda:self.server.acceptThread(self.entry_A1,self.data,self.text,self.table1))
        self.data.connectorFeature.append(self.button_A2)
        self.text = Text(self.root,width=21,height=15)
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
        self.integer = IntVar()
        self.button_A5 = Checkbutton(self.root,text="IP",variable=self.integer)
        self.data.connectorFeature.append(self.button_A5)
        string2 = StringVar()
        self.entry_A2 = Entry(self.root,textvariable=string2,borderwidth=0,border=0,width=16)
        self.entry_A2.insert("0","IP")
        self.data.connectorFeature.append(self.entry_A2)
        string3 = StringVar()
        self.entry_A3 = Entry(self.root,textvariable=string3,borderwidth=0,border=0,width=16)
        self.entry_A3.insert("0","Hostname")
        self.data.connectorFeature.append(self.entry_A3)
        string4 = StringVar()
        self.entry_A4 = Entry(self.root,textvariable=string4,borderwidth=0,border=0,width=16)
        self.entry_A4.insert("0","Port")
        self.data.connectorFeature.append(self.entry_A4)
        self.button_A3 = Button(self.root,text="Make Client",width=10,bg="white",command=lambda:self.client.makeClient(self.text))
        self.data.connectorFeature.append(self.button_A3)
        self.button_A4 = Button(self.root,text="Connect",width=10,bg="white",command=lambda:self.client.connect(self.entry_A3,self.entry_A2,self.entry_A4,self.integer,self.table1,self.data,self.text))
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
        self.entry_A2.place(x=80,y=275)
        self.entry_A3.place(x=80,y=300)
        self.entry_A4.place(x=80,y=250)
        self.button_A4.place(x=10,y=320)
        self.button_A3.place(x=100,y=320)
        self.button_A5.place(x=75,y=220)
        self.text.place(x=5,y=350)
        self.table1.place(x=220,y=40)
        self.table2.place(x=220,y=320)
        self.button_A6.place(x=720,y=270)
        self.button_A7.place(x=710,y=550)
        self.button_A8.place(x=670,y=550)