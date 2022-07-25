import tkinter as tk
from tkinter import ttk

from requests import delete
from Libraries.connector import connector
import sys
"""
Features Information
Connector:
    label_A1=> Hostname 
    label_A2=> IP
    label_A3=> Port
    label_A4=> text
    entry_A1=> HostName
    entry_A2=> IP
    entry_A3=> Port

FileMatcher:



"""



class application():
    def __init__(self,objectConn:connector) -> None:
        self.conn = objectConn
        self.root = tk.Tk()
        self.root.title("MyMatcher")
        self.root.geometry("800x600")
        self.root.configure()
        self.root.resizable(False,False)
        self.trustedDevices = []
        self.connecteDevices =[]
        self.objectConnected = None
        self.allFeature = []
        self.connectorFeature = []
        self.fileFeature = []
    def buildMain(self):
        self.menuMatch = tk.Button(self.root,text="FileMathcer",command=self.buildFile)
        self.menuConn = tk.Button(self.root,text="Connector",command=self.buildConnector) 
        self.label_C1 = tk.Label(self.root,text="ZeroCondition")
    def placeMain(self):
        self.menuMatch.place(x=0,y=0)
        self.menuConn.place(x=75,y=0)
        self.label_C1.place(x=150,y=0)
    def buildConnector(self):
        self.cleaner(self.fileFeature)
        self.label_A1 = tk.Label(self.root,text="   HostName")
        self.label_A2 = tk.Label(self.root,text="   IP")
        self.label_A3 = tk.Label(self.root,text="   Port")
        self.label_A4 = tk.Label(self.root,text="MyDevices:")
        self.label_A5 = tk.Label(self.root,text="   HostName")
        self.label_A6 = tk.Label(self.root,text="   IP")
        self.label_A7 = tk.Label(self.root,text="   Port")
        self.label_A8 = tk.Label(self.root,text="OtherDevices:")
        self.connectorFeature.append(self.label_A1)
        self.connectorFeature.append(self.label_A2)
        self.connectorFeature.append(self.label_A3)
        self.connectorFeature.append(self.label_A4)
        self.connectorFeature.append(self.label_A5)
        self.connectorFeature.append(self.label_A6)
        self.connectorFeature.append(self.label_A7)
        self.connectorFeature.append(self.label_A8)
        #
        self.table = ttk.Treeview(self.root,selectmode="browse",columns=("1","2","3","4"))
        self.table2 = ttk.Treeview(self.root,selectmode="browse",columns=("1","2","3","4"))
        self.entry_A1 = tk.Entry(self.root)
        self.entry_A1.insert(0,str(self.conn.hostName))
        self.entry_A2 = tk.Entry(self.root)
        self.entry_A2.insert(0,str(self.conn.IP))
        self.data = tk.IntVar()
        self.entry_A3 = tk.Entry(self.root,textvariable=self.data)
        self.entry_A3.insert(0,str(self.conn.port))  
        self.connectorFeature.append(self.entry_A1)
        self.connectorFeature.append(self.entry_A2)
        self.connectorFeature.append(self.entry_A3)
        self.data4 = tk.StringVar()
        self.entry_A4 = tk.Entry(self.root,textvariable=self.data4)
        self.entry_A4.insert(0,"Hostname")
        self.data3 = tk.StringVar()
        self.entry_A5 = tk.Entry(self.root,textvariable=self.data3)
        self.entry_A5.insert(0,"IP")
        self.data2 = tk.IntVar()
        self.entry_A6 = tk.Entry(self.root,textvariable=self.data2)
        self.entry_A6.insert("0",80)
        self.connectorFeature.append(self.entry_A5)
        self.connectorFeature.append(self.entry_A6)
        self.connectorFeature.append(self.entry_A4)
        #
        self.button_A1 = tk.Button(self.root,text="Make Server",width=10,command=lambda:self.conn.makeServer(self.label_C1))
        self.button_A2 = tk.Button(self.root,text="Accept",width=6,command=lambda:self.conn.acceptThreading(self.label_C1,self.table,self.connecteDevices,int(self.entry_A3.get())))
        self.button_A3 = tk.Button(self.root,text="Close",width=6,command=self.conn.close)
        self.button_A4 = tk.Button(self.root,text="Make Client",command=self.conn.makeClient)
        self.button_A5 = tk.Button(self.root,text="Connect",command=lambda:self.conn.connect(self.entry_A4.get(),self.entry_A5.get(),int(self.entry_A6.get()),self.objectConnected))
        self.button_A6 = tk.Button(self.root,text="Trust",command=self.trust)
        self.button_A7 = tk.Button(self.root,text="Untrust",command=self.untrust)
        self.button_A8 = tk.Button(self.root,text="Add")
        self.connectorFeature.append(self.button_A1)
        self.connectorFeature.append(self.button_A2)
        self.connectorFeature.append(self.button_A3)
        self.connectorFeature.append(self.button_A4)
        self.connectorFeature.append(self.button_A5)
        self.connectorFeature.append(self.button_A6)
        self.connectorFeature.append(self.button_A7)
        self.connectorFeature.append(self.button_A8)
        #
        self.table.column('#0', width=0, stretch=tk.NO)
        self.table.column('1', width=80)
        self.table.column('2', width=80)
        self.table.column('3', width=200)
        self.table.column('4', width=200)
        self.table.heading("1",text="Object",anchor=tk.CENTER)
        self.table.heading("3",text="IP",anchor=tk.CENTER)
        self.table.heading("4",text="HostName",anchor=tk.CENTER)
        self.table.heading("2",text="Port",anchor=tk.CENTER)
        self.table2.column('#0', width=0, stretch=tk.NO)
        self.table2.column('1', width=80)
        self.table2.column('2', width=80)
        self.table2.column('3', width=200)
        self.table2.column('4', width=200)
        self.table2.heading("1",text="Object",anchor=tk.CENTER)
        self.table2.heading("3",text="IP",anchor=tk.CENTER)
        self.table2.heading("4",text="HostName",anchor=tk.CENTER)
        self.table2.heading("2",text="Port",anchor=tk.CENTER)
        if len(self.connecteDevices) !=0 or len(self.trustedDevices) !=0  :
            for i in self.connecteDevices:
                self.table.insert("",tk.END,values=tuple([i[0],i[1][0],i[1][1],i[1][2]]))
            self.table.update()
            for i in self.trustedDevices:
                self.table2.insert("",tk.END,values=tuple(i))
            self.table2.update()        
        self.connectorFeature.append(self.table)
        self.connectorFeature.append(self.table2)
        self.placeConnector()
    def buildFile(self):
        self.cleaner(self.connectorFeature)
        self.placeFile
    def untrust(self):
        selected_item = self.table2.selection()[0]
        self.table2.delete(selected_item)
    def trust(self):
        selected = self.table.focus()
        self.trustedDevices.append(list(self.table.item(selected,"values")))
        self.table2.insert("",tk.END,tk.END,values=self.table.item(selected,"values"))
        self.table2.update()
    def placeConnector(self):
        self.label_A1.place(x=0,y=60)
        self.label_A2.place(x=0,y=100)
        self.label_A3.place(x=0,y=80)
        self.label_A4.place(x=0,y=40)
        self.label_A5.place(x=0,y=170)
        self.label_A6.place(x=0,y=210)
        self.label_A7.place(x=0,y=190)
        self.label_A8.place(x=0,y=150)
        self.entry_A1.place(x=80,y=60)
        self.entry_A3.place(x=80,y=80)
        self.entry_A2.place(x=80,y=100)
        self.entry_A4.place(x=80,y=170)
        self.entry_A6.place(x=80,y=190)
        self.entry_A5.place(x=80,y=210)
        self.button_A1.place(x=10,y=120)
        self.button_A2.place(x=95,y=120)
        self.button_A3.place(x=150,y=120)
        self.button_A4.place(x=10,y=240)
        self.button_A5.place(x=90,y=240)
        self.button_A6.place(x=740,y=290)
        self.button_A7.place(x=680,y=290)
        self.button_A8.place(x=640,y=290)
        self.table.place(x=220,y=60)
        self.table2.place(x=220,y=320)
        self.root.update()
    def placeFile(self):
        self.root.update()
    def cleaner(self,listFeatures:list):
        for i in listFeatures:
            i.destroy()
    def destroy(self):
        self.root.mainloop()





if __name__ == "__main__":
    connect = connector()
    app = application(connect)
    app.buildMain()
    app.placeMain()
    app.destroy()
    sys.exit()


