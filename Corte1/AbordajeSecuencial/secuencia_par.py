import time

try:
    num = 1
    while True:
        if num % 2 == 0:
            print(f"{num} es par")
        else:
            print(f"{num} es impar")
        num += 1
        time.sleep(1)
except KeyboardInterrupt:
    print("\nSaliendo del programa...")
