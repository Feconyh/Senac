from tkinter import *

#back-end
def soma():
    if entry1.get().isnumeric() and entry2.get().isnumeric():
        resultado["text"] = int(entry1.get()) + int(entry2.get())
    else:
        resultado['text'] = 'Valor Invalido'
def subtracao():
    if entry1.get().isnumeric() and entry2.get().isnumeric():
        resultado["text"] = int(entry1.get()) - int(entry2.get())
    else:
        resultado['text'] = 'Valor Invalido'
def multiplicacao():
    if entry1.get().isnumeric() and entry2.get().isnumeric():    
        resultado["text"] = int(entry1.get()) * int(entry2.get())
    else:
        resultado['text'] = 'Valor Invalido'
def divisao():
    if entry1.get().isnumeric() and entry2.get().isnumeric():
        resultado["text"] = int(entry1.get()) / int(entry2.get())
    else:
        resultado['text'] = 'Valor Invalido'

# front-end
# criar a janela
janela = Tk()
janela.geometry('600x600+600+100')
janela.config(background='lightblue')

# criar os widgets
label1 = Label(janela, text='1º números', background='lightblue', font='Arial 15 bold')
entry1 = Entry(janela, font='Arial 15')

label2 = Label(janela, text='2º números', background='lightblue', font='Arial 15 bold')
entry2 = Entry(janela, font='Arial 15')

soma = Button(janela, text='soma', command=soma)
subtracao = Button(janela, text='subtracao', command=subtracao)
multiplicacao = Button(janela, text='multiplicacao', command=multiplicacao)
divisao = Button(janela, text='divisao', command=divisao)

resultado = Label(janela, background='lightblue', font='Arial 20')

# organizar os widgets
label1.pack()
entry1.pack()

label2.pack()
entry2.pack()

soma.pack()
subtracao.pack()
multiplicacao.pack()
divisao.pack()

resultado.pack()

# executar a janela
janela.mainloop()