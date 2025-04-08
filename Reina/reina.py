# reinas.py

class NReinas:
    """Clase para resolver el problema de las n-reinas."""
    def __init__(self, n):
        self.n = n
        self.soluciones = []

    def es_seguro(self, tablero, fila, col):
        """Verifica si se puede colocar una reina en la posición (fila, col)."""
        for i in range(fila):
            if tablero[i] == col or \
               tablero[i] - i == col - fila or \
               tablero[i] + i == col + fila:
                return False
        return True

    def resolver(self, tablero, fila):
        """Resuelve el problema de las n-reinas de forma recursiva."""
        if fila == self.n:
            self.soluciones.append(tablero[:])
            return
        for col in range(self.n):
            if self.es_seguro(tablero, fila, col):
                tablero[fila] = col
                self.resolver(tablero, fila + 1)
                tablero[fila] = -1

    def ejecutar_simulacion(self):
        """Ejecuta la simulación y muestra todas las soluciones posibles."""
        tablero = [-1] * self.n  # Inicia un tablero vacío
        self.resolver(tablero, 0)
        print(f"Soluciones para {self.n}-reinas:")
        for sol in self.soluciones:
            print(sol)

