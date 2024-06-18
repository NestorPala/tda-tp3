import sys
import time
ARCHIVO_ESCRIBIR = "solucion.txt"
SEPARADOR = ","

def leer_archivo(ARCHIVO):
    try:
        with open(ARCHIVO, "r") as grupos:
            lineas = [linea for linea in grupos if not linea.startswith("#")]
    except:
        print("Error al abrir el archivo de los grupos")
        return None, None
    
    cantidad_de_grupos = int(lineas[0].strip())
    
    nombre_y_habilidad = []
    for linea in lineas[1:]:
        nombre, fuerza = linea.strip().split(SEPARADOR)
        nombre_y_habilidad.append((nombre, int(fuerza)))
    
    return cantidad_de_grupos, nombre_y_habilidad

#n = numero de maestros, k = numero de grupos, x= lista de fuerzas de los maestros
#grupo = lista de sumas de fuerzas de los grupos, pos = posicion actual en la lista de maestros
#minimo = minimo encontrado hasta ahora
def backtracking(n, k, x, grupo, asignacion, pos, minimo):
    #si se asignaorn todos los maestros a un grupo, calcula la suma de los cuadrados de las sumas de las fuerzas de los grupos
    if pos == n:
        suma = sum(i**2 for i in grupo)
        if suma < minimo[0]:
            minimo[0] = suma
            minimo[1] = asignacion[:]
    else:
        #bucle que recorre grupos
        for i in range(k):
            #asigna al maestro actual al grupo
            grupo[i] += x[pos]
            asignacion[pos] = i
            #verifica si la suma es manor al minimo actual, si es asi sigue con el sig maestro
            if sum(j**2 for j in grupo) < minimo[0]:
                #llama la siguiente posicion
                backtracking(n, k, x, grupo, asignacion, pos + 1, minimo)
            #deshace la asignacion del maestro
            grupo[i] -= x[pos]


def resolver(cantidad_de_grupos, nombre_y_habilidad):
    #numero total de maestros
    n = len(nombre_y_habilidad)
    #crea lista con las fuerzas de los maestros
    x = [habilidad for _, habilidad in nombre_y_habilidad]
    grupo = [0]*cantidad_de_grupos
    asignacion = [0]*n
    minimo = [float('inf'), []]
    backtracking(n, cantidad_de_grupos, x, grupo, asignacion, 0, minimo)
    return minimo[0], minimo[1]


def escribir_archivo(minimo, asignacion, nombre_y_habilidad):
    try:
        solucion = open(ARCHIVO_ESCRIBIR, "w")
    except:
        print("error al abrir el archivo")
        return
    
    grupos = [[] for _ in range(max(asignacion) + 1)]
    for (nombre, _), grupo in zip(nombre_y_habilidad, asignacion):
        grupos[grupo].append(nombre)
    
    for i, grupo in enumerate(grupos, 1):
        solucion.write(f'Grupo {i}: {", ".join(grupo)}\n')

    solucion.write(f'Coeficiente: {minimo}')

    solucion.close()


def main(ARCHIVO):

    cantidad_de_grupos, nombre_y_habilidad = leer_archivo(ARCHIVO)

    start_time = time.time()
    minimo, asignacion = resolver(cantidad_de_grupos, nombre_y_habilidad)
    end_time = time.time()

    tiempo_total = end_time - start_time

    escribir_archivo(minimo, asignacion, nombre_y_habilidad)
    print("la solucion se encuentra en el archivo solucion.txt")
    print(f"la funcion de backtraking tardo {tiempo_total} segundos.")



#para usar el algortimo se espera que los argumentos sean:
#python 003_backtracking.py (archivo del drive, ej: 6_3)
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