import time, sys
from prog_lineal import tribu_agua_prog_lineal
from datetime import datetime


SEPARADOR = ","

NOMBRES = [
    '5_2.txt', 
    '6_3.txt', 
    '6_4.txt', 
    '8_3.txt',
    '10_3.txt',
    '10_5.txt', # NOT PASS
    # '10_10.txt',
    '11_5.txt', 
    '14_3.txt', 
    '14_4.txt', 
    # '14_6.txt',
    '15_4.txt', 
    # '15_6.txt',
    # '17_5.txt',
    # '17_7.txt', 
    # '17_10.txt', 
    # '18_6.txt', 
    # '18_8.txt', 
    # '20_4.txt', 
    # '20_5.txt', 
    # '20_8.txt'
]

RESULTS = {
    '10_10.txt': """
        10_10.txt
        Grupo 1: Unalaq
        Grupo 2: Sura
        Grupo 3: Senna
        Grupo 4: Ming-Hua
        Grupo 5: Rafa
        Grupo 6: Tho
        Grupo 7: Desna
        Grupo 8: Katara
        Grupo 9: Kya
        Grupo 10: Amon
        Coeficiente: 172295
    """,
    '10_3.txt': """
        10_3.txt
        Grupo 1: Sangok, Yue, Pakku
        Grupo 2: Eska, Wei, Amon
        Grupo 3: Sura, Siku, La, Tonraq
        Coeficiente: 385249
    """, 
    '10_5.txt': """
        10_5.txt
        Grupo 1: Katara, Hasook
        Grupo 2: Misu, Eska
        Grupo 3: Siku I, Desna
        Grupo 4: Siku, Sura
        Grupo 5: Desna I, Unalaq
        Coeficiente: 355882
    """, 
    '11_5.txt': """
        11_5.txt
        Grupo 1: Yakone
        Grupo 2: Siku I
        Grupo 3: Tonraq, Siku
        Grupo 4: Misu, Hasook, Siku II, Hama
        Grupo 5: Misu I, Kya, Pakku
        Coeficiente: 2906564
    """, 
    '14_3.txt': """
        14_3.txt
        Grupo 1: Huu, Kuruk, Tonraq, Eska I, Hama
        Grupo 2: Sangok, Rafa, Tonraq I, Eska II
        Grupo 3: Sangok I, Misu, Katara, Wei, Eska
        Coeficiente: 15659106
    """, 
    '14_4.txt': """
        14_4.txt
        Grupo 1: Pakku I, Misu, Hasook
        Grupo 2: Tonraq, Huu I, Tho
        Grupo 3: La, Ming-Hua, Huu II
        Grupo 4: Kya I, Huu, Pakku, Kya, Yue
        Coeficiente: 15292055
    """, 
    '14_6.txt': """
        14_6.txt
        Grupo 1: Ming-Hua, Wei
        Grupo 2: Siku, Desna
        Grupo 3: Unalaq, Misu
        Grupo 4: Amon, Senna
        Grupo 5: Misu I, Ming-Hua I
        Grupo 6: Kuruk I, Kuruk, La, Kya
        Coeficiente: 10694510
    """, 
    '15_4.txt': """
        15_4.txt
        Grupo 1: Katara, Tonraq I, Yue, Kuruk I
        Grupo 2: Kuruk, Wei, Desna, Tho
        Grupo 3: Hasook, Yakone, Pakku, Kya
        Grupo 4: Senna, Tonraq, Hama
        Coeficiente: 4311889
    """, 
    '15_6.txt': """
        15_6.txt
        Grupo 1: Senna II, Huu I
        Grupo 2: Amon, Hasook, Senna I
        Grupo 3: Hasook I, Rafa
        Grupo 4: Pakku, Senna
        Grupo 5: La, Ming-Hua, Sura
        Grupo 6: Huu, Tonraq, Wei
        Coeficiente: 6377225
    """, 
    '17_10.txt': """
        17_10.txt
        Grupo 1: Yue
        Grupo 2: Rafa
        Grupo 3: Pakku I
        Grupo 4: Siku
        Grupo 5: Wei I, Eska
        Grupo 6: Misu, Pakku
        Grupo 7: Sangok, Siku I
        Grupo 8: Wei, Tho
        Grupo 9: Amon, Yue I, Sura
        Grupo 10: Hama, Desna
        Coeficiente: 5427764
    """, 
    '17_5.txt': """
        17_5.txt
        Grupo 1: Sangok I, Misu I, Rafa
        Grupo 2: Yakone I, Yakone, Tho
        Grupo 3: Sangok, Huu, Ming-Hua, Misu
        Grupo 4: Senna I, Amon I, Senna
        Grupo 5: Wei, Unalaq, Amon, Hama
        Coeficiente: 15974095
    """, 
    '17_7.txt': """
        17_7.txt
        Grupo 1: Pakku II, Hasook I, Pakku
        Grupo 2: Rafa, Eska, Hasook
        Grupo 3: Hama, Wei I, Desna
        Grupo 4: Wei, La
        Grupo 5: Unalaq, Tonraq
        Grupo 6: Pakku I, Yue
        Grupo 7: Siku, Sangok
        Coeficiente: 11513230
    """, 
    '18_6.txt': """
        18_6.txt
        Grupo 1: Misu I, Kya
        Grupo 2: Yue II, Kuruk, Huu
        Grupo 3: Yue I, Yakone
        Grupo 4: Tho, Hama I, Sangok
        Grupo 5: Senna, Amon, Pakku, Misu
        Grupo 6: Hama, Kuruk I, Kya I, Yue
        Coeficiente: 10322822
    """, 
    '18_8.txt': """
        18_8.txt
        Grupo 1: Amon II, Senna
        Grupo 2: Sura, Hama
        Grupo 3: Kya I, Amon I
        Grupo 4: Siku, Tho I
        Grupo 5: Yakone, Amon
        Grupo 6: Rafa I, Desna, Katara
        Grupo 7: Rafa, Wei, Ming-Hua
        Grupo 8: Tho, Kya
        Coeficiente: 11971097
    """, 
    '20_4.txt': """
        20_4.txt
        Grupo 1: Sura I, Tonraq, Yue, Siku
        Grupo 2: Siku I, Wei, Rafa, Wei I
        Grupo 3: Sangok, Tonraq I, Sura, Hama, Katara, Sangok II
        Grupo 4: Tho, Ming-Hua, Tho I, Kya, Sangok I, Hasook
        Coeficiente: 21081875
    """, 
    '20_5.txt': """
        20_5.txt
        Grupo 1: Huu, Kuruk, Ming-Hua
        Grupo 2: Desna, Sura, Tonraq, Misu II
        Grupo 3: Yakone, Misu, Huu II, Yue, Huu III
        Grupo 4: Huu I, Siku, Wei
        Grupo 5: Hasook I, Hasook, Tonraq I, Yue I, Misu I
        Coeficiente: 16828799
    """, 
    '20_8.txt': """
        20_8.txt
        Grupo 1: Wei, Sangok, Hama I
        Grupo 2: Kuruk, Katara, Sura I
        Grupo 3: Unalaq, Amon I
        Grupo 4: Yakone, Ming-Hua, Sura
        Grupo 5: Tonraq, Pakku, La
        Grupo 6: Misu, Ming-Hua I
        Grupo 7: Tho, Amon
        Grupo 8: Hama, Rafa
        Coeficiente: 11417428
    """, 
    '5_2.txt': """
        5_2.txt
        Grupo 1: Yakone, Yue, Pakku
        Grupo 2: Wei, Pakku I
        Coeficiente: 1894340
    """, 
    '6_3.txt': """
        6_3.txt
        Grupo 1: Wei, Hasook
        Grupo 2: Senna, Hama I
        Grupo 3: Hama, Wei I
        Coeficiente: 1640690
    """, 
    '6_4.txt': """
        6_4.txt
        Grupo 1: Huu
        Grupo 2: Eska
        Grupo 3: Sura
        Grupo 4: Hama, Sangok, Ming-Hua
        Coeficiente: 807418
    """, 
    '8_3.txt': """
        8_3.txt
        Grupo 1: Katara, Rafa
        Grupo 2: Hama, Unalaq, Amon, Tonraq
        Grupo 3: Misu, Hasook
        Coeficiente: 4298131
    """,
}

OFFSET = "        "

SOLUTIONS = {
    "-greedy":   lambda guerreros, k: tribu_agua_greedy(guerreros, k),
    "-back":     lambda guerreros, k: tribu_agua_backtracking(guerreros, k),
    "-lp":       lambda guerreros, k: tribu_agua_prog_lineal(guerreros, k, logs=False)
}


def leer_archivo(ARCHIVO):
    try:
        with open(ARCHIVO, "r") as grupos:
            lineas = [linea for linea in grupos if not linea.startswith("#")]
    except:
        print("Error al abrir el archivo de los grupos")
        return None, None
    
    cantidad_de_grupos = int(lineas[0].strip())
    
    nombre_y_habilidad = {}
    for linea in lineas[1:]:
        nombre, fuerza = linea.strip().split(SEPARADOR)
        nombre_y_habilidad[nombre] = int(fuerza)
    
    return cantidad_de_grupos, nombre_y_habilidad


def resultado_esperado_to_data(resultado_esperado_str):
    data = resultado_esperado_str.split("\n")
    data.pop(0)
    data.pop(0)
    data.pop()
    coeficiente = int(data.pop().split(":")[1])
    data = list(map(lambda item: item.replace("        ", ""), data))
    data = list(map(lambda item: item.split(":"), data))
    data = list(map(lambda item: item[1].replace(" ", "").split(","), data))

    data = sorted(data, key=lambda item: "".join(item))

    return data, coeficiente


def format_result(nombre, resultado, coeficiente):
    result = "\n"
    result += OFFSET + nombre + "\n"
    for key, value in resultado.items():
        guerreros = ", ".join(value)
        result += OFFSET + key + ": " + guerreros + "\n"
    result += OFFSET + "Coeficiente: " + str(coeficiente) + "\n" + "    "
    return result


def solve(f):
    for nombre in NOMBRES:
        print(f"\nProcessing test for file: {nombre}")

        file = f"TP3/{nombre}"
        cantidad_de_grupos, nombre_y_habilidad = leer_archivo(file)

        start_time = time.time()
        current_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
        print("Test start: ", current_date)

        # CALLING GREEDY SOLUTION
        #

        # CALLING BACKTRACKING SOLUTION
        #

        # CALLING LP SOLUTION
        resultado, coeficiente = f(nombre_y_habilidad, cantidad_de_grupos)

        end_time = time.time()
        current_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
        print("Test end: ", current_date)
        execution_time = end_time - start_time
        print("Execution time:", execution_time, "seconds")

        formatted_result_1 = format_result(nombre, resultado, coeficiente)
        formatted_result_2 = resultado_esperado_to_data(formatted_result_1)

        print(formatted_result_1)

        try:
            assert formatted_result_2 == resultado_esperado_to_data(RESULTS[nombre])
        except:
            print(f"FILE {nombre} NOT PASSED!!!!!\n")
            continue

        print(f"File {nombre} passed!\n")


def main():
    method = sys.argv[1]
    solve(SOLUTIONS[method])


main()
