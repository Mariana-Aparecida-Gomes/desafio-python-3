def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

resultado = calcular_fatorial(5)
print(resultado)  # Saída: 120