import time
from utils.tribu_agua import obtener_ruta_archivo, read_guerreros_file, aproximacion, escribir_archivo


ARCHIVO_ESCRIBIR = "solucion_aproximada.txt"


def aproximacion_Maestro_Pakku(guerreros, k):
    # Ordenamos de mayor a menor los maestros en función de su habilidad o fortaleza
    habilidad_ordenada = sorted(guerreros, key=lambda x: int(x[1]), reverse=True)
    return aproximacion(k, habilidad_ordenada)


def tribu_agua_aproximacion(guerreros, k):
    start_time = time.time()
    grupos, minimo = aproximacion_Maestro_Pakku(guerreros, k)
    end_time = time.time()

    total_time = end_time - start_time

    escribir_archivo(grupos, minimo, ARCHIVO_ESCRIBIR)
    print("la solucion se encuentra en el archivo solucion_aproximada.txt")
    print(f"el tiempo que tarda el algortimo es {total_time}")


# para usar el algortimo se espera que los argumentos sean:
# python ej005_algoritmo_de_aproximacion.py (archivo del drive, ej: 6_3)
if __name__ == "__main__":
    filename = obtener_ruta_archivo()
    k, guerreros = read_guerreros_file(filename)
    tribu_agua_aproximacion(guerreros, k)
