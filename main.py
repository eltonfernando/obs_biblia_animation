"""
Autor :Elton Fernandes dos Santos
data : 07/11/2020

Descrição : busca ver biblico "https://www.bibliaonline.com.br/aa/"

"""
import os

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from bs4 import BeautifulSoup

import data_base
from core.biblia_const import LIVRO_COMBO, LIVRO_DB, LIVRO_PT
from memoria import Historico
from setup import __VERSION__

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("from.ui", self)
        self.setWindowTitle(f"Bíblia para OBS {__VERSION__}")
        self.historico = Historico()
        self.start_combox_name_apresentador()
        self.start_combox_cargo()

        for name_livro in LIVRO_COMBO:
            self.comboBox_livro.addItem(name_livro)

    def start_combox_name_apresentador(self):
        self.comboBox_name_apresentador.clear()
        for name_people in self.historico.get_name_apresentador():
            self.comboBox_name_apresentador.addItem(name_people)

    def start_combox_cargo(self):
        self.comboBox_cargo.clear()
        for name_cargos in self.historico.get_cargo_apresentador():
            self.comboBox_cargo.addItem(name_cargos)

    def on_comboBox_livro_currentTextChanged(self, index):
        print("indes", index)

    @pyqtSlot()
    def on_pushButton_buscar_clicked(self):

        current_livro = self.comboBox_livro.currentText()
        index_livro = self.comboBox_livro.currentIndex()

        versiculo = self.spinBox_versiculo.value()
        capitulo = self.spinBox_capitulo.value()

        db = data_base.Connect(LIVRO_DB[index_livro])
        lista_vercisulo = db.get_versiculo(capitulo, versiculo)
        print(lista_vercisulo)
        print(LIVRO_PT[index_livro], capitulo, versiculo)
        if not lista_vercisulo:
            self.textEdit_saida.setText("Versiculo não existe")
        else:
            text_livro = LIVRO_PT[index_livro] + " " + str(lista_vercisulo[0][1]) + " : " + str(lista_vercisulo[0][2])
            self.textEdit_saida.setText(text_livro + "\n" + str(lista_vercisulo[0][3]))
            self.update_template_html(text_livro, lista_vercisulo[0][3])
            with open(os.path.join("templates", "livro.txt"), "w", encoding="utf-8") as file:
                file.write(text_livro)
            with open(os.path.join("templates", "versiculo.txt"), "w", encoding="utf-8") as file:
                file.write(lista_vercisulo[0][3])

    @pyqtSlot()
    def on_pushButton_criar_apresentador_clicked(self):
        apresentador = self.comboBox_name_apresentador.currentText()
        cargo = self.comboBox_cargo.currentText()
        self.historico.update_apresentador(apresentador, cargo)

    @pyqtSlot()
    def on_pushButton_delete_people_clicked(self):
        self.historico.delete_people_name(self.comboBox_name_apresentador.currentText())
        self.start_combox_name_apresentador()

    @pyqtSlot()
    def on_pushButton_delete_cargo_clicked(self):
        self.historico.delete_cargo(self.comboBox_cargo.currentText())
        self.start_combox_cargo()

    @pyqtSlot()
    def on_pushButton_save_cargo_clicked(self):
        cargo:str = self.comboBox_cargo.currentText()
        self.historico.set_cargo_apresentador(cargo)
        self.start_combox_cargo()
        idex = self.comboBox_cargo.findText(cargo)
        self.comboBox_cargo.setCurrentIndex(idex)

    @pyqtSlot()
    def on_pushButton_salve_people_clicked(self):
        name:str = self.comboBox_name_apresentador.currentText()
        self.historico.set_name_apresentador(name)
        self.start_combox_name_apresentador()
        idex = self.comboBox_name_apresentador.findText(name)
        self.comboBox_name_apresentador.setCurrentIndex(idex)

    def update_template_html(self, livro, texto):
        with open(os.path.join("templates", "biblia.html"), "r", encoding="utf-8") as inf:
            txt = inf.read()
        inport_soup = BeautifulSoup(txt, features="html.parser")

        inport_soup.h1.string = livro
        inport_soup.h2.string = texto
        with open(os.path.join("templates", "biblia.html"), 'w', encoding="utf-8") as file:
            file.write(str(inport_soup))


if __name__ == "__main__":
    import sys
    import logging

    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)s:%(filename)s:%(funcName)s:%(asctime)s:%(message)s',
                        filename="loger.log", )
    app = QApplication(sys.argv)
    tela = Main()
    tela.show()
    app.exec_()
