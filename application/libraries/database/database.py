from tkinter import Tk


class databaseObject():
    def __init__(self) -> None:
        self.guiRoot: Tk
        self.guiRoot = None
        self.guiMainFeature = []
        self.guiFileHandlerFeature = []
        self.guiConnectionFeature = []
