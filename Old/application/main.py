from tkinter import Tk
from database.database import database
from userInterface.gui3 import mainRoot
data = database()
rootConfig = mainRoot("MyMathcer", data)


if __name__ == "__main__":
    # This is main tkinter root for application
    root = Tk()
    data.guiRoot = root
    rootConfig.mainRootConfig(data.guiRoot)
    root.mainloop()
