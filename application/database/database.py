from socket import gethostname
from socket import gethostbyname




class database():
    def __init__(self) -> None:
        self.guiRoot = None
        self.connectorFeature = []
        self.filerFeature = []
        self.hostname = gethostname()
        self.IP = gethostbyname(self.hostname)



