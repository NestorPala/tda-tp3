# TP3 de TDA - FIUBA


### Integrantes

* Palavecino Arnold, Nestor Fabian - 108244
* Vázquez Morales, Matias - 111083


## Probar el TP3 con un archivo de pruebas de "n" guerreros en "k" grupos

<code>SOLVER</code> : "-back", "-lp", "-aprox" o "-greedy" <br><br>

Si el archivo está en la misma carpeta que tp3.py:

<code>python tp3.py -file ARCHIVO_GUERREROS.txt SOLVER</code>

Ejemplo: <br> *python tp3.py -file 5_2.txt -greedy*

<br>

Si el archivo está en cualquier ruta:

<code>python tp3.py -abs PATH_TO_/ARCHIVO_GUERREROS.txt SOLVER</code>

Ejemplo: <br> *python tp3.py -abs C:\Users\Nestor\Desktop\5_2.txt -greedy*

----

## Ejecutar tests de la cátedra

Se corren junto con las pruebas de tiempo. 

<code>python tests_catedra.py</code>

----

## Ejecutar las pruebas de tiempo del algoritmo

Estas pruebas se pueden correr para cualquier archivo de guerreros. 

<br>

<code>SOLVER</code> : "-back", "-lp", "-aprox" o "-greedy" <br><br>

Si el archivo está en la misma carpeta que pruebas_tiempo_algoritmo.py:

<code>python pruebas_tiempo_algoritmo.py -file ARCHIVO_GUERREROS.txt</code>

Ejemplo: <br>  *python pruebas_tiempo_algoritmo.py -file 5_2.txt -greedy*

<br>

Si el archivo está en cualquier ruta:

<code>python pruebas_tiempo_algoritmo.py -abs PATH_TO_/ARCHIVO_GUERREROS.txt</code>

Ejemplo: <br>  *python pruebas_tiempo_algoritmo.py -abs C:\Users\Nestor\Desktop\5_2.txt -greedy*

----

## Generar archivo de conjunto de guerreros

<code>python generador.py CANTIDAD_DE_GUERREROS CANTIDAD_DE_GRUPOS</code>

Ejemplo: <br>  *python generador.py 5 2*
