from utils import combinatoria


def validar_entrada(n, k):
    if n < 0:
        raise ValueError("n debe ser >= 0")
    if k <= 0:
        raise ValueError("k debe ser > 0")

def distribucion_identicos(n, k):
    validar_entrada(n, k)
    return combinatoria(n + k - 1, k - 1)



def distribucion_sin_vacias(n, k):
    validar_entrada(n, k)
    if n < k:
        return 0 
    return combinatoria(n - 1, k - 1)



def distribucion_con_limite(n, k, m):
    validar_entrada(n, k)
    if m < 0:
        raise ValueError("m debe ser >= 0")

    total = 0

   
    for j in range(k + 1):
        signo = (-1) ** j
        formas = combinatoria(k, j) * combinatoria(n - j * (m + 1) + k - 1, k - 1)
        total += signo * formas

    return total
