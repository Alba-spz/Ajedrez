class Caballo:
    def __init__(self):
        # Teclado tipo teléfono con ceros como espacios inválidos
        self.tablero = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [0, 0, 0]
        ]

        # Movimientos válidos desde cada tecla (caballo de ajedrez)
        self.movimientos_caballo = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

    def generar_vecinos(self):
        print("Generando vecinos según movimientos de caballo...")

    def obtener_movimientos_validos(self, inicio, profundidad):
        def dfs(actual, profundidad):
            if profundidad == 0:
                return 1
            total = 0
            for vecino in self.movimientos_caballo.get(actual, []):
                total += dfs(vecino, profundidad - 1)
            return total

        print(f"Obteniendo movimientos desde {inicio} con profundidad {profundidad}")
        return dfs(inicio, profundidad)

    def jugar(self):
        print("Ejecutando simulación del caballo:")
        self.generar_vecinos()
        total = 0
        for i in range(10):
            movimientos = self.obtener_movimientos_validos(i, 2)
            print(f"Desde {i}: {movimientos} caminos")
            total += movimientos
        print(f"Total de caminos válidos: {total}")

