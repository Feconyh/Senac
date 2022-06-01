from tkinter import *

# back-end
fonte = ('Arial 15')

def imc():
    if float(pesoE.get()) and float(alturaE.get()) > 0:
        limite = (float(pesoE.get()) / ( float(alturaE.get()) * float(alturaE.get()) ))
        resultado['text'] = (f'Resultado: {limite:.2f}')
    
# front-end
janela = Tk()
janela.geometry('600x600+700+100')
janela.minsize(width=400, height=200)
janela.maxsize(width=700, height=500)
janela.config(background='lightblue')

janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(5, weight=1)

janela.grid_columnconfigure(0, weight=2)
janela.grid_columnconfigure(3, weight=2)

# criação de widgets
pesoL = Label(janela, text='Peso:', background='lightblue', font=fonte)
pesoE = Entry(janela, font=fonte)

alturaL = Label(janela, text='Altura:', background='lightblue', font=fonte)
alturaE = Entry(janela, font=fonte)

btn1 = Button(janela, text='IMC', font=fonte, command=imc)

resultado = Label(janela, font=fonte)

# organizar wigdets
pesoL.grid(row=1, column=1, sticky=NSEW)
pesoE.grid(row=1, column=2, sticky=NSEW)

alturaL.grid(row=2, column=1, sticky=NSEW)
alturaE.grid(row=2, column=2, sticky=NSEW)

btn1.grid(row=3, column=2)

resultado.grid(row=4, column=2)

# executar a janela
janela.mainloop()