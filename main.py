from tkinter import *

master = Tk()
master.title('Calculadora de IMC')
master.geometry('490x560+670+250')

# Definir função para o botão

def bt_click():

    peso = float(peso_str.get())
    altura = float(altura_str.get())
    imc = peso / (altura **2)
    if imc < 18.5:
        resultado['text'] = f'IMC = {imc:.2F} \n \n ABAIXO DO PESO NORMAL'
    elif imc >= 18.5 and imc <= 24.9:
        resultado['text'] = f'IMC = {imc:.2f} \n \n PESO NORMAL'
    elif imc > 24.9 and imc < 29.9 :
        resultado['text'] = f'IMC = {imc:.2f} \n \n SOBREPESO'
    elif imc >= 29.9 and imc < 34.9:
        resultado['text'] = f'IMC = {imc:.2f} \n \n OBESIDADE GRAU I'
    else:
        resultado['text'] = f'IMC = {imc:.2f} \n \n OBESIDADE GRAU II'

fundo_tela = PhotoImage(file='tela.png')
lab_fundo = Label(master, image=fundo_tela)
lab_fundo.pack()

texto_inicial = Label(master, text='Calculadora de I.M.C.', font=('Verdana', 15, 'bold'))
texto_inicial.place(width=270, height=40, x=110, y=20)

texto_peso = Label(master, text='Peso (kg):', font=('Verdana', 10, 'bold'))
texto_peso.place(width=200, height=30, x=146, y=90)
peso_str = Entry(master, font=('Verdana', 10, 'bold'), justify=CENTER)
peso_str.place(width=200, height=30, x=146, y=130)


texto_altura = Label(master, text='Altura (cm):', font=('Verdana', 10, 'bold'))
texto_altura.place(width=200, height=30, x=146, y=180)
altura_str = Entry(master, font=('Verdana', 10, 'bold'), justify=CENTER)
altura_str.place(width=200, height=30, x=146, y=220)

botao = Button(master, text='Calcular', font=('Verdana', 10, 'bold'), command=bt_click)
botao.place(width=200, height=30, x=146, y= 260)

resultado = Label(master, text='Resultado', font=('Verdana', 10, 'bold'))
resultado.place(width=200, height=200, x=146, y=310)

master.mainloop()

