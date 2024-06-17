import pulp


def key(j, i):
    return f"a{j}{i}"


def tribu_agua_ple(lista_guerreros, k):
    problem = pulp.LpProblem("tribu_agua", pulp.LpMinimize)

    # coefficients
    constants = list(map(lambda guerrero: guerrero[1], lista_guerreros))

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
    result = list(map(lambda variable: [variable, pulp.value(variable)], variables.values()))

    return problem, result


def main():
    lista_guerreros = [
        ("Pakku", 101),
        ("Yue", 134),
        ("Yakone", 759),
        ("Pakku I", 308),
        ("Wei", 644)
    ]

    k = 2

    problem, result = tribu_agua_ple(lista_guerreros, k)

    # debug
    print(
        50 * "--" + "\nPROBLEM: \n", 
        problem, 
        "\n" + 50 * "--"
    )

    print("Solution: \n")
    for variable in result:
        print(variable)


main()
