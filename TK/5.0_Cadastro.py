from mailbox import NotEmptyError
from tkinter import *

# =======================================   Back-end    ==========================================================
root = Tk()
root.geometry = ('600x600+700+100')
root.config(background='lightblue')
root.minsize(width=500, height=400)

fonte = 'Arial 15'

f1 = Frame(root)
f1.grid()

f2 = Frame(root)
f2.grid()

f3 = Frame(root)
f3.grid()

class Dados_Pessoais:
    def nome(conteudo1, conteudo2):
        conteudo1 = Label(f1, text=conteudo1, background='lightblue')
        conteudo2 = Entry(f1)
        conteudo1.grid(row = 2, column = 1, sticky=NSEW)
        conteudo2.grid(row = 2, column = 2, sticky=NSEW)

    def data_nasc(conteudo1, conteudo2):
        conteudo1 = Label(f1, text=conteudo1, background='lightblue')
        conteudo2 = Entry(f1)
        conteudo1.grid(row = 3, column = 1)
        conteudo2.grid(row = 3, column = 2)

    def cpf(conteudo1, conteudo2):
        conteudo1 = Label(f1, text=conteudo1, background='lightblue')
        conteudo2 = Entry(f1)
        conteudo1.grid(row = 4, column = 1)
        conteudo2.grid(row = 4, column = 2)

    def telefone(conteudo1, conteudo2):
        conteudo1 = Label(f1, text=conteudo1, background='lightblue')
        conteudo2 = Entry(f1)
        conteudo1.grid(row = 5, column = 1)
        conteudo2.grid(row = 5, column = 2)

class Endereco():
    def rua(conteudo1, conteudo2):
        conteudo1 = Label(f2, text=conteudo1, background='lightblue')
        conteudo2 = Entry(f2)
        conteudo1.grid(row = 7, column = 1, sticky=NSEW)
        conteudo2.grid(row = 7, column = 2, sticky=NSEW)

    def numero(conteudo1, conteudo2):
        conteudo1 = Label(f2, text=conteudo1, background='lightblue')
        conteudo2 = Entry(f2)
        conteudo1.grid(row = 8, column = 1)
        conteudo2.grid(row = 8, column = 2)

    def bairro(conteudo1, conteudo2):
        conteudo1 = Label(f2, text=conteudo1, background='lightblue')
        conteudo2 = Entry(f2)
        conteudo1.grid(row = 9, column = 1, sticky=NSEW)
        conteudo2.grid(row = 9, column = 2, sticky=NSEW)

    def cidade(conteudo1, conteudo2):
        conteudo1 = Label(f2, text=conteudo1, background='lightblue')
        conteudo2 = Entry(f2)
        conteudo1.grid(row = 10, column = 1)
        conteudo2.grid(row = 10, column = 2)

    def uf(conteudo1, conteudo2):
        conteudo1 = Label(f2, text=conteudo1, background='lightblue')
        conteudo2 = Entry(f2)
        conteudo1.grid(row = 11, column = 1)
        conteudo2.grid(row = 11, column = 2)

class Botao():
    def botao(conteudo, row, column):
        conteudo = Button(f3, text=conteudo)
        conteudo.grid(row = row, column = column)

# =======================================   Front-end    ==========================================================
for row in range(13):
    root.grid_rowconfigure(row, weight=1)
for column in range(2):
    root.grid_columnconfigure(column, weight=1)
# =======================================   criando widgets / organiznado widgets    =============================

Dados_Pessoais.nome('Nome', 'Nome')
Dados_Pessoais.data_nasc('Data_Nasc', 'Data_Nasc')
Dados_Pessoais.cpf('CPF', 'CPF')
Dados_Pessoais.telefone('Telefone', 'Telefone')

Endereco.rua('rua','rua')
Endereco.numero('numero','numero')
Endereco.bairro('bairro','bairro')
Endereco.cidade('cidade','cidade')
Endereco.uf('uf','uf')

Botao.botao('btn1', 13, 1)
Botao.botao('btn2', 13, 2)

# =======================================           executando janela    =========================================
root.mainloop()