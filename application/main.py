from libraries.database.database import databaseObject
from tkinter import Tk
from libraries.interface.guiMain import guiMain
if __name__ == "__main__":
    database = databaseObject()
    guiRoot = Tk()
    database.guiRoot = guiRoot
    guiMain = guiMain(database)
