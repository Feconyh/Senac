# importar a biblioteca
from tkinter import *

#back-end
def imprimir():
    label1['text'] = entry1.get()
    #print('Olá Mundo!')


# front-end
# criar a janela
janela = Tk()
janela.geometry('600x600+600+100')
janela.minsize(width=600, height=600)
janela.maxsize(width=1200, height=1200)
janela.config(background='lightblue')

# criar os widgets
label1 = Label(janela, text='Olá mundo!', font='Arial 36 bold')
entry1 = Entry(janela, font='Arial 20')
btn1 = Button(janela, text='Sair', font='Arial 20', command=quit)
btn2 = Button(janela, text='Imprimir', font='Arial 20', command=imprimir)


# organizar os widgets
label1.pack()
entry1.pack()
btn1.pack()
btn2.pack()

# executar a janela
janela.mainloop()