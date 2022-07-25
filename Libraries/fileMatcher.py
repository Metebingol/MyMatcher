import os


class fileMatch():
    def __init__(self) -> None:
        pass
    def fileComparer(self,file_1:str,file_2:str,printo=1):
        try:
            file_1Content = open(file_1,"r")
            file_2Content = open(file_2,"r")
        except:
            return -1 
        if file_1Content.readlines() == file_2Content.readlines():
            return 1 
        else: return 0
    def dirComparer(self,dir1:str,dir2:str):
        listSame = []
        listSameindex = []
        listDiff1 = []
        listDiff2 = []
        listFiles1 = os.listdir(dir1)
        listFiles2 = os.listdir(dir2)
        for i in listFiles1:
            for j in listFiles2:
                if i == j:
                    listSame.append(i)
                    listSameindex.append(listFiles2.index(i)) # listSameindex  :  [[ index1  , index2  ]  , [index1  , index2]]
                    break
            if i != j:
                listDiff1.append(i)
        for i in listFiles2:
            if listFiles2.index(i) in listSameindex:
                continue
            listDiff2.append(i)
        return {"Same":listSame,
                "diff1":listDiff1,
                "diff2":listDiff2}









