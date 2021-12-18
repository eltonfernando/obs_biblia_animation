import logging
import os

from bs4 import BeautifulSoup

from core.historico_io import OpenTxt


class Historico:
    def __init__(self):
        self.path = "historico"
        self.log = logging.getLogger(__name__)

    def get_cargo_apresentador(self):
        txt = OpenTxt()
        cargos = txt.read_data(os.path.join(self.path, "cargos.txt"))
        return cargos

    def get_name_apresentador(self):
        path_file = os.path.join(self.path, "people_names.txt")
        people_names = OpenTxt().read_data(path_file)
        return people_names

    def set_cargo_apresentador(self, cargo: str):
        cargo = cargo.strip()
        path_file = os.path.join(self.path, "cargos.txt")
        get_cargos = self.get_cargo_apresentador()
        if cargo.capitalize() in get_cargos:
            self.log.info(f'cargo {cargo} ja existe')
        else:
            OpenTxt().write_data(path_file, cargo.capitalize())

    def set_name_apresentador(self, name: str):
        name = name.strip()
        path_file = os.path.join(self.path, "people_names.txt")
        names = self.get_name_apresentador()
        if name.capitalize() in names:
            self.log.info(f'cargo {name} ja existe')
        else:
            OpenTxt().write_data(path_file, name.capitalize())

    def delete_people_name(self, name):
        cargos = self.get_name_apresentador()
        if name.capitalize() in cargos:
            del cargos[cargos.index(name)]
        with open(os.path.join(self.path, "people_names.txt"), "w", encoding="utf-8") as info:
            for c in cargos:
                info.write(c + "\n")

    def delete_cargo(self, cargo):
        cargos = self.get_cargo_apresentador()

        if cargo.capitalize() in cargos:
            del cargos[cargos.index(cargo)]
        with open(os.path.join(self.path, "cargos.txt"), "w", encoding="utf-8") as info:
            for c in cargos:
                info.write(c + "\n")

    def update_apresentador(self, apresenador, cargo):
        with open(os.path.join("templates", "aviso.html"), "r", encoding="utf-8") as inf:
            txt = inf.read()
        inport_soup = BeautifulSoup(txt, features="html.parser")

        inport_soup.h2.string = apresenador
        inport_soup.h1.string = cargo
        with open(os.path.join("templates", "aviso.html"), 'w', encoding="utf-8") as file:
            file.write(str(inport_soup))


if __name__ == "__main__":
    pass
# ob=Historico()
# livros=ob.get_name_livro_all()
# print(livros)
# for name in livros:
#     print(name)
# with open(ob.path+"li.txt","w") as info:
#     for name in livros:
#        info.writelines(name+"\n")
