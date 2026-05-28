def factorial(n):
    if n < 0:
        raise ValueError("n debe ser >= 0")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def combinatoria(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))
