from tkinter import *

def imprimirdados():
    text = Label(screen,text=nome.get(),background='lightblue',foreground='black')
    text.place(x=300,y=150)
    

font=('Arial',20)

screen = Tk()

screen.title('😃👍')
screen.geometry('500x300')
screen.configure(background='lightblue')

text1 = Label (screen,text="EXEMPLO TKINTER" ,background='#dde',foreground='Blue',anchor=W).place(x=220,y=2,height=12,width=110)
line=Label(screen,text='',background='red').place(x=0,y=13,height=7,width=500)

text = Label(screen,text='Nome',background='lightblue',foreground='black')
text.place(x=10,y=20)

nome = Entry(screen)
nome.place(x=10,y=40)

Label(screen,text="Telefone",background="lightblue",foreground='black',anchor=W).place(x=10,y=60,height=30,width=60)
vfone = Entry(screen)
vfone.place(x=10,y=80)

Label(screen,text='E-MAIL',background='lightblue',foreground='black',anchor=W).place(x=10,y=100,height=40,width=200)
vemail = Entry(screen)
vemail.place(x=10,y=130)

Label(screen,text='OBS',background='lightblue',foreground='black',anchor=W).place(x=10,y=170,height=10,width=30)
vobs= Entry(screen)
vobs.place(x=10,y=190,width=200,height=60)

button = Button(screen,text='sair',background='red',foreground='white',command=screen.destroy)
button.place(x=250,y=270,height=20,width=50)

button2 = Button(screen,text='imprimir',background='red',foreground='white',command=imprimirdados)
button2.place(x=250,y=270,height=20,width=50)

screen.mainloop()