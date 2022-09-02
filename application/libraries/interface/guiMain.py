from ctypes import WinDLL
from libraries.database.database import databaseObject
from os import getcwd
from tkinter import Button
from tkinter import Text
from tkinter import END
from tkinter import Scrollbar
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
        print(getcwd().replace("\\", "/") +
              "/application/libraries/database/codest.ico")
        self.database.guiRoot.iconbitmap(
            getcwd().replace("\\", "/") + "/Project/MyMatcher/application/libraries/database/codest.ico")
        self.main()

    def main(self):
        self.buildButton()
        self.buildText()
        self.destroy()

    def buildButton(self) -> None:
        self.buttonA1 = Button(self.database.guiRoot,
                               text="File Handler", width=10, borderwidth=0)
        self.buttonA2 = Button(self.database.guiRoot,
                               text="Connector", width=10, borderwidth=0)
        self.placeButton()

    def placeButton(self) -> None:
        self.buttonA1.place(x=0, y=0)
        self.buttonA2.place(x=80, y=0)

    def buildText(self):
        self.ScrollBar = Scrollbar(
            self.database.guiRoot, activebackground="black", bg="white", width=10)
        self.textBox = Text(self.database.guiRoot, width=30,
                            height=36, yscrollcommand=self.ScrollBar.set)
        for i in range(0, 100):
            self.textBox.insert(END, "No selected WorkSpace"+str(i)+"\n")

        self.placeText()

    def placeText(self):
        self.textBox.place(x=5, y=20)
        self.ScrollBar.place(x=250, y=300)

    def buildLabel(self) -> None:
        pass

    def placeLabel(self) -> None:
        pass

    def destroy(self) -> None:
        self.database.guiRoot.mainloop()
