import operator

def postfijo(operacion):
    operaciones = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
        }
    
    pila = []
    elementos = operacion.split()

    for elemento in elementos:
        if elemento.isdigit():
            pila.append(int(elemento))
        else:
            num2 = pila.pop()
            num1 = pila.pop()

            resultado= operaciones[elemento](num1, num2)
            pila.append(resultado)

    return pila.pop()

def prefija(operacion):
    operaciones = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
        }
    
    pila = []
    elementos = operacion.split()

    for elemento in reversed(elementos):
        if elemento.isdigit():
            pila.append(int(elemento))
        else:
            num1 = pila.pop()
            num2 = pila.pop()

            resultado= operaciones[elemento](num1, num2)
            pila.append(resultado)

    return pila.pop()

def tipo_notacion():
    while True:
        print("Calculadora de notaciones postfijo (notación polaca inversa) y prefijo (notación polaca)")
        print("\nOpciones:")
        print("1. Notación postfija")
        print("2. Notación prefija")
        print("3. Salir")

        opcion= input("Elija una opción: ")

        if opcion == '1':
            operacion = input("Ingrese la operación: ").strip()
            resultado = postfijo(operacion)
        elif opcion == '2':
            operacion = input("Ingrese la operación: ").strip()
            resultado = prefija(operacion)
        elif opcion == '3':
            break
        else:
            print("Algo salió mal, intente ingresando de nuevo.")
            return
        
        print(f"El resultado de la operación es de: {resultado}")

tipo_notacion()