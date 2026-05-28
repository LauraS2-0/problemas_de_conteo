from utils import combinatoria


def validar_entrada(n, k=None):
    if n < 0:
        raise ValueError("n debe ser no negativo")
    if k is not None:
        if k < 0 or k > n:
            raise ValueError("k debe cumplir 0 <= k <= n")


def total_cadenas(n):
    validar_entrada(n)
    return 2 ** n


def exactamente_k_unos(n, k):
    validar_entrada(n, k)
    return combinatoria(n, k)


def a_lo_mas_k_unos(n, k):
    validar_entrada(n, k)
    return sum(combinatoria(n, i) for i in range(k + 1))


def al_menos_k_unos(n, k):
    validar_entrada(n, k)
    return sum(combinatoria(n, i) for i in range(k, n + 1))


def igual_ceros_unos(n):
    validar_entrada(n)
    if n % 2 != 0:
        return 0
    return combinatoria(n, n // 2)
