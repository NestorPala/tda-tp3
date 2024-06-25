import time
from utils.tribu_agua import get_sorted_guerreros, obtener_ruta_archivo, read_guerreros_file


ARCHIVO_ESCRIBIR = "solucion.txt"


def backtracking_(n, k, x, grupo, asignacion, pos, minimo, current_sum_sq, grupos_ordenados):
    if pos == n:
        if current_sum_sq < minimo[0]:
            minimo[0] = current_sum_sq
            minimo[1] = asignacion[:]
    else:
        for i in grupos_ordenados:
            grupo[i] += x[pos]
            new_sum_sq = current_sum_sq + 2 * x[pos] * grupo[i] - x[pos]**2
            asignacion[pos] = i

            if new_sum_sq < minimo[0]:
                backtracking_(n, k, x, grupo, asignacion, pos + 1, minimo, new_sum_sq, grupos_ordenados)

            grupo[i] -= x[pos]

def backtracking(cantidad_de_grupos, nombre_y_habilidad):
    n = len(nombre_y_habilidad)
    x = [habilidad for _, habilidad in nombre_y_habilidad]
    x.sort(reverse=True)
    grupo = [0] * cantidad_de_grupos
    asignacion = [0] * n
    minimo = [float('inf'), []]
    grupos_ordenados = sorted(range(cantidad_de_grupos), key=lambda i: grupo[i])
    backtracking_(n, cantidad_de_grupos, x, grupo, asignacion, 0, minimo, 0, grupos_ordenados)
    return minimo[0], minimo[1]


def escribir_archivo(coeficiente, asignacion, nombre_y_habilidad):
    res = {}

    try:
        solucion = open(ARCHIVO_ESCRIBIR, "w")
    except:
        print("error al abrir el archivo")
        return
    
    grupos = [[] for _ in range(max(asignacion) + 1)]
    for (nombre, _), grupo in zip(nombre_y_habilidad, asignacion):
        grupos[grupo].append(nombre)
    
    for i, grupo in enumerate(grupos, 1):
        key_ = f'Grupo {i}'
        solucion.write(f'{key_}: {", ".join(grupo)}\n')
        res[key_] = grupo

    solucion.write(f'Coeficiente: {coeficiente}')
    solucion.close()

    return res


def tribu_agua_backtracking(guerreros, k):
    start_time = time.time()
    coeficiente, asignacion = backtracking(k, guerreros)
    end_time = time.time()

    tiempo_total = end_time - start_time

    res = escribir_archivo(coeficiente, asignacion, guerreros)
    print("la solucion se encuentra en el archivo solucion.txt")
    print(f"la funcion de backtraking tardo {tiempo_total} segundos.")

    res = get_sorted_guerreros(res, guerreros)

    return res, coeficiente


# para usar el algortimo se espera que los argumentos sean:
# python ej003_backtracking.py (archivo del drive, ej: 6_3)
if __name__ == "__main__":
    filename = obtener_ruta_archivo()
    k, guerreros = read_guerreros_file(filename)
    tribu_agua_backtracking(guerreros, k)
