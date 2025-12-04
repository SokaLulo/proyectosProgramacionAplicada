def selectionSort(arr):
    n = len(arr)

    for i in range(n - 1):
        minIndex = i

        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j

        if minIndex != i:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]

def printArray(arr):
    print(*arr)

if __name__ == "__main__":
    arr = [5, 3, 6, 1, 4]
    n = len(arr)

    print("Arreglo original:")
    printArray(arr)

    selectionSort(arr)

    print("Arreglo ordenado:")
    printArray(arr)
