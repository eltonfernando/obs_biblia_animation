import logging
from os.path import isfile
loger=logging.getLogger(__name__)
class OpenTxt():
    def __init__(self):
        logging.basicConfig(filename='OpenTxt.log',filemode='a', level=logging.INFO)
    def read_data(self,path):
        data = []
        if not isfile(path):
            loger.warning("Arquivo %s não existe",path)
            return data

        with open(path,"r",encoding="utf-8") as file:
            data=file.read().strip().split("\n")
        print(data)
        loger.info("lendo")
    def write_data(self,path,line_data):
        data=self.read_data(path)
        if line_data in data:
            print("exite",line_data)

        with open(path,"a",encoding="utf-8") as info:
            info.write(line_data+"\n")

if __name__=="__main__":
    txt=OpenTxt()
    txt.read_data("./../historico/cargos.txt")
   # logging.StreamHandler()
    #import time
    #time.sleep(10)