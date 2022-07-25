import tkinter as tk
from tkinter import ttk 
from Libraries.connector import connector
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
        self.allFeature = []
        self.connectorFeature = []
        self.fileFeature = []
    def buildMain(self):
        self.menuMatch = tk.Button(self.root,text="FileMathcer",command=self.buildFile)
        self.menuConn = tk.Button(self.root,text="Connector",command=self.buildConnector) 
    def placeMain(self):
        self.menuMatch.place(x=0,y=0)
        self.menuConn.place(x=75,y=0)
    def buildConnector(self):
        self.cleaner(self.fileFeature)
        self.label_A1 = tk.Label(self.root,text="   HostName")
        self.label_A2 = tk.Label(self.root,text="   IP")
        self.label_A3 = tk.Label(self.root,text="   Port")
        self.label_A4 = tk.Label(self.root,text="MyDevices:")
        self.connectorFeature.append(self.label_A1)
        self.connectorFeature.append(self.label_A2)
        self.connectorFeature.append(self.label_A3)
        self.connectorFeature.append(self.label_A4)
        #
        self.entry_A1 = tk.Entry(self.root)
        self.entry_A1.insert(0,str(self.conn.hostName))
        self.entry_A2 = tk.Entry(self.root)
        self.entry_A2.insert(0,str(self.conn.IP))
        self.entry_A3 = tk.Entry(self.root)
        self.entry_A3.insert(0,str(self.conn.port))  
        self.connectorFeature.append(self.entry_A1)
        self.connectorFeature.append(self.entry_A2)
        self.connectorFeature.append(self.entry_A3)
        #
        self.button_A1 = tk.Button(self.root,text="Make Server",width=10)
        self.button_A2 = tk.Button(self.root,text="Accept",width=6)
        self.button_A3 = tk.Button(self.root,text="Close",width=6)
        self.connectorFeature.append(self.button_A1)
        self.connectorFeature.append(self.button_A2)
        self.connectorFeature.append(self.button_A3)
        self.placeConnector()
    def buildFile(self):
        self.cleaner(self.connectorFeature)
        self.placeFile
    def placeConnector(self):
        self.label_A1.place(x=0,y=60)
        self.label_A2.place(x=0,y=100)
        self.label_A3.place(x=0,y=80)
        self.label_A4.place(x=0,y=40)
        self.entry_A1.place(x=80,y=60)
        self.entry_A2.place(x=80,y=80)
        self.entry_A3.place(x=80,y=100)
        self.button_A1.place(x=10,y=120)
        self.button_A2.place(x=95,y=120)
        self.button_A3.place(x=150,y=120)
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


