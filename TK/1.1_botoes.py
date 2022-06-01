from tkinter import *

janela = Tk()
janela.geometry('600x600+600+100')
janela.config(background='lightblue')

janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)

btn1 = Button(janela, text='Botão 1', font='Arial 15', command='')
btn2 = Button(janela, text='Botão 2', font='Arial 15', command='')
btn3 = Button(janela, text='Botão 3', font='Arial 15', command='')
btn4 = Button(janela, text='Botão 4', font='Arial 15', command='')
btn5 = Button(janela, text='Botão 5', font='Arial 15', command='')
btn6 = Button(janela, text='Botão 6', font='Arial 15', command='')

btn1.grid(row=0, column=0, sticky=NSEW)
btn2.grid(row=0, column=1, sticky=NSEW)
btn3.grid(row=0, column=2, sticky=NSEW)
btn4.grid(row=1, column=0, sticky=NSEW)
btn5.grid(row=1, column=1, sticky=NSEW)
btn6.grid(row=1, column=2, sticky=NSEW)

janela.mainloop()