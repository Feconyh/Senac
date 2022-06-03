from tkinter import *

# =======================================   Back-end    ==========================================================
screen = Tk()
screen.geometry('500x850+600+100')
screen.config(background='gray')

class Botao():

    def botao(nome,texto,comando,y,x):
        nome = Button(screen, text=texto, font=fonte, background='white', command=comando)
        nome.grid(row=y, column=x, sticky=NSEW)

    def entrada(valor):
        visor['text'] += valor

    def sim(botao):
        screen.bind(botao, lambda event: Botao.entrada(botao))

    def btn_c():
        visor['text'] = ''

    def btn_delete():
        visor['text'] = ''

    def resultado_final():
        resultado = eval(visor['text'])
        visor['text'] = str(resultado)

# =======================================   Front-end    ==========================================================
fonte = 'Arial 15'

for row in range(6):
    screen.grid_rowconfigure(row, weight=1)
for column in range(4):
    screen.grid_columnconfigure(column, weight=1)

visor = Label(screen, text='', font=fonte, background='gray')
visor.grid(row=0, columnspan=4, sticky=NSEW)

# =======================================   criando widgets / organiznado widgets    =============================
# =======================================                Números                     =============================
Botao.botao('btn1','1',Botao.sim('1'),3,0)
Botao.botao('btn2','2',Botao.sim('2'),3,1)
Botao.botao('btn3','3',Botao.sim('3'),3,2)
Botao.botao('btn4','4',Botao.sim('4'),2,0)
Botao.botao('btn5','5',Botao.sim('5'),2,1)
Botao.botao('btn6','6',Botao.sim('6'),2,2)
Botao.botao('btn7','7',Botao.sim('7'),1,0)
Botao.botao('btn8','8',Botao.sim('8'),1,1)
Botao.botao('btn9','9',Botao.sim('9'),1,2)
Botao.botao('btn0','0',Botao.sim('0'),4,0)

# =============================================         utilitarios    ===========================================
Botao.botao('btn_c','C',Botao.btn_c,5,1)
Botao.botao('btn_delete','Del',Botao.btn_delete,5,0)
Botao.botao('btn_virgula','‚',Botao.sim(','),5,2)
Botao.botao('btn_parentese1','(',Botao.sim('('),4,1)
Botao.botao('btn_parentese2',')',Botao.sim(')'),4,2)

# =======================================           simbolos de calculos    =======================================
Botao.botao('btn_igual','=',Botao.resultado_final,5,3)
Botao.botao('btn_mais','+',Botao.sim('+'),4,3)
Botao.botao('btn_menos','–',Botao.sim('-'),3,3)
Botao.botao('btn_vezes','×',Botao.sim('*'),2,3)
Botao.botao('btn_divisao','÷',Botao.sim('/'),1,3)

# =======================================           executando janela    =========================================
screen.mainloop()