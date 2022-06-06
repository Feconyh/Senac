from tkinter import *

janela = Tk()
janela.geometry('600x600+600+100')
janela.config(background='lightblue')

f1 = Frame(janela)
f1.grid()

def aumenta():
    if int(numero["text"]) < 10:
        numero["text"] = int(numero["text"]) + 1
def diminui():
    if int(numero["text"]) > -10:
        numero["text"] = int(numero["text"]) - 1

janela.grid_rowconfigure(0, weight=1)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)

numero = Label(f1, text='0', background='lightblue', font='Arial 15')

btn1 = Button(f1, text='Botão 1', font='Arial 15', command=diminui)
btn2 = Button(f1, text='Botão 2', font='Arial 15', command=aumenta)

numero.grid(row=0, column=1, stick=NSEW)

btn1.grid(row=0, column=0, sticky=NSEW)
btn2.grid(row=0, column=2, sticky=NSEW)

janela.mainloop()