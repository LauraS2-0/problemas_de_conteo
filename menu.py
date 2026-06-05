from binarios import (
    total_cadenas,
    exactamente_k_unos,
    a_lo_mas_k_unos,
    al_menos_k_unos,
    igual_ceros_unos
)

from distribucion import (
    distribucion_identicos,
    distribucion_sin_vacias,
    distribucion_con_limite
)


# ===============================
# MENÚ PRINCIPAL
# ===============================
def iniciar_menu():
    while True:
        print("\n=== PROYECTO BONO - MATEMÁTICAS DISCRETAS ===")
        print("1. Problema 3 - Cadenas binarias")
        print("2. Problema 7 - Distribución de objetos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_binarios()
        elif opcion == "2":
            menu_distribucion()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")


# ===============================
# PROBLEMA 3
# ===============================
def menu_binarios():
    while True:
        print("\n--- CADENAS BINARIAS ---")
        print("1. Total de cadenas")
        print("2. Exactamente k unos")
        print("3. A lo más k unos")
        print("4. Al menos k unos")
        print("5. Igual número de ceros y unos")
        print("6. Volver")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                n = int(input("Ingrese n: "))
                print("Resultado:", total_cadenas(n))

            elif opcion == "2":
                n = int(input("Ingrese n: "))
                k = int(input("Ingrese k: "))
                print("Resultado:", exactamente_k_unos(n, k))

            elif opcion == "3":
                n = int(input("Ingrese n: "))
                k = int(input("Ingrese k: "))
                print("Resultado:", a_lo_mas_k_unos(n, k))

            elif opcion == "4":
                n = int(input("Ingrese n: "))
                k = int(input("Ingrese k: "))
                print("Resultado:", al_menos_k_unos(n, k))

            elif opcion == "5":
                n = int(input("Ingrese n: "))
                print("Resultado:", igual_ceros_unos(n))

            elif opcion == "6":
                break

            else:
                print("Opción inválida")

        except ValueError as e:
            print("Error:", e)


# ===============================
# PROBLEMA 7
# ===============================
def menu_distribucion():
    while True:
        print("\n--- DISTRIBUCIÓN DE OBJETOS ---")
        print("1. Con cajas vacías")
        print("2. Sin cajas vacías")
        print("3. Con límite por caja")
        print("4. Volver")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                n = int(input("Ingrese n: "))
                k = int(input("Ingrese k: "))
                print("Resultado:", distribucion_identicos(n, k))

            elif opcion == "2":
                n = int(input("Ingrese n: "))
                k = int(input("Ingrese k: "))
                print("Resultado:", distribucion_sin_vacias(n, k))

            elif opcion == "3":
                n = int(input("Ingrese n: "))
                k = int(input("Ingrese k: "))
                m = int(input("Ingrese máximo por caja: "))
                print("Resultado:", distribucion_con_limite(n, k, m))

            elif opcion == "4":
                break

            else:
                print("Opción inválida")

        except ValueError as e:
            print("Error:", e)