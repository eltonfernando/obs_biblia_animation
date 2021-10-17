from bs4 import BeautifulSoup
import os

class Historico:
    def __init__(self):
        self.path="historico"
    def get_cargo_apresentador(self):
        cargos = open(os.path.join(self.path , "cargos.txt"),"r").read().strip().split("\n")
        return cargos
    def get_name_apresentador(self):
        people_names = open(os.path.join(self.path , "people_names.txt"),"r",encoding="utf-8").read().strip().split("\n")
        return people_names
    def set_cargo_apresentador(self,cargo):
        with open(os.path.join(self.path , "cargos.txt"),"a",encoding="utf-8") as info:
            info.write(cargo+"\n")
    def set_name_apresentador(self,name):
        names =self.get_name_apresentador()
        if name in names:
            print("nome ja existe")
        elif name+" " in names:
            print("nome ja existe")
        with open(os.path.join(self.path , "people_names.txt"),"a",encoding="utf-8") as info:
            info.write(name+"\n")
    def delete_people_name(self,name):
        cargos = open(os.path.join(self.path , "people_names.txt"),"r",encoding="utf-8").read().strip().split("\n")
        if name in cargos:
            del cargos[cargos.index(name)]
        with open(os.path.join(self.path , "people_names.txt"),"w",encoding="utf-8") as info:
            for c in cargos:
                info.write(c+"\n")

    def delete_cargo(self,cargo):
        cargos=[]
        with open(os.path.join(self.path, "cargos.txt"),"r",encoding="utf-8") as file:
            cargos=file.read().strip().split("\n")

        if cargo in cargos:
            del cargos[cargos.index(cargo)]
        with open(os.path.join(self.path, "cargos.txt"),"w",encoding="utf-8") as info:
            for c in cargos:
                info.write(c+"\n")

    def update_apresentador(self,apresenador,cargo):
        with open(os.path.join("templates","aviso.html"),"r",encoding="utf-8") as inf:
            txt = inf.read()
        inport_soup = BeautifulSoup(txt, features="html.parser")

        inport_soup.h2.string = apresenador
        inport_soup.h1.string = cargo
        with open(os.path.join("templates","aviso.html"), 'w',encoding="utf-8") as file:
            file.write(str(inport_soup))
if __name__=="__main__":
    ob=Historico()
    livros=ob.get_name_livro_all()
    print(livros)
    for name in livros:
        print(name)
   # with open(ob.path+"li.txt","w") as info:
   #     for name in livros:
    #        info.writelines(name+"\n")

