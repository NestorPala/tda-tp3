import sys
import random
import backtraking

INDICE_NOMBRES = 1
INDICE_GRUPOS = 2
INDICE_GENERADOR = 4
INDICE_ALGORITMO = 3
ARCHIVO = "generador.txt"
ARCHIVO_NOMBRES = "nombres.txt"

def generador(cantidad_de_nombres, cantidad_de_grupos):
    try:
        generador = open(ARCHIVO, "w")
    except:
        print("Error al abrir el archivo generador")
        return
    
    try:
        archivo_nombres = open(ARCHIVO_NOMBRES, "r")
    except:
        print("Error al abrir archivo de nombres")
        return
    
    nombres = archivo_nombres.read().splitlines()

    generador.write(f"{cantidad_de_grupos}\n")

    vueltas = 0
    for i in range(cantidad_de_nombres):
        indice = i % len(nombres)
        if indice == 0 and i != 0:
            vueltas += 1
        nombre = nombres[indice]
        numero = random.randint(0, 999)
        if i != cantidad_de_nombres -1:
            generador.write(f"{nombre} {vueltas}, {numero}\n")
        else:
            generador.write(f"{nombre} {vueltas}, {numero}")

    generador.close()
    archivo_nombres.close()

def main():
    argumentos = sys.argv
    numero_parametros = len(argumentos)
    
    if numero_parametros < INDICE_GENERADOR:
        print("faltan argumentos para utilizar el generador")
        return
    elif numero_parametros > INDICE_GENERADOR:
        print("se agregaron argumentos de mas, que van a ser ignorados")

    try:
        cantidad_de_nombres = int(argumentos[INDICE_NOMBRES])
        cantidad_de_grupos = int(argumentos[INDICE_GRUPOS])
    except (IndexError, ValueError):
        print("Error: los argumentos deben ser números enteros.")
        return

    generador(cantidad_de_nombres, cantidad_de_grupos)

    if argumentos[INDICE_ALGORITMO] == "backtraking":
        backtraking.main(ARCHIVO)




if __name__ == "__main__":
    main()