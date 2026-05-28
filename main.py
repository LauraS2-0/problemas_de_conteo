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




def menu_binarios():
    print("\n--- PROBLEMA 3: CADENAS BINARIAS ---")
    print("1. Total de cadenas")
    print("2. Exactamente k unos")
    print("3. A lo más k unos")
    print("4. Al menos k unos")
    print("5. Igual número de ceros y unos")
    print("6. Volver")


def ejecutar_binarios():
    while True:
        menu_binarios()
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





def menu_distribucion():
    print("\n--- PROBLEMA 7: DISTRIBUCIÓN DE OBJETOS ---")
    print("1. Objetos idénticos (cajas con vacías)")
    print("2. Objetos idénticos (sin cajas vacías)")
    print("3. Distribución con límite por caja")
    print("4. Volver")


def ejecutar_distribucion():
    while True:
        menu_distribucion()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                n = int(input("Ingrese n (objetos): "))
                k = int(input("Ingrese k (cajas): "))
                print("Resultado:", distribucion_identicos(n, k))

            elif opcion == "2":
                n = int(input("Ingrese n (objetos): "))
                k = int(input("Ingrese k (cajas): "))
                print("Resultado:", distribucion_sin_vacias(n, k))

            elif opcion == "3":
                n = int(input("Ingrese n (objetos): "))
                k = int(input("Ingrese k (cajas): "))
                m = int(input("Ingrese el máximo por caja (m): "))
                print("Resultado:", distribucion_con_limite(n, k, m))

            elif opcion == "4":
                break

            else:
                print("Opción inválida")

        except ValueError as e:
            print("Error:", e)
            
def menu_principal():
    print("\n=== PROYECTO BONO - MATEMÁTICAS DISCRETAS ===")
    print("1. Problema 3 - Cadenas binarias")
    print("2. Problema 7 - Distribución de objetos")
    print("3. Salir")


def main():
    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejecutar_binarios()

        elif opcion == "2":
            ejecutar_distribucion()

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
