def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        for j in range(n - i - 1):
            
            if arr[j] > arr[j + 1]:
                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def printArray(arr):
    print(*arr)

if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    n = len(arr)
    print(f"Tamaño del arreglo: {n}")

    print("Arreglo original:")
    printArray(arr)
    
    bubbleSort(arr)

    print("Arreglo ordenado:")
    printArray(arr)
