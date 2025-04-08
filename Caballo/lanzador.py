import pygame
from .caballos import Caballo

class JuegoCaballo:
    """Clase para gestionar el juego del caballo en el tablero"""
    def __init__(self):
        self.caballo = Caballo()
        self.caballo.generar_vecinos()
        self.running = False

    def mostrar_tablero(self, screen, font):
        """Dibuja el tablero de ajedrez con los números del teclado"""
        screen.fill((255, 255, 255))
        colors = [(200, 200, 200), (150, 150, 150)]

        for i in range(4):
            for j in range(3):
                if self.caballo.tablero[i][j] != 0:
                    rect = pygame.Rect(j * 150 + 50, i * 150 + 50, 100, 100)
                    pygame.draw.rect(screen, colors[(i + j) % 2], rect)
                    text = font.render(str(self.caballo.tablero[i][j]), True, (0, 0, 0))
                    screen.blit(text, rect.move(30, 30))

        pygame.display.update()

    def ejecutar_movimientos(self, inicio, movimientos):
        """Devuelve la cantidad de caminos posibles"""
        return self.caballo.obtener_movimientos_validos(inicio, movimientos)

    def ejecutar(self, screen, font):
        """Reservado para ejecución continua si se desea animar luego"""
        pass

    @staticmethod
    def ejecutar_simulacion():
        print("Simulación del juego del caballo iniciada.")
        pygame.init()
        screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Juego del Caballo")
        font = pygame.font.SysFont(None, 48)

        juego = JuegoCaballo()
        juego.mostrar_tablero(screen, font)

        # Mostrar algunos resultados en consola
        total = 0
        for i in range(10):
            caminos = juego.ejecutar_movimientos(i, 2)
            print(f"Desde {i}: {caminos} caminos posibles")
            total += caminos

        print(f"Total caminos válidos con 2 movimientos: {total}")
        pygame.time.wait(3000)
        pygame.quit()


