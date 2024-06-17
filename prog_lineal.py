import pulp


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


def get_name(key, lista_guerreros):
    index = int(key.split(KEY_SEPARATOR)[KEY_NAME]) - 1
    return lista_guerreros[index][GUERRERO_NAME]


def to_name_in_group(variable_item, pulp, lista_guerreros):
    variable_name, variable = variable_item

    is_in_group = get_boolean(pulp.value(variable))

    if not is_in_group:
        return None
    
    return [
        get_group_number(variable_name),
        get_name(variable_name, lista_guerreros)
    ]


def tribu_agua_ple(lista_guerreros, k):
    problem = pulp.LpProblem("tribu_agua", pulp.LpMinimize)

    # coefficients
    constants = list(map(lambda guerrero: guerrero[GUERRERO_VALUE], lista_guerreros))

    # binary variables to solve
    n = len(lista_guerreros)

    variables = {}
    for j in range(1, k+1):
        for i in range(1, n+1):
            name = key(j, i)
            variables[name] = pulp.LpVariable(name, cat=pulp.LpBinary)

    # restrictions
    subsets = []
    for j in range(1, k+1):
        sj = pulp.LpAffineExpression([(variables[key(j, i+1)], constants[i]) for i in range(len(constants))]) 
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
        all_coefficients_for_an_specific_element = [ variables[key(j, i)] for j in range(1, k+1) ]
        problem += pulp.lpSum(all_coefficients_for_an_specific_element) == 1

    # objective function
    s1 = subsets[0]
    sk = subsets[len(subsets) - 1]
    problem += s1 - sk

    print("Solving integer lineal programming problem...")

    problem.solve()
    
    # DEBUG
    # print("------------------------- DEBUG ------------------------- ")
    # solved_variables = list(map(lambda variable: [get_name(variable[0], lista_guerreros), variable[0], pulp.value(variable[1])], variables.items()))
    # for v in solved_variables:
    #     print(v)
    # print("--------------------------------------------------------- ")

    return problem, variables


def main():
    lista_guerreros = [
        ("Pakku", 101),
        ("Yue", 134),
        ("Yakone", 759),
        ("Pakku I", 308),
        ("Wei", 644)
    ]

    k = 2

    problem, variables = tribu_agua_ple(lista_guerreros, k)

    # DEBUG
    # print("------------------------- DEBUG ------------------------- ")
    # print(problem)
    # print("--------------------------------------------------------- ")

    result = list(map(lambda variable: to_name_in_group(variable, pulp, lista_guerreros), variables.items()))
    result = list(filter(lambda item: item is not None, result))

    print("Solution: \n")
    for variable in result:
        print(variable)


main()
