import pulp
from utils.tribu_agua import obtener_ruta_archivo, read_guerreros_file


TP3 = "tribu_agua_problem"

GUERRERO_NAME = 0
GUERRERO_VALUE = 1

KEY_SEPARATOR = "_"
KEY_GROUP = 1
KEY_NAME = 2


def key(j, i):
    return f"a{KEY_SEPARATOR}{j}{KEY_SEPARATOR}{i}"


def get_boolean(value):
    if int(value) == 0:
        return False
    return True


def get_group_number(key):
    return int(key.split(KEY_SEPARATOR)[KEY_GROUP])


def get_name(key, guerreros_list):
    index = int(key.split(KEY_SEPARATOR)[KEY_NAME]) - 1
    return guerreros_list[index][GUERRERO_NAME]


def to_name_in_group(variable_item, guerreros_list):
    variable_name, variable = variable_item

    is_in_group = get_boolean(pulp.value(variable))

    if not is_in_group:
        return None
    
    return [
        get_group_number(variable_name),
        get_name(variable_name, guerreros_list)
    ]


def group_by_number(result: list[list[str, bool]]) -> dict[int, list[str]]:
    groups = {}
    for item in result:
        group_number_key = f"Grupo {item[0]}"
        guerrero_name = item[1]
        if group_number_key not in groups:
            groups[group_number_key] = []
        groups[group_number_key].append(guerrero_name)
    return groups


def calc_total_coefficient(result: dict[int, list[str]], guerreros) -> int:
    coef = 0
    group_sums = {}

    for group_number, guerreros_names in result.items():
        for name in guerreros_names:
            if group_number not in group_sums:
                group_sums[group_number] = 0
            power_value = guerreros[name]
            group_sums[group_number] += power_value

    for power_sum in group_sums.values():
        coef += power_sum ** 2

    return coef


def tribu_agua_lp_(guerreros_list, k, logs=False):
    problem = pulp.LpProblem(TP3, pulp.LpMinimize)

    # coefficients
    constants = list(map(lambda guerrero: guerrero[GUERRERO_VALUE], guerreros_list))

    # binary variables to solve
    n = len(guerreros_list)

    boolean_variables = {}
    for j in range(1, k+1):
        for i in range(1, n+1):
            # "j" is for subsets
            # "i" is for guerreros
            name = key(j, i)
            boolean_variables[name] = pulp.LpVariable(name, cat=pulp.LpBinary)

    # restrictions
    subsets = []
    for j in range(1, k+1):
        sj = pulp.LpAffineExpression([(boolean_variables[key(j, i+1)], constants[i]) for i in range(len(constants))]) 
        subsets.append(sj)
    
    for sj in subsets:
        problem += sj
    
    for j in range(2, k + 1):
        s1 = subsets[0]
        sj = subsets[j - 1]
        problem += s1 >= sj
    
    for j in range(1, k):
        sk = subsets[len(subsets) - 1]
        sj = subsets[j - 1]
        problem += sk <= sj

    for i in range(1, n+1):
        all_booleans_for_an_specific_element = [ boolean_variables[key(j, i)] for j in range(1, k+1) ]
        problem += pulp.lpSum(all_booleans_for_an_specific_element) == 1

    # objective function
    s1 = subsets[0]
    sk = subsets[len(subsets) - 1]
    problem += s1 - sk

    print("Solving integer lineal programming problem...")

    if logs:
        problem.solve()
    else:
        problem.solve(pulp.PULP_CBC_CMD(msg=0))
    
    # DEBUG
    # print("------------------------- DEBUG ------------------------- ")
    # solved_variables = list(map(lambda variable: [get_name(variable[0], lista_guerreros), variable[0], pulp.value(variable[1])], variables.items()))
    # for v in solved_variables:
    #     print(v)
    # print("--------------------------------------------------------- ")

    return problem, boolean_variables


def tribu_agua_lp(guerreros, k, logs=False):
    guerreros_list = [ [key, value] for key,value in guerreros.items() ]

    problem, solved_variables = tribu_agua_lp_(guerreros_list, k, logs)

    # DEBUG
    # print("------------------------- DEBUG ------------------------- ")
    # print(problem)
    # print("--------------------------------------------------------- ")

    result = list(map(lambda variable: to_name_in_group(variable, guerreros_list), solved_variables.items()))
    result = list(filter(lambda item: item is not None, result))
    result = group_by_number(result)

    for key, value in result.items():
        result[key] = sorted(value, key=lambda name: guerreros[name], reverse=True)

    coefficient = calc_total_coefficient(result, guerreros)

    return result, coefficient


# para usar el algortimo se espera que los argumentos sean:
# python ej004_programacion_lineal.py (archivo del drive, ej: 6_3)
if __name__ == "__main__":
    filename = obtener_ruta_archivo()
    k, guerreros_ = read_guerreros_file(filename)

    guerreros = {}
    for tuple_ in guerreros_:
        key_ = tuple_[0]
        value = tuple_[1]
        guerreros[key_] = value

    tribu_agua_lp(guerreros, k)
