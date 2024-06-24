from datetime import datetime
import os
import sys
import time
from ej003_backtracking import tribu_agua_backtracking
from ej004_programacion_lineal import tribu_agua_lp
from ej005_algoritmo_de_aproximacion import tribu_agua_aproximacion
from ej006_greedy import tribu_agua_greedy
from utils.tribu_agua import format_result


ARG_COUNT = 4

FILE_OPTION = "-file"
ABS_OPTION = "-abs"

USO = f"""
    Uso del programa:

    El archivo tiene que estar en la misma carpeta que tp3.py:

        python file.py {FILE_OPTION} ARCHIVO_GUERREROS.txt SOLVER

    El archivo puede estar en cualquier ruta:

        python file.py {ABS_OPTION} PATH_TO_/ARCHIVO_GUERREROS.txt SOLVER

    SOLVER : "-back", "-lp", "-aprox" o "-greedy"
"""

SOLVERS = {
    "-back":     lambda guerreros, k: tribu_agua_backtracking(guerreros, k),
    "-lp":       lambda guerreros, k: tribu_agua_lp(guerreros, k, logs=False),
    "-aprox":    lambda guerreros, k: tribu_agua_aproximacion(guerreros, k),
    "-greedy":   lambda guerreros, k: tribu_agua_greedy(guerreros, k),
}


def read_file(path):
    pass


def write_file(path):
    pass


def solve(f, path):
    name, k, guerreros = read_file(path)

    print(f"\nProcessing test for file: {name}")

    start_time = time.time()
    current_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
    print("Test start: ", current_date)

    # CALLING SPECIFIED SOLVER
    result, coefficient = f(guerreros, k)

    end_time = time.time()
    current_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
    print("Test end: ", current_date)
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")

    formatted_result_1 = format_result(name, result, coefficient)
    print(formatted_result_1)

    print(f"File {name} processed!\n")

    return result, coefficient


def main():
    if len(sys.argv) != ARG_COUNT:
        print(USO)
        return
    
    arg_filemode = sys.argv[1]
    arg_path     = sys.argv[2]
    arg_solver   = sys.argv[3]
    
    if (arg_filemode == FILE_OPTION):
        path = arg_path
    elif(arg_filemode == ABS_OPTION):
        path = os.path.normpath(arg_path)
    else:
        print(USO)
        return
    
    result, coefficient = solve(SOLVERS[arg_solver], path)

    write_file(path, result, coefficient)

    filename = os.path.basename(path)
    print("\nArchivo procesado con éxito!")
    print(f"Los resultados se encuentran en el archivo solved_{filename}")


if __name__ == "__main__":
    main()
