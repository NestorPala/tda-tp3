import time
from utils.tribu_agua import get_sorted_guerreros, obtener_ruta_archivo, read_guerreros_file, aproximacion, escribir_archivo


ARCHIVO_ESCRIBIR = "solucion_aproximada_greedy.txt"


def tribu_agua_greedy(guerreros, k):
    start_time = time.time()

    # En este caso no ordenamos los guerreros por nivel de habilidad
    grupos, coeficiente = aproximacion(k, guerreros)

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
# python ej006_greedy.py (archivo del drive, ej: 6_3)
if __name__ == "__main__":
    filename = obtener_ruta_archivo()
    k, guerreros = read_guerreros_file(filename)
    tribu_agua_greedy(guerreros, k)
    