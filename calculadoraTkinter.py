"""
Nombre: calculadoraTkinter.py
Objetivo: Utilizar una interfaz grafica mediante la libreria tKinder
Autor: I Eduardo Ceja Tejeda
Fecha: 11/10/2019
"""
from tkinter import *
#RAIZ
raiz=Tk()
raiz.title("CALCULADORA")
#(ancho,alto) bloquemos dimensiones en la ventana
raiz.resizable(False,False)
#Agregamos un icono en la ventana
#raiz.iconbitmap("flash.ico")
#Asignamos tamaño de la ventana
raiz.geometry("525x400")
#Ponemos color la ventana background
raiz.config(bg="red")
#Declaramos string el cuadro texto
text_pantalla = StringVar()
operador = ""
#declaramos variable del operador
def clear():
    global operador
    operador=""
    text_pantalla.set("0")
def click(b):
    global operador
    operador += str(b)
    text_pantalla.set(operador)
def resultado():
    global operador
    try:
        r = str(eval(operador))
    except:
        r = "ERROR"
    text_pantalla.set(r)
#Agregamos un cuadro de texto
pantalla=Entry(raiz,width=31,font=("arial",20,"bold"),textvariable=text_pantalla)
#posicion del cuadro del text
pantalla.place(x=30,y=10)
#Agregamos los botones de numeros con su posicion
btn1=Button(raiz,text="1",width=10,height=2,command=lambda:click(1)).place(x=30,y=100)
btn2=Button(raiz,text="2",width=10,height=2,command=lambda:click(2)).place(x=160,y=100)
btn3=Button(raiz,text="3",width=10,height=2,command=lambda:click(3)).place(x=290,y=100)
btn4=Button(raiz,text="4",width=10,height=2,command=lambda:click(4)).place(x=30,y=180)
btn5=Button(raiz,text="5",width=10,height=2,command=lambda:click(5)).place(x=160,y=180)
btn6=Button(raiz,text="6",width=10,height=2,command=lambda:click(6)).place(x=290,y=180)
btn7=Button(raiz,text="7",width=10,height=2,command=lambda:click(7)).place(x=30,y=260)
btn8=Button(raiz,text="8",width=10,height=2,command=lambda:click(8)).place(x=160,y=260)
btn9=Button(raiz,text="9",width=10,height=2,command=lambda:click(9)).place(x=290,y=260)
btn0=Button(raiz,text="0",width=10,height=2,command=lambda:click(0)).place(x=30,y=340)
#Agregamos los botones de operadores con su posicion
btnigual=Button(raiz,text="=",width=29,height=2).place(x=160,y=340)
btnmas=Button(raiz,text="+",width=10,height=2).place(x=420,y=100)
btnmenos=Button(raiz,text="-",width=10,height=2).place(x=420,y=180)
btnx=Button(raiz,text="*",width=10,height=2).place(x=420,y=260)
btnentre=Button(raiz,text="/",width=10,height=2).place(x=420,y=340)
#miFrame=Frame()
#posicionamos el frame en la ventana
#miFrame.pack(side="bottom")
#Rellenamos horizonal el frame en la ventana
#miFrame.pack(fill="x")
#Rellenamos vertical el frame en la ventana
#miFrame.pack(fill="y", expand="True")
#Rellenamos completamente el frame en la ventana
#miFrame.pack(fill="x", expand="True")
#Poner relieve al frame
#miFrame.config(relief=groove)
#miFrame.config(bg="yellow")

#miFrame.config(width="400", height="450")

raiz.mainloop()