from tkinter import *

# back-end
fonte = ('Arial 15')

def fahrenheit():
    if float(c_Entry.get()) > 0:
        Fah = ( float(c_Entry.get()) * 1.8 + 32)
        resultado['text'] = (f'Resultado: {Fah:.2f}')

# front-end
janela = Tk()
janela.geometry('400x200+700+100')
janela.minsize(width=400, height=200)
janela.maxsize(width=500, height=300)
janela.config(background='lightblue')

janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(3, weight=1)

janela.grid_columnconfigure(0, weight=2)
janela.grid_columnconfigure(3, weight=2)

# criação de widgets
c = Label(janela, text='C°:', font=fonte)
c_Entry = Entry(janela, font=fonte)

btn1 = Button(janela, text='Converte °F', font=fonte, command=fahrenheit)

resultado = Label(janela, font=fonte)

# organizar wigdets
c.grid(row=1, column=1, sticky=NSEW)
c_Entry.grid(row=1, column=2, sticky=NSEW)

btn1.grid(row=2, column=1, sticky=NSEW)
resultado.grid(row=2, column=2, sticky=NSEW)

# executar a janela
janela.mainloop()