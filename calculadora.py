#(1)suma (+)
#(2)resta (-)
#(3)mutiplicacion (*)
#(4)division (/)
#(5)modulo (%)  
#(6)exponente (**) 

# MODULOS DE OPERACIONES / FUNCIONES.
from operaciones.suma import suma
from operaciones.resta import resta
from operaciones.multiplicacion import multiplicacion
from operaciones.division import division
from operaciones.modulo import modulo
from operaciones.exponente import exponente




def operaciones(numero1, numero2, opcion):
    print("calculadora de ingenieria".center(50,'-') )
    if opcion == 1:
        print(f"El resultado es:{suma(numero1, numero2)} ")
    elif opcion == 2:
        print(f"El resultado es: {resta(numero1, numero2)} ")
    elif opcion == 3:
        print(f"El resultado es: {multiplicacion(numero1, numero2)}")    
    elif opcion == 4:
        print(f"El resultado es: {division(numero1, numero2)} ")
    elif opcion == 5:
        print(f"El resultado es : {modulo(numero1, numero2)}")
    elif opcion == 6:
        print(f"El resultado es :{exponente(numero1, numero2)}")
    else:
        print("---error, intente una vez mas--- ")

try:

    var1 = float(input("ingrese su primer numero : "))
    var2 = float(input("ingrese su segundo numero : "))
    var3 = int(input(
        "Ingrese opción:\n"
        "(1) Sumar\n"
        "(2) Restar\n"
        "(3) Multiplicar\n"
        "(4) Dividir\n"
        "(5) Módulo\n"
        "(6) Potencia\n"
        "Ingrese solo el número de la opción: "
    ))
    operaciones(var1, var2, var3)

except ValueError:
    print(" se ah equivocado asegurese de ingresar la opcion correcta")



