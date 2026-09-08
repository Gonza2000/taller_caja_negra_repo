## Actividad 1 - Mapa conceptual
<img width="1805" height="1000" alt="Caja Negra MC" src="https://github.com/user-attachments/assets/817d5194-b01f-43d4-824d-e92c4abac651" />


## Actividad 3 y 4 - Casos de Prueba.

## 1. Caso de Prueba 01
Probamos con la entrada de socios <=0 como clase inválida y 0 como valor límite

| ID | Descripción | Precondición | Entrada | Esperado | Real | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CP-01 | Comportamiento con 0 socios | Script iniciado en terminal / listo para ingreso de datos | presupuesto total: 100, socios: 0, meses: 10 | Mensaje de división no disponible/ volver a intentar, ejecución normal. | pendiente | pendiente |

#### Ejecutar y Localizar el Bug
Log de Consola:
```
Traceback (most recent call last):
  File "C:\Users\GONZALO GABRIEL\Desktop\Diseño y Testing\presupuesto_analisis.py", line 15, in <module>
    calcular_presupuesto()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\GONZALO GABRIEL\Desktop\Diseño y Testing\presupuesto_analisis.py", line 9, in calcular_presupuesto
    cuota_por_socio = total / socios
                      ~~~~~~^~~~~~~~
ZeroDivisionError: float division by zero
```
#### Reporte del Defecto
El código nunca valida socios es igual a 0 antes de dividir.
| ID | Descripción | Precondición | Entrada | Esperado | Real | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CP-01 | Comportamiento con 0 socios | Script iniciado en terminal / listo para ingreso de datos | presupuesto total: 100, socios: 0, meses: 10 | Mensaje de división no disponible, ejecución normal. | ZeroDivisionError: float division by zero en la línea 9 | Failed |
##  2. Caso de Prueba 02
Probamos el bloque inválido de presupuesto < 0 y límite -3
| ID | Descripción | Precondición | Entrada | Esperado | Real | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CP-02 | Comportamiento con presupuesto negativo| Script iniciado en terminal / listo para ingreso de datos | presupuesto total: -3, socios: 23, meses: 23 | Mensaje de presupuesto negativo/volver a intentar, ejecución normal | pendiente | pendiente |
#### Ejecutar y Localizar el Bug
Log de Consola:
```
=== Sistema de Análisis de Presupuesto ===

Ingrese el presupuesto total: -3
Ingrese el número de socios: 23
Ingrese los meses de inversión: 23

Presupuesto inicial: $-3.00
Intereses generados: $-31.74
Total con intereses: $-34.74
Cuota por socio (23 socios): $-1.51
```
#### Reporte del Defecto
El código no valida que presupuesto no puede ser negativo y altera el resultado.
| ID | Descripción | Precondición | Entrada | Esperado | Real | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CP-02 | Comportamiento con presupuesto negativo| Script iniciado en terminal / listo para ingreso de datos | presupuesto total: -3, socios: 23, meses: 23 | Mensaje de presupuesto negativo/volver a intentar, ejecución normal | Ejecuta la operación con presupuesto negativo, resultado negativo, el programa termina con éxito | Failed |
## 3. Caso de Prueba 03
Probamos con clase inválida de cadenas vacías o inputs no numéricos
| ID | Descripción | Precondición | Entrada | Esperado | Real | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CP-03 | Input vacío | Script iniciado en terminal / listo para ingreso de datos | presupuesto total: 0, socios:0, meses:0 | Ingrese un valor para continuar/Volver a intentar, ejecución normal| pendiente | pendiente |
#### Ejecutar y Localizar el Bug
Log de Consola:
```
=== Sistema de Análisis de Presupuesto ===

Ingrese el presupuesto total:
Traceback (most recent call last):
  File "C:\Users\GONZALO GABRIEL\Desktop\Diseño y Testing\presupuesto_analisis.py", line 15, in <module>
    calcular_presupuesto()
    ~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\GONZALO GABRIEL\Desktop\Diseño y Testing\presupuesto_analisis.py", line 3, in calcular_presupuesto
    presupuesto = float(input("Ingrese el presupuesto total: "))
ValueError: could not convert string to float: ''

```
#### Reporte del Defecto
Falta de control de validación de cadenas vacías antes de aplicar el casteo de tipos float() o int()
| ID | Descripción | Precondición | Entrada | Esperado | Real | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CP-03 | Input vacío | Script iniciado en terminal / listo para ingreso de datos | presupuesto total: 0, socios:0, meses:0 | Ingrese un valor para continuar/Volver a intentar, ejecución normal| ValueError: could not convert string to float: '' | Failed |



