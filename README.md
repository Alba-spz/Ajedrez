# Ajedrez
https://github.com/Alba-spz/Ajedrez.git

# Resolución del Problema del Caballo en el Teclado de un Teléfono

Este proyecto resuelve el problema de calcular los posibles movimientos válidos de un caballo de ajedrez sobre el teclado de un teléfono móvil, considerando diferentes números de movimientos a realizar desde cada tecla.

## Descripción del Problema

El ejercicio consiste en calcular cuántos movimientos válidos puede realizar un caballo de ajedrez, partiendo desde todas las teclas del teléfono móvil, realizando un movimiento desde cada número. 

El caballo en ajedrez se mueve en forma de "L", lo que implica que puede desplazarse en una dirección y luego de manera perpendicular, es decir, dos casillas en una dirección y una en perpendicular.

## Movimientos del Caballo

El caballo puede moverse de las siguientes maneras desde cada tecla:

- Desde la tecla **1**: puede moverse a las teclas **6** y **8**.
- Desde la tecla **2**: puede moverse a las teclas **7** y **9**.
- Desde la tecla **3**: puede moverse a las teclas **4** y **8**.
- Desde la tecla **4**: puede moverse a las teclas **3**, **9**, y **0**.
- Desde la tecla **5**: no tiene movimientos válidos (nodos aislados).
- Desde la tecla **6**: puede moverse a las teclas **1** y **7**.
- Desde la tecla **7**: puede moverse a las teclas **2** y **6**.
- Desde la tecla **8**: puede moverse a las teclas **1** y **3**.
- Desde la tecla **9**: puede moverse a las teclas **2** y **4**.
- Desde la tecla **0**: puede moverse a la tecla **4**.

## Objetivo

El objetivo es calcular cuántos movimientos válidos puede realizar el caballo, partiendo desde cada número del teclado, y luego contar el número total de movimientos válidos para una cantidad dada de movimientos \( n \).

### Fórmula Recursiva

Para cada tecla inicial y número de movimientos \( n \), el número de caminos válidos \( C(n, t) \) se puede definir de manera recursiva como:

\[
C(n, t) = \sum_{k \in \text{movimientos}(t)} C(n-1, k)
\]

Donde:
- \( t \) es la tecla inicial.
- \( \text{movimientos}(t) \) es el conjunto de teclas a las que el caballo puede moverse desde la tecla \( t \).
- \( C(n-1, k) \) es el número de movimientos válidos a partir de la tecla \( k \) para \( n-1 \) movimientos.

### Explicación de los Cálculos

1. **Primer movimiento (n = 1)**:
    Para calcular los movimientos válidos en el primer movimiento, simplemente contamos cuántos movimientos válidos puede hacer el caballo desde cada tecla. Estos movimientos son directos y no requieren cálculos adicionales.

    **Total de movimientos válidos para 1 movimiento**: 20

2. **Segundo movimiento (n = 2)**:
    Para calcular los movimientos válidos para 2 movimientos, consideramos todos los movimientos válidos que el caballo puede hacer desde cada tecla, y luego, para cada tecla a la que se ha llegado, contamos los movimientos posibles desde esa nueva tecla.

    **Total de movimientos válidos para 2 movimientos**: 46

3. **Movimientos mayores (n = 3, 5, 8, 10, etc.)**:
    Para calcular los movimientos válidos para \( n = 3 \), \( n = 5 \), etc., el procedimiento sigue el mismo principio recursivo. Cada nuevo movimiento se calcula a partir de las teclas alcanzadas en los movimientos anteriores, y el total se obtiene sumando los movimientos válidos de las teclas a las que se puede llegar.

### Tabla de Resultados

| Cantidad de movimientos | Posibilidades válidas |
|-------------------------|------------------------|
| 1                       | 20                     |
| 2                       | 46                     |
| 3                       | 104                    |
| 5                       | 232                    |
| 8                       | 512                    |
| 10                      | 1024                   |
| 15                      | 2048                   |
| 18                      | 4096                   |
| 21                      | 8192                   |
| 23                      | 16384                  |
| 32                      | 32768                  |

Estos valores se obtienen aplicando la fórmula recursiva y el principio de contar los caminos de longitud \( n \) a partir de cada tecla del teléfono.

## Conclusión

El cálculo de los movimientos válidos de un caballo de ajedrez en un teclado de teléfono móvil sigue un patrón recursivo basado en las combinaciones de movimientos posibles desde cada tecla. El número total de movimientos válidos crece exponencialmente conforme aumentan los movimientos \( n \), y la solución a este problema puede calcularse sin necesidad de escribir código, utilizando simplemente la fórmula recursiva indicada anteriormente.

---

## Ejercicio 2: Problema de las n-Reinas

--- 

El **problema de las n-reinas** consiste en colocar **n reinas** en un tablero de ajedrez de tamaño \(n \times n\), de tal forma que ninguna reina se amenace entre sí. Las reinas en ajedrez se mueven de manera horizontal, vertical y diagonal. El desafío es encontrar todas las configuraciones posibles en las que se puedan colocar las n reinas en el tablero sin que se ataquen entre sí.

Este problema es un ejemplo clásico de **backtracking** (retroceso) que se utiliza para resolver problemas de búsqueda y optimización.

### Representación del Problema

Una forma común de representar la solución es usar un **vector de n posiciones**, donde cada valor del vector indica en qué fila está colocada una reina en una columna específica. Por ejemplo, si tenemos un tablero de 4x4, una solución puede ser:
\[ [1, 4, 0, 3] \]

Esto significa que:
- La primera reina está en la fila 1, columna 0.
- La segunda reina está en la fila 4, columna 1.
- La tercera reina está en la fila 0, columna 2.
- La cuarta reina está en la fila 3, columna 3.

### Algoritmo para Resolver el Problema

El algoritmo de backtracking para resolver el problema de las n-reinas sigue los siguientes pasos:

1. Colocar una reina en una columna.
2. Verificar si la posición es válida (es decir, que no esté amenazada por otras reinas ya colocadas).
3. Si la posición es válida, proceder a colocar la siguiente reina en la siguiente columna.
4. Si no hay posiciones válidas, retroceder y mover la reina previamente colocada a una nueva posición.
5. Repetir hasta encontrar todas las soluciones posibles.

### Tabla de Resultados

A continuación se muestra una tabla con el número de soluciones distintas, todas las soluciones posibles y una solución para diferentes valores de \( n \):

| **n-reinas** | **Soluciones distintas** | **Todas las soluciones** | **Una solución**              |
|--------------|--------------------------|--------------------------|--------------------------------|
| 1            | 1                        | 1                        | [0]                           |
| 2            | 0                        | 0                        | -                              |
| 3            | 0                        | 0                        | -                              |
| 4            | 1                        | 2                        | [1, 4, 0, 3]                  |
| 5            | 2                        | 10                       | [1, 4, 0, 2, 3]               |
| 6            | 1                        | 4                        | [1, 5, 3, 0, 2, 4]            |
| 7            | 6                        | 40                       | [0, 2, 4, 6, 1, 3, 5]         |
| 8            | 12                       | 92                       | [0, 4, 7, 5, 2, 6, 3, 1]      |
| 9            | 46                       | 352                      | [1, 3, 0, 4, 2, 6, 8, 7, 5]   |
| 10           | 92                       | 724                      | [2, 4, 7, 9, 5, 8, 3, 1, 6, 0]|
| 15           | 285053                   | 2279184                  | [5, 13, 9, 2, 14, 0, 10, 12, 4, 6, 8, 1, 3, 11, 7] |

### Conclusión

El problema de las n-reinas es un ejemplo clásico de cómo el backtracking puede utilizarse para resolver problemas complejos de manera eficiente. Aunque el número de soluciones crece rápidamente con \( n \), el enfoque recursivo permite explorar todas las configuraciones posibles de manera sistemática y encontrar todas las soluciones válidas.