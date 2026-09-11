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
Probamos la partición válida  cálculo de intereses con valores normales

| ID | Descripción | Precondición | Entrada | Esperado | Real | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CP-03 | Cálculo de intereses y cuota por socio | Script iniciado en terminal / listo para ingreso de datos | presupuesto total: 1000, socios: 2, meses: 2 | Intereses generados: $40.00, Total: $1040.00, Cuota: $520.00 | pendiente | pendiente |

#### Ejecutar y Localizar el Bug
Log de Consola:

```
=== Sistema de Análisis de Presupuesto ===

Ingrese el presupuesto total: 1000
Ingrese el número de socios: 2
Ingrese los meses de inversión: 2

Presupuesto inicial: $1000.00
Intereses generados: $80.00
Total con intereses: $1080.00
Cuota por socio (2 socios): $540.00
```
#### Reporte del Defecto
El fallo ocurre en la línea 7: la fórmula eleva los meses al cuadrado (`meses ** 2`) en vez de multiplicar linealmente por el periodo, alterando el interés y el total final calculado.
| ID | Descripción | Precondición | Entrada | Esperado | Real | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CP-03 | Cálculo de intereses y cuota por socio | Script iniciado en terminal / listo para ingreso de datos | presupuesto total: 1000, socios: 2, meses: 2 | Intereses generados: $40.00, Total: $1040.00, Cuota: $520.00 | Intereses generados: $80.00, Total: $1080.00, Cuota: $540.00 en la línea 7 | Failed |



