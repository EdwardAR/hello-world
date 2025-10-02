print("Hello, world") 

import matplotlib.pyplot as plt

# Función para generar la secuencia de Fibonacci
def fibonacci(n):
    secuencia = [0, 1]
    for i in range(2, n):
        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)
    return secuencia

# Solicita al usuario cuántos términos desea
n = int(input("¿Cuántos términos de Fibonacci quieres generar? (mínimo 2): "))

if n >= 2:
    fib = fibonacci(n)
    print("🔢 Secuencia de Fibonacci:", fib)

    # Visualiza la secuencia
    plt.plot(fib, marker='o', linestyle='-', color='purple')
    plt.title(f"Secuencia de Fibonacci ({n} términos)")
    plt.xlabel("Índice")
    plt.ylabel("Valor")
    plt.grid(True)
    plt.show()
else:
    print("⚠️ Debes ingresar un número mayor o igual a 2.")
    