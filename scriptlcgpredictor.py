# Este script es el resultado de la explotacion inicial de un CTF de DockerLabs (Predictable)
# Esta hecho para sacar el siguiente numero de un Generador Lineal Congruencial (LCG) a partir de una tabla
# Se necesitan minimo 4 datos para ver el siguiente numero
# Made by Ghxstsec

import sys

def solve_lcg_universal():
    print("="*50)
    print("   LCG PREDICTOR (MODO TRES PUNTOS)")
    print("="*50)

    try:
        n = 9223372036854775783 

        print("[*] Introduce 3 números CONSECUTIVOS de la tabla:")
        x1 = int(input("    [1/4] Primer valor (X1): "))
        x2 = int(input("    [2/4] Segundo valor (X2): "))
        x3 = int(input("    [3/4] Tercer valor (X3): "))
        
        print("\n[*] Punto de predicción:")
        x_last = int(input("    [4/4] Último valor conocido (X99): "))

        # --- LÓGICA MATEMÁTICA ---
        # m = (X3 - X2) * inv(X2 - X1) mod n
        num = (x3 - x2) % n
        den = (x2 - x1) % n
        
        # Inverso modular
        m = (num * pow(den, -1, n)) % n

        # c = X2 - (X1 * m) mod n
        c = (x2 - (x1 * m)) % n

        print("\n" + "-"*50)
        print(f"[+] Multiplicador (m) hallado: {m}")
        print(f"[+] Incremento (c) hallado:    {c}")
        print("-"*50)

        # Verificación: ¿El cálculo genera X3 a partir de X2?
        if (x2 * m + c) % n == x3:
            print("[✔] ¡Constantes Verificadas!")
            x_next = (x_last * m + c) % n
            print(f"\n[!!!] Siguiente numero del GLC: {x_next}\n")
        else:
            print("[X] ERROR: Los números no siguen una secuencia LCG.")

    except ValueError:
        print("\n[-] ERROR: No existe inverso modular. Esto ocurre si los números no son consecutivos.")

if __name__ == "__main__":
    solve_lcg_universal()
