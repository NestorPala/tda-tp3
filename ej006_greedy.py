import sys
import time
from utils.tribu_agua import read_guerreros_file, aproximacion, escribir_archivo


ARCHIVO_ESCRIBIR = "solucion_aproximada_greedy.txt"


def aproximacion_greedy(cantidad_de_grupos, nombre_y_habilidad):
    return aproximacion(cantidad_de_grupos, nombre_y_habilidad)


def main(ARCHIVO):
    cantidad_de_grupos, nombre_y_habilidad = read_guerreros_file(ARCHIVO)
    
    start_time = time.time()
    grupos, minimo = aproximacion_greedy(cantidad_de_grupos, nombre_y_habilidad)
    end_time = time.time()

    total_time = end_time - start_time

    escribir_archivo(grupos, minimo, ARCHIVO_ESCRIBIR)
    print("la solucion se encuentra en el archivo solucion_aproximada.txt")
    print(f"el tiempo que tarda el algortimo es {total_time}")


# para usar el algortimo se espera que los argumentos sean:
# python ej006_greedy.py (archivo del drive, ej: 6_3)
if __name__ == "__main__":
    argumentos = sys.argv
    numero_parametros = len(argumentos)
    
    if numero_parametros < 2:
        print("faltan argumentos para utilizar el generador")
        sys.exit()
    elif numero_parametros > 2:
        print("se agregaron argumentos de mas, que van a ser ignorados")
    
    ARCHIVO = f"TP3/{argumentos[1]}.txt"
    main(ARCHIVO)
