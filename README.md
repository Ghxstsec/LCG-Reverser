# 🛡️ Herramienta de predicción y criptoanálisis de LCG

Este repositorio contiene una herramienta/exploit desarrollado en Python diseñado para realizar ingeniería inversa a los **Generadores Congruenciales Lineales (LCG)**. Al observar una pequeña ventana de salida, este script puede derivar las constantes internas y predecir cada número futuro de la secuencia, siempre teniendo en cuenta que se necesitara saber 4 puntos de una tabla en total.

Script usado en el acceso inicial de la maquina **Predictable** de la plataforma **DockerLabs**

---

## 📖 Trasfondo Teórico

Un Generador Congruencial Lineal (LCG) es un algoritmo común para generar una secuencia de números pseudo-aleatorios. Se define por la siguiente relación de recurrencia:

$$X_{n+1} = (a \cdot X_n + c) \pmod m$$

Donde:
* **$X$**: La secuencia de valores pseudo-aleatorios.
* **$m > 0$**: El "módulo".
* **$a$**: El "multiplicador" ($0 < a < m$).
* **$c$**: El "incremento" ($0 \le c < m$).

Aunque son rápidos, los LCG **no son criptográficamente seguros**. Si el módulo ($m$) es conocido, solo necesitamos tres valores consecutivos para romper completamente el generador.

---

## 🧠 Cómo funciona el Exploit

La herramienta realiza un **Ataque de Tres Puntos**:

1.  **Calcular el Multiplicador ($a$):**
    La diferencia entre valores consecutivos sigue la regla: 
    $(X_3 - X_2) \equiv a(X_2 - X_1) \pmod m$.
    Resolvemos para $a$ calculando el **Inverso Multiplicativo Modular** de $(X_2 - X_1)$.

2.  **Calcular el Incremento ($c$):**
    Una vez conocido $a$, hallamos $c$ mediante: 
    $c \equiv (X_2 - aX_1) \pmod m$.

3.  **Verificación:**
    El script valida las constantes contra el tercer valor conocido para asegurar que la predicción sea 100% precisa.

---

## 🚀 Características

* **CLI Interactivo:** Introduce valores en tiempo real durante CTFs.
* **Alta Precisión:** Maneja módulos primos extremadamente grandes (ej. enteros de 64 bits).
* **Sin Dependencias:** Utiliza Python 3.8+ puro (lógica `pow(a, -1, m)`).
* **Predicción Rápida:** Deriva las constantes y predice el siguiente estado de forma instantánea.

---

## 🛠️ Uso

1. **Clonar el repo:**
   ```bash
   git clone https://github.com/Ghxstsec/LCG-Reverser.git
   cd lcg-predictor.py
   python3 lcg-predictor.py
