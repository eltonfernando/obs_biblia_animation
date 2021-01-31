import data_base
import time
from bs4 import BeautifulSoup
import requests
name_livros =open("historico/li.txt").read().strip().split("\n")
name_livros_tb =open("historico/livros.txt").read().strip().split("\n")
def get_verciculo(livro, cap,ver):
    url = home+livro + "/" +str(cap) + "/" + str(ver)
    print(url)
    while True:
        try:
            page_html = requests.get(url).content
            soup = BeautifulSoup(page_html, 'html.parser')
            text_versiculo = soup.find("p", class_="jss35")
            livro = soup.find("a", class_="jss25 jss39")
            return text_versiculo, livro
        except:
            print("try")





home = "https://www.bibliaonline.com.br/aa/"

#get_verciculo("gn",1,166)
#time.sleep(20)

#criando tabelas
#for livro in name_livros_tb[0:]:
#    db = data_base.Connect(livro)
#    db.create_db()


for livro in name_livros[0:]:
    aux_brak_cap=False
    for capitulo in range(1,151):
        if aux_brak_cap is True:
            break
        for versiculo in range(1,177):
            text_ver,ret_livro=get_verciculo(livro,capitulo,versiculo)
            if text_ver is None:
                print("findo do capitulo ",livro,capitulo,versiculo)
                aux_brak_cap=True
                break
            else:
                text_ver=text_ver.string
                ret_livro=ret_livro.string
                if text_ver is None:
                    print("fim do verciculo ",livro,capitulo,versiculo)
                    break
                else: #salva
                    save_livro=name_livros_tb[name_livros.index(livro)]
                    print("local ", save_livro,name_livros.index(livro))
                    print(capitulo,versiculo)
                    lista=[capitulo,versiculo,text_ver]
                    #print(lista)
                    db=data_base.Connect(save_livro)
                    db.add(lista)
                    del db





