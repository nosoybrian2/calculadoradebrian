# -*- coding: utf-8 -*-

def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Error: División por cero"
    return x / y

def calculadora():
    print("Selecciona la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    while True:
        seleccion = input("Ingresa el número de la operación (1/2/3/4): ")

        if seleccion in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            if seleccion == '1':
                print(f"{num1} + {num2} = {sumar(num1, num2)}")
            elif seleccion == '2':
                print(f"{num1} - {num2} = {restar(num1, num2)}")
            elif seleccion == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif seleccion == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")
        else:
            print("Selección no válida. Por favor intenta de nuevo.")

        otra_vez = input("¿Quieres hacer otra operación? (si/no): ")
        if otra_vez.lower() != 'si':
            break

if __name__ == "__main__":
    calculadora()
