import socket as sc





class connector():
    def __init__(self) -> None:
        self.hostName = sc.gethostname()
        self.IP = sc.gethostbyname(self.hostName)
        self.port = 80
