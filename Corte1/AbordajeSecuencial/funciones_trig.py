import math

# Funciones trigonométricas en grados
def sin_deg(grados):
    return math.sin(math.radians(grados))

def cos_deg(grados):
    return math.cos(math.radians(grados))

def tan_deg(grados):
    return math.tan(math.radians(grados))

# Menú interactivo
def menu():
    print("=== Calculadora trigonométrica en grados ===")
    print("1. Seno")
    print("2. Coseno")
    print("3. Tangente")
    print("4. Salir")

while True:
    menu()
    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "4":
        print("¡Hasta luego!")
        break

    if opcion in ["1", "2", "3"]:
        try:
            angulo = float(input("Ingresa el ángulo en grados: "))
            if opcion == "1":
                print(f"sin({angulo}°) = {sin_deg(angulo):.5f}\n")
            elif opcion == "2":
                print(f"cos({angulo}°) = {cos_deg(angulo):.5f}\n")
            elif opcion == "3":
                # Manejo especial para tangentes indefinidas (90°, 270°, etc.)
                if abs(cos_deg(angulo)) < 1e-10:
                    print(f"tan({angulo}°) no está definida (tiende a infinito)\n")
                else:
                    print(f"tan({angulo}°) = {tan_deg(angulo):.5f}\n")
        except ValueError:
            print("Por favor, ingresa un número válido.\n")
    else:
        print("Opción no válida. Intenta de nuevo.\n")
