# main.py
from Caballo.lanzador import JuegoCaballo as CaballoLanzador
from Reina.lanzador import Lanzador as ReinasLanzador

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Ejecutar simulación del caballo")
    print("2. Ejecutar simulación de las reinas")
    print("3. Salir")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Ingrese su elección: ")
        
        if opcion == "1":
            CaballoLanzador.ejecutar_simulacion()  # Ejecutar simulación del caballo
        elif opcion == "2":
            ReinasLanzador.ejecutar_simulacion()  # Ejecutar simulación de las reinas
        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
