def calcular_metricas_presupuesto(presupuesto: float, socios: int, meses: int) -> dict:
    """
    Calcula los intereses, total y cuota por socio dado un presupuesto,
    número de socios y meses de inversión.
    
    Lanza ValueError si alguno de los valores viola las reglas de negocio:
    - presupuesto < 0
    - socios <= 0
    - meses <= 0
    """
    if presupuesto < 0:
        raise ValueError("El presupuesto no puede ser negativo.")
    if socios <= 0:
        raise ValueError("El número de socios debe ser mayor a cero.")
    if meses <= 0:
        raise ValueError("El número de meses debe ser mayor a cero.")

    tasa_interes_mensual = 0.02
    intereses = round(presupuesto * tasa_interes_mensual * meses, 2)
    total = round(presupuesto + intereses, 2)
    cuota_por_socio = round(total / socios, 2)

    return {
        "presupuesto": float(presupuesto),
        "intereses": intereses,
        "total": total,
        "cuota_por_socio": cuota_por_socio
    }


def calcular_presupuesto():
    print("=== Sistema de Análisis de Presupuesto ===\n")
    try:
        presupuesto = float(input("Ingrese el presupuesto total: "))
        socios = int(input("Ingrese el número de socios: "))
        meses = int(input("Ingrese los meses de inversión: "))

        resultado = calcular_metricas_presupuesto(presupuesto, socios, meses)

        print(f"\nPresupuesto inicial: ${resultado['presupuesto']:.2f}")
        print(f"Intereses generados: ${resultado['intereses']:.2f}")
        print(f"Total con intereses: ${resultado['total']:.2f}")
        print(f"Cuota por socio ({socios} socios): ${resultado['cuota_por_socio']:.2f}")
    except ValueError as e:
        print(f"\n[ERROR] Entrada inválida: {e}")


if __name__ == "__main__":
    calcular_presupuesto()

