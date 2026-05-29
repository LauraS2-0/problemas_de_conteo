# Modelado Combinatorio con Python
## Conteo, algoritmos y estructuras aplicadas al análisis de datos

### Autor
Laura Sophia Castro Amaya
Universidad Nacional de Colombia

---

### Resumen

Este proyecto transforma problemas clásicos de combinatoria en herramientas computacionales interactivas, permitiendo modelar:
 - Estructuras binarias (0/1)
 - Distribución de recursos
 - Conteo bajo restricciones
Todo mediante código modular, validado y eficiente.
---

### Descripción 

Este proyecto tiene como objetivo desarrollar soluciones generales a problemas de conteo en matemáticas discretas, mediante la implementación de algoritmos en Python.
A diferencia de resolver casos específicos, se construyen herramientas que permiten:
 - Ingresar parámetros variables
 - Validar entradas
 - Aplicar modelos combinatorios correctamente
 - Obtener resultados para múltiples escenarios
De esta manera, el proyecto conecta el razonamiento matemático con su implementación computacional, permitiendo modelar problemas de forma estructurada y eficiente.
---

### Características principales

 - Implementación general (no casos fijos)
 - Validación de entradas robusta
 - Pruebas automatizadas
 - Arquitectura modular
 - Uso de principios combinatorios
 - Código reutilizable y escalable
---

### Módulos principales

| Módulo            | Descripción                                     |
| ----------------- | ----------------------------------------------- |
| `binarios.py`     | Conteo de cadenas binarias con restricciones    |
| `distribucion.py` | Distribución de objetos en cajas                |
| `utils.py`        | Funciones matemáticas (factorial, combinatoria) |
| `main.py`         | Interfaz interactiva                            |
---

### Enfoque
Este proyecto no solo resuelve ejercicios puntuales, sino que:

 - Modela estructuras discretas
 - Implementa algoritmos basados en matemáticas
 - Aplica combinatoria en contextos computacionales
Con un enfoque cercano a análisis de datos y modelado algorítmico.
---

### Fundamento matemático
El proyecto se basa en principios fundamentales de la combinatoria, especialmente en el uso de factoriales y coeficientes binomiales.

 - Factorial

El factorial de un número n se define como: n!=n⋅(n−1)⋅(n−2)⋯1

Se utiliza para contar el número de formas de ordenar elementos.

 - Combinatoria (coeficiente binomial)

El número de formas de elegir k elementos de un conjunto de n elementos está dado por:

Este principio es fundamental en:
 - Conteo de cadenas binarias
 - Distribución de objetos
 - Cálculo de combinaciones bajo restricciones
 - 
 **Aplicación en el proyecto**

En lugar de generar todas las configuraciones posibles (lo cual sería computacionalmente costoso), el programa utiliza directamente estas fórmulas para:
- Reducir la complejidad
- Optimizar el cálculo
- Permitir trabajar con valores más grandes
---

### Problemas implementados
**Problema 3: Cadenas binarias con restricciones**
Se estudia el número de cadenas binarias de longitud n bajo distintas condiciones.
 Modelos:
         - Total:
         $$
         2^n
         $$
         
         - Exactamente k:
         $$
         \binom{n}{k}
         $$
         
         - A lo sumo k:
         $$
         \sum_{i=0}^{k} \binom{n}{i}
         $$
         
         - Al menos k:
         $$
         \sum_{i=k}^{n} \binom{n}{i}
         $$
         
         - Balanceadas:
         $$
         \binom{n}{n/2}
         $$

**Problema 7: Distribución de objetos en caja**
Modela la asignación de *n* objetos en *k* cajas
 Modelos:
         - Con cajas vacías: 2
         - Sin cajas vacías:
         - Con límite por caja: Aplicación del principio de inclusión-exclusión

---

### Ejecución 
 - python main.py

**Pruebas**
 - python -m unittest tests/test_binarios.py
 - python -m unittest tests/test_distribucion.py

---

### Validación
El sistema maneja:
 - Valores negativos
 - Parámetros inválidos
 - Casos imposibles
---

### Posibles mejoras
 - Visualización gráfica
 - Simulación de distribuciones
 - Interfaz gráfica
 - Integración con grafos
