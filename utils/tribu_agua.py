import sys


SEPARATOR = ","


def read_guerreros_file(filename, separator=SEPARATOR):
    try:
        with open(filename, "r") as groups:
            lines = [line for line in groups if not line.startswith("#")]
    except:
        print("Error opening groups file!")
        return None, None
    
    group_count = int(lines[0].strip())
    
    guerreros = []
    for line in lines[1:]:
        name, power = line.strip().split(separator)
        guerreros.append((name, int(power)))
    
    return group_count, guerreros


def aproximacion(cantidad_de_grupos, habilidad_ordenada):
    grupos = [[] for _ in range(cantidad_de_grupos)]
    sumas_cuadradas = [0] * cantidad_de_grupos

    for nombre, habilidad in habilidad_ordenada:
        grupo_minimo = min(range(cantidad_de_grupos), key = lambda i: sumas_cuadradas[i])

        grupos[grupo_minimo].append(nombre)

        sumas_cuadradas[grupo_minimo] += habilidad

    minimo = sum(j**2 for j in sumas_cuadradas)

    return grupos, minimo


def escribir_archivo(grupos, minimo, archivo_escribir):
    try:
        archivo = open(archivo_escribir, "w")
    except:
        print("Error al abrir el archivo de solucion")
        return
    
    for i, grupo in enumerate(grupos, start=1):
        nombres = ', '.join(grupo)
        archivo.write(f"grupo {i}: {nombres}\n")

    archivo.write(f"coeficiente: {minimo}")

    archivo.close()


def obtener_ruta_archivo():
    argumentos = sys.argv
    numero_parametros = len(argumentos)
    
    if numero_parametros < 2:
        print("faltan argumentos para utilizar el generador")
        sys.exit()
    elif numero_parametros > 2:
        print("se agregaron argumentos de mas, que van a ser ignorados")
    
    return f"TP3/{argumentos[1]}.txt"


def get_sorted_guerreros(res: dict[str, list[str]], guerreros: list[str, int]):
    guerreros_ = {}
    for tuple_ in guerreros:
        key_ = tuple_[0]
        value = tuple_[1]
        guerreros_[key_] = value

    for key, value in res.items():
        res[key] = sorted(value, key=lambda name: guerreros_[name], reverse=True)

    return res
