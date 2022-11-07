from tkinter import Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("295x260")

# Configuración pantalla de salida 
pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

# Eventos
def AgregarNum(num):
    if operacion1:
        global num1
        if num1=="0":
            num1=num
        else:
            num1=num1+num
        pantalla.delete(0,100)
        pantalla.insert(0,num1)
    else:
        global num2
        if num2=="0":
            num2=num
        else:
            num2=num2+num
        pantalla.delete(0,100)
        pantalla.insert(0,num2)
        
def Operacion(operacion):
    global operacion1
    operacion1=False
    global procedimiento
    procedimiento=operacion
    pantalla.delete(0,100)
    pantalla.insert(0,operacion)

def Resultado():
    pantalla.delete(0,100)
    if procedimiento=="+":
        resultado=float(num1)+float(num2)
        pantalla.insert(0,resultado)
    elif procedimiento=="-":
        resultado=float(num1)-float(num2)
        pantalla.insert(0,resultado)
    elif procedimiento=="*":
        resultado=float(num1)*float(num2)
        pantalla.insert(0,resultado)
    else:
        resultado=float(num1)/float(num2)
        pantalla.insert(0,resultado)

num1="0"
num2="0"
procedimiento="a"
operacion1=True

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: AgregarNum("1")).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: AgregarNum("2")).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: AgregarNum("3")).grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: AgregarNum("4")).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: AgregarNum("5")).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: AgregarNum("6")).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: AgregarNum("7")).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: AgregarNum("8")).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: AgregarNum("9")).grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command = Resultado).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command=lambda: AgregarNum(".")).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: Operacion("+")).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: Operacion("-")).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: Operacion("*")).grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: Operacion("/")).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()