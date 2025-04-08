class Lanzador:
    """Lanzador para ejecutar la simulación del juego de las n-reinas."""
    @staticmethod
    def ejecutar_simulacion():
        """Ejecuta la simulación de las reinas."""
        print("Bienvenido al juego de las N-Reinas")
        # Aquí puedes agregar la lógica que desees para elegir el tamaño del tablero
        n = int(input("Introduce el tamaño del tablero (N): "))
        from .reina import NReinas
        n_reinas = NReinas(n)
        n_reinas.ejecutar_simulacion()
