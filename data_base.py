import sqlite3
import io
import os
import datetime

"""
    File name         : data_base.py
    File Description  : controle banco de dado
                      :
    Author            : Eng. Elton Fernandes dos Santos
    Date created      : 03/08/2020
    Version           : v2.7
    Python Version    : 3.8
    tempo de para escrita 4.8 ms (12% do loop de 33.33ms)
    tempo de leitura 5 ms e acrescenta mas 5 ms a cada mil linhas adicionada
"""

import logging

class Connect:

    def __init__(self,tabela="gn"):

        self.db_name="biblia_aa"
        self.tabela=tabela
        if not os.path.isfile(self.db_name+'.db'):
            print("sem banco")
            self.conn = sqlite3.connect(self.db_name + ".db")
            self.cursor = self.conn.cursor()
            self.create_db()
            self.close_db()
        try:
            # conectando...
            self.conn = sqlite3.connect(self.db_name+".db")
            self.cursor = self.conn.cursor()
            #print("Banco:", db_name)
            #self.cursor.execute('SELECT SQLITE_VERSION()')
            #self.data = self.cursor.fetchone()
            #print(self.data)
        except sqlite3.Error as e:
           # print("Erro ao abrir banco.")
           message=f'ERROR OPEN BANCO\n' \
                   f'name banco {self.db_name}.db \n' \
                   f'erro {e}'
           logging.critical(message)

    def get_all_data(self):
        """
        seleciona todas as linha do banco
        Returns:lista de tupla com linhas selecionadas do banco
        """
       # print("buscando",self.db_name)
        self.cursor.execute("SELECT * FROM "+self.tabela+" ;")
        data=self.cursor.fetchall()
        self.close_db()
        return data
    def get_versiculo(self,capitulo,versiculo):
        """
        busa em self.tabela na coluna colunn todos valor igual a busca
        Args:
            colunn: coluna da pesquisa
            busca: valor a ser buscado (str ou float int)

        Returns: lista de tupla com linhas selecionadas do banco
        """
        data=[]
        #print("buscando data")
        try:
            self.cursor.execute("SELECT * FROM "+self.tabela+"  WHERE capitulo=? AND versiculo =?", (capitulo,versiculo))
            data=self.cursor.fetchall()

        except sqlite3.OperationalError as e:
            message = f'ERROR BANCO SELECT WERE DATA\n' \
                      f'name banco {self.db_name}.db \n' \
                      f'erro {e}'
            logging.critical(message)
        self.close_db()
        return data

    def add(self,lista):
        """
        Adiciona o novo evento ao banco
        Args:
            lista: Lista com dados de entrada

        Returns: sem retorno

        """
        try:
            #add new produto ao banco
            self.cursor.execute("INSERT INTO "+self.tabela+" (capitulo,versiculo,texto) VALUES (?,?,?)",lista)
            # gravando no bd
            self.conn.commit()
            #print('Salve no banco .')

        except sqlite3.OperationalError as e:
            message = f'ERROR BANCO INSERT\n' \
                      f'name banco {self.db_name}.db \n' \
                      f'erro {e}'
            logging.critical(message)
        self.close_db()

    def update(self,id,colunn,valor):
        """
        Edita linha do banco pelo id unico
        Args:
            id: id da linha a ser editada
            colunn: coluna a ser editada
            valor: novo valor atribuido
        Returns: sem retorno
        """
        try:
            # alterando os dados da tabela
            self.cursor.execute("UPDATE "+self.tabela+"  SET "+colunn+" = ?  WHERE id = ?", (valor,id))
            self.conn.commit()
            self.close_db()
        except sqlite3.OperationalError as e:
            message = f'ERROR BANCO UPDATE\n' \
                      f'name banco {self.db_name}.db \n' \
                      f'erro {e}'
            logging.critical(message)
        self.close_db()

    def delete(self,id):
        """
        Deleta uma linha dado ao ID
        Args:
            id: ID indetificador unico
        Returns: sem retorno
        """
          # excluindo um registro da tabela
        self.cursor.execute("DELETE FROM "+self.tabela+" WHERE id = ?", (id,))
        self.conn.commit()
       # print('Registro excluido com sucesso.')
        self.close_db()

    # def commit_db(self):
    #     if self.conn:
    #         self.conn.commit()

    def close_db(self):
        if self.conn:
            self.conn.close()

    def create_db(self):
        """
        Usada para criar tabelas do banco
        :return: nada
        """
        #print("criando")
        # criando a tabela (schema)
        self.cursor.execute("""
        CREATE TABLE """ + self.tabela+ """(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                capitulo INTEGER NOT NULL,
                versiculo INTEGER NOT NULL,
                texto TEXT NOT NULL          
        );
        """)

        print('Tabela criada com sucesso.')
        # desconectando...

if __name__ == '__main__':
    db=Connect("db_event","db_event")
    db.create_db()