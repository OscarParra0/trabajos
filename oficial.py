def suma_promedio():
    suma=0
    numeros = int(input("¿Cuántos números quieres introducir? "))
    for x in range(numeros):
        suma += int(input("Introduce un número: "))
    print("Se han introducido", numeros, "números que en total han sumado",suma, "y la media de estos números es", suma/numeros)

suma_promedio()