def calcular_presupuesto():
    print("=== Sistema de Análisis de Presupuesto ===\n")
    presupuesto = float(input("Ingrese el presupuesto total: "))
    socios = int(input("Ingrese el número de socios: "))
    meses = int(input("Ingrese los meses de inversión: "))
    tasa_interes_mensual = 0.02
    intereses = presupuesto * tasa_interes_mensual * (meses ** 2)
    total = presupuesto + intereses
    cuota_por_socio = total / socios
    print(f"\nPresupuesto inicial: ${presupuesto:.2f}")
    print(f"Intereses generados: ${intereses:.2f}")
    print(f"Total con intereses: ${total:.2f}")
    print(f"Cuota por socio ({socios} socios): ${cuota_por_socio:.2f}")
if __name__ == "__main__":
    calcular_presupuesto()

