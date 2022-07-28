from database.database import database
from tkinter import Tk




class guiFiler():
    def __init__(self,root:Tk,data:database) -> None:
        self.root = root
        self.data = data
    def build(self):
        for feature in self.data.connectorFeature:
            feature.destroy()
        self.root.update()