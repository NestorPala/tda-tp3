import time
from utils.tribu_agua import get_sorted_guerreros, obtener_ruta_archivo, read_guerreros_file, aproximacion, escribir_archivo


ARCHIVO_ESCRIBIR = "solucion_aproximada.txt"


def aproximacion_Maestro_Pakku(guerreros, k):
    # Ordenamos de mayor a menor los maestros en función de su habilidad o fortaleza
    habilidad_ordenada = sorted(guerreros, key=lambda x: int(x[1]), reverse=True)
    return aproximacion(k, habilidad_ordenada)


def tribu_agua_aproximacion(guerreros, k):
    start_time = time.time()
    grupos, coeficiente = aproximacion_Maestro_Pakku(guerreros, k)
    end_time = time.time()

    total_time = end_time - start_time

    escribir_archivo(grupos, coeficiente, ARCHIVO_ESCRIBIR)
    print("la solucion se encuentra en el archivo solucion_aproximada.txt")
    print(f"el tiempo que tarda el algortimo es {total_time}")

    res = {}
    i = 0
    for grupo in grupos:
        i+=1
        key = f"Grupo {i}"
        res[key] = []
        for e in grupo:
            res[key].append(e)
    
    res = get_sorted_guerreros(res, guerreros)

    return res, coeficiente


# para usar el algortimo se espera que los argumentos sean:
# python ej005_algoritmo_de_aproximacion.py (archivo del drive, ej: 6_3)
if __name__ == "__main__":
    filename = obtener_ruta_archivo()
    k, guerreros = read_guerreros_file(filename)
    tribu_agua_aproximacion(guerreros, k)
