## Actividad 1 - Mapa conceptual
<img width="1805" height="1000" alt="Caja Negra MC" src="https://github.com/user-attachments/assets/817d5194-b01f-43d4-824d-e92c4abac651" />


## Actividad 3 y 4 - Casos de Prueba

## 1. Caso de Prueba 01
Probamos con la entrada de socios <= 0 como clase inválida y 0 como valor límite.

| ID | Descripción | Precondición | Entrada | Esperado | Real | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CP-01 | Comportamiento con 0 socios | Script iniciado en terminal / listo para ingreso de datos | presupuesto total: 100, socios: 0, meses: 10 | Mensaje de división no disponible / volver a intentar, ejecución normal. | ZeroDivisionError: float division by zero en la línea 9 | Failed |

#### Ejecutar y Localizar el Bug
Log de Consola:
```text
Traceback (most recent call last):
  File "presupuesto_analisis.py", line 15, in <module>
    calcular_presupuesto()
  File "presupuesto_analisis.py", line 9, in calcular_presupuesto
    cuota_por_socio = total / socios
ZeroDivisionError: float division by zero
```

#### Reporte del Defecto
El código nunca valida que `socios` sea mayor a 0 antes de realizar la división en la línea 9:
`cuota_por_socio = total / socios`

Este defecto es el que se utiliza como base para la prueba automatizada y el sabotaje intencional en GitHub Actions, verificando que una entrada de `socios = 0` detona el fallo del pipeline (color Rojo / FAIL).
