"""
Busca verso biblico
"""
import requests
from PyQt5.QtCore import QThread, pyqtSignal
from bs4 import BeautifulSoup

class Biblia(QThread):
    text_log = pyqtSignal(str)
    def __init__(self):
        super(Biblia, self).__init__()
        self.url = "https://www.bibliaonline.com.br/aa/"
        self.livro = ""
        self.versiculo = ""
        self.capitulo = ""
        self.page_html = ""
        self.soup=""
        #self.text_log = pyqtSignal(str)
    def run(self):
        page_html = self.get_html()
        self.soup = BeautifulSoup(page_html, 'html.parser')

        self.text_log.emit(self.get_text_versiculo())

    def get_html(self):
        if self.livro=="Daniel":
            self.livro="dn"

        url = self.url + self.livro + "/" + self.capitulo + "/" + self.versiculo
        print(url)
        page_html = requests.get(url).content
        return page_html

    def set_livro(self, livro):
        self.livro = livro

    def set_capitulo(self, capitulo):
        self.capitulo = str(capitulo)

    def set_versiculo(self, versiculo):
        self.versiculo = str(versiculo)

    def get_text_versiculo(self):
        text_versiculo = self.soup.find("p", class_="jss35")
        if text_versiculo is None:
            return "ERRO versiculo não existe"
        return text_versiculo.string

    def get_text_livro(self):
        livro = self.soup.find("a", class_="jss25 jss39")
        if livro is None:
            return "ERRO"
        return livro.string
    def update_template(self,):
        with open("templates/biblia.html", "r") as inf:
            txt = inf.read()
        inport_soup = BeautifulSoup(txt, features="html.parser")

        inport_soup.h1.string = self.get_text_livro()
        inport_soup.h2.string = self.get_text_versiculo()
        with open("templates/biblia.html", 'w') as file:
            file.write(str(inport_soup))

if __name__=="__main__":
    ob=Biblia()
    ob.set_livro("dn")
    ob.set_capitulo(1)
    ob.set_versiculo(1)
    ob.start()
    while ob.isRunning():
        pass

    print(ob.get_text_versiculo())
    print(ob.get_text_livro())
#    ob.update_template()