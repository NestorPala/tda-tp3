import sys
import time


ARCHIVO_ESCRIBIR = "solucion_aproximada.txt"
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


def ordenar(nombre_y_habilidad):
    lista_ordenada = sorted(nombre_y_habilidad, key=lambda x: int(x[1]), reverse=True)
    return lista_ordenada


def aproximacion(cantidad_de_grupos, habilidad_ordenada):
    grupos = [[] for _ in range(cantidad_de_grupos)]
    sumas_cuadradas = [0] * cantidad_de_grupos

    for nombre, habilidad in habilidad_ordenada:
        grupo_minimo = min(range(cantidad_de_grupos), key = lambda i: sumas_cuadradas[i])

        grupos[grupo_minimo].append(nombre)

        sumas_cuadradas[grupo_minimo] += habilidad

    minimo = sum(j**2 for j in sumas_cuadradas)

    return grupos, minimo


def escribir_archivo(grupos, minimo):
    try:
        archivo = open(ARCHIVO_ESCRIBIR, "w")
    except:
        print("Error al abrir el archivo de solucion")
        return
    
    for i, grupo in enumerate(grupos, start=1):
        nombres = ', '.join(grupo)
        archivo.write(f"grupo {i}: {nombres}\n")

    archivo.write(f"coeficiente: {minimo}")

    archivo.close()


def main(ARCHIVO):
    cantidad_de_grupos, nombre_y_habilidad = leer_archivo(ARCHIVO)
    habilidad_ordenada = ordenar(nombre_y_habilidad)
    
    start_time = time.time()
    grupos, minimo = aproximacion(cantidad_de_grupos, habilidad_ordenada)
    end_time = time.time()

    total_time = end_time - start_time

    escribir_archivo(grupos, minimo)
    print("la solucion se encuentra en el archivo solucion_aproximada.txt")
    print(f"el tiempo que tarda el algortimo es {total_time}")


# para usar el algortimo se espera que los argumentos sean:
# python ej005_algoritmo_de_aproximacion.py (archivo del drive, ej: 6_3)
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
