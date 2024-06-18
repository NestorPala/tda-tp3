import time
from utils.tribu_agua import obtener_ruta_archivo, read_guerreros_file, aproximacion, escribir_archivo


ARCHIVO_ESCRIBIR = "solucion_aproximada_greedy.txt"


def tribu_agua_greedy(guerreros, k):
    start_time = time.time()

    # En este caso no ordenamos los guerreros por nivel de habilidad
    grupos, minimo = aproximacion(k, guerreros)

    end_time = time.time()
    total_time = end_time - start_time

    escribir_archivo(grupos, minimo, ARCHIVO_ESCRIBIR)
    
    print("la solucion se encuentra en el archivo solucion_aproximada.txt")
    print(f"el tiempo que tarda el algortimo es {total_time}")


# para usar el algortimo se espera que los argumentos sean:
# python ej006_greedy.py (archivo del drive, ej: 6_3)
if __name__ == "__main__":
    filename = obtener_ruta_archivo()
    k, guerreros = read_guerreros_file(filename)
    tribu_agua_greedy(guerreros, k)
    