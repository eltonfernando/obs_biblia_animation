"""
Autor :Elton Fernandes dos Santos
data : 07/11/2020

Descrição : busca ver biblico "https://www.bibliaonline.com.br/aa/"

"""
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtCore import pyqtSlot
from biblia import Biblia
from memoria import Historico
class Main(QMainWindow,Historico):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("from.ui",self)
        self.livros=self.get_name_livro_all()
        self.my_bibila=Biblia()
        self.start_combox_name_apresentador()
        self.start_combox_cargo()
        for name_livro in self.livros:
            self.comboBox_livro.addItem(name_livro)

        self.my_bibila.text_log.connect(self.test)
    def start_combox_name_apresentador(self):
        self.comboBox_name_apresentador.clear()
        for name_people in self.get_name_apresentador():
            self.comboBox_name_apresentador.addItem(name_people)

    def start_combox_cargo(self):
        self.comboBox_cargo.clear()
        for name_cargos in self.get_cargo_apresentador():
            self.comboBox_cargo.addItem(name_cargos)

    def test(self,msg):
        self.textEdit_saida.clear()
        self.textEdit_saida.append(self.my_bibila.get_text_livro())
        self.textEdit_saida.append(msg)
        self.my_bibila.update_template()

    def on_comboBox_livro_currentTextChanged(self,index):
        print("indes",index)

    @pyqtSlot()
    def on_pushButton_buscar_clicked(self):
        if not self.my_bibila.isRunning():
            print(self.comboBox_livro.currentText())
            print(self.spinBox_capitulo.value())
            self.my_bibila.set_livro(self.comboBox_livro.currentText())
            self.my_bibila.set_capitulo(self.spinBox_capitulo.value())
            self.my_bibila.set_versiculo(self.spinBox_versiculo.value())
            self.my_bibila.start()
    @pyqtSlot()
    def on_pushButton_criar_apresentador_clicked(self):
        apresentador=self.comboBox_name_apresentador.currentText()
        cargo=self.comboBox_cargo.currentText()
        self.update_apresentador(apresentador,cargo)
    @pyqtSlot()
    def on_pushButton_delete_people_clicked(self):
        self.delete_people_name(self.comboBox_name_apresentador.currentText())
        self.start_combox_name_apresentador()

    @pyqtSlot()
    def on_pushButton_delete_cargo_clicked(self):
        self.delete_cargo(self.comboBox_cargo.currentText())
        self.start_combox_cargo()


    @pyqtSlot()
    def on_pushButton_save_cargo_clicked(self):
        cargo=self.comboBox_cargo.currentText()
        self.set_cargo_apresentador(cargo)
        self.start_combox_cargo()
        idex = self.comboBox_cargo.findText(cargo)
        self.comboBox_cargo.setCurrentIndex(idex)

    @pyqtSlot()
    def on_pushButton_salve_people_clicked(self):
        name=self.comboBox_name_apresentador.currentText()
        self.set_name_apresentador(name)
        self.start_combox_name_apresentador()
        idex=self.comboBox_name_apresentador.findText(name)
        self.comboBox_name_apresentador.setCurrentIndex(idex)



if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    tela=Main()
    tela.show()
    app.exec_()