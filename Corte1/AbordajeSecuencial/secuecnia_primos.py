import time

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

try:
    num = 1
    while True:
        if es_primo(num):
            print(f"{num} es primo")
        else:
            print(f"{num} no es primo")
        num += 1
        time.sleep(1)
except KeyboardInterrupt:
    print("\nSaliendo del programa...")
