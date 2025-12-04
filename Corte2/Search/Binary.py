def first_occurrence(arr, key):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            result = mid
            high = mid - 1
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return result


def last_occurrence(arr, key):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            result = mid
            low = mid + 1
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return result


def main():
    arr = [3, 5, 7, 9, 11, 11, 11, 11, 13, 15]
    print("Arreglo (ordenado):", arr)

    key = int(input("Ingrese el numero a buscar: "))

    first = first_occurrence(arr, key)
    last = last_occurrence(arr, key)

    if first == -1:
        print(f"El numero {key} NO se encuentra en el arreglo.")
    else:
        count = last - first + 1
        print(f"El numero {key} aparece {count} veces.")
        print("Posiciones (indices 0-based):", list(range(first, last + 1)))


if __name__ == "__main__":
    main()
