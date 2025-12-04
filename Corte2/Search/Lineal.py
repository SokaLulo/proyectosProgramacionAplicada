def linear_search(arr, key):
    """Devuelve la primera posición donde aparece key, o -1 si no está."""
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def linear_search_all(arr, key):
    """Devuelve una lista con TODAS las posiciones donde aparece key."""
    indices = []
    for i in range(len(arr)):
        if arr[i] == key:
            indices.append(i)
    return indices


def main():
    # Arreglo de ejemplo (puedes cambiarlo)
    arr = [4, 9, 2, 7, 5, 7, 9, 7]

    print("Arreglo:", arr)

    key = int(input("Ingrese el numero a buscar: "))

    # --- Primera aparición ---
    pos = linear_search(arr, key)

    if pos == -1:
        print(f"El numero {key} NO se encuentra en el arreglo.")
    else:
        print(f"El numero {key} se encuentra (al menos) en la posicion {pos} (indice 0-based).")

    # --- Todas las apariciones ---
    indices = linear_search_all(arr, key)

    if len(indices) == 0:
        print(f"No se encontraron ocurrencias de {key}.")
    else:
        print(f"El numero {key} aparece {len(indices)} veces, en las posiciones: {indices}")


if __name__ == "__main__":
    main()
