## 1. Caso de Prueba 01


| ID | Descripción | Precondición | Entrada | Esperado | Real | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CP-01 | Comportamiento con 0 socios | Script iniciado en terminal / listo para ingreso de datos | presupuesto total: 100, socios: 0, meses: 10 | Mensaje de división no disponible, ejecución normal | pendiente | pendiente |

#### Ejecutar y Localizar el Bug
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
| ID | Descripción | Precondición | Entrada | Esperado | Real | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CP-01 | Comportamiento con 0 socios | Script iniciado en terminal / listo para ingreso de datos | presupuesto total: 100, socios: 0, meses: 10 | Mensaje de división no disponible, ejecución normal | ZeroDivisionError: float division by zero en la línea 9 | Failed |
##  2. Caso de Prueba 02
| ID | Descripción | Precondición | Entrada | Esperado | Real | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CP-02 | Cálculo de negocio| Script iniciado en terminal / listo para ingreso de datos | presupuesto total: 1000, socios:2, meses:2 | intereses: 40, total con intereses:1040, cuota por socio: 520 | pendiente | pendiente |
#### Ejecutar y Localizar el Bug
## 3. Caso de Prueba 03
| ID | Descripción | Precondición | Entrada | Esperado | Real | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CP-03 | No detectado | Script iniciado en terminal / listo para ingreso de datos | presupuesto total: 1000, socios:2, meses:2 | intereses: 40, total con intereses:1040, cuota por socio: 520 | pendiente | pendiente |
#### Ejecutar y Localizar el Bug




