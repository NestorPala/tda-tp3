import time
from utils.tribu_agua import get_sorted_guerreros, obtener_ruta_archivo, read_guerreros_file


ARCHIVO_ESCRIBIR = "solucion.txt"


# n = numero de maestros, k = numero de grupos, x= lista de fuerzas de los maestros
# grupo = lista de sumas de fuerzas de los grupos, pos = posicion actual en la lista de maestros
# minimo = minimo encontrado hasta ahora
def backtracking_(n, k, x, grupo, asignacion, pos, minimo):
    # si se asignaorn todos los maestros a un grupo, calcula la suma de los cuadrados de las sumas de las fuerzas de los grupos
    if pos == n:
        suma = sum(i**2 for i in grupo)
        if suma < minimo[0]:
            minimo[0] = suma
            minimo[1] = asignacion[:]
    else:
        # bucle que recorre grupos
        for i in range(k):
            # asigna al maestro actual al grupo
            grupo[i] += x[pos]
            asignacion[pos] = i
            # verifica si la suma es manor al minimo actual, si es asi sigue con el sig maestro
            if sum(j**2 for j in grupo) < minimo[0]:
                # llama la siguiente posicion
                backtracking_(n, k, x, grupo, asignacion, pos + 1, minimo)
            # deshace la asignacion del maestro
            grupo[i] -= x[pos]


def backtracking(cantidad_de_grupos, nombre_y_habilidad):
    # numero total de maestros
    n = len(nombre_y_habilidad)
    # crea lista con las fuerzas de los maestros
    x = [habilidad for _, habilidad in nombre_y_habilidad]
    grupo = [0]*cantidad_de_grupos
    asignacion = [0]*n
    minimo = [float('inf'), []]
    backtracking_(n, cantidad_de_grupos, x, grupo, asignacion, 0, minimo)
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
