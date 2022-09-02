from libraries.database.database import databaseObject
from os import getcwd
from tkinter import Button

"""
Information for this user interface code package:
General=> This is code package for main window for application 
ButtonA1:

"""


class guiMain():
    def __init__(self, database: databaseObject) -> None:
        self.database = database
        self.database.guiRoot.geometry("800x600")
        self.database.guiRoot.resizable(False, False)
        self.database.guiRoot.iconbitmap(
            getcwd().replace("\\", "/") + "/application/libraries/database/codest.ico")

        self.destroy()

    def buildButton(self) -> None:
        buttonA1 = Button(self.database.guiRoot, text="Hello")

    def placeButton(self) -> None:
        pass

    def buildLabel(self) -> None:
        pass

    def placeLabel(self) -> None:
        pass

    def destroy(self) -> None:
        self.database.guiRoot.mainloop()
