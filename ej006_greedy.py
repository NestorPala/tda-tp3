import time
from utils.tribu_agua import obtener_ruta_archivo, read_guerreros_file, aproximacion, escribir_archivo


ARCHIVO_ESCRIBIR = "solucion_aproximada_greedy.txt"


def aproximacion_greedy(cantidad_de_grupos, nombre_y_habilidad):
    return aproximacion(cantidad_de_grupos, nombre_y_habilidad)


def tribu_agua_greedy(filename):
    cantidad_de_grupos, nombre_y_habilidad = read_guerreros_file(filename)
    
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
    archivo = obtener_ruta_archivo()
    tribu_agua_greedy(archivo)
    