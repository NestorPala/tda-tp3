from datetime import datetime
import sys
import time
from ej003_backtracking import tribu_agua_backtracking
from ej004_programacion_lineal import tribu_agua_lp
from ej005_algoritmo_de_aproximacion import tribu_agua_aproximacion
from ej006_greedy import tribu_agua_greedy
from utils.tribu_agua import format_result, read_guerreros_file


SOLVERS = {
    "-back":     lambda guerreros, k: tribu_agua_backtracking(guerreros, k),
    "-lp":       lambda guerreros, k: tribu_agua_lp(guerreros, k, logs=False),
    "-aprox":    lambda guerreros, k: tribu_agua_aproximacion(guerreros, k),
    "-greedy":   lambda guerreros, k: tribu_agua_greedy(guerreros, k),
}


def read_file(path):
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


if __name__ == "__main__":
    method = sys.argv[1]
    solve(SOLVERS[method], "")
