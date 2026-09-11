import pytest
from presupuesto_analisis import calcular_metricas_presupuesto


def test_calculo_exitoso_cp03():
    """
    CP-03: Cálculo de intereses y cuota por socio con valores válidos.
    Entrada: presupuesto=1000, socios=2, meses=2
    Esperado:
      - Intereses generados: $40.00 (tasa 2% mensual lineal: 1000 * 0.02 * 2)
      - Total con intereses: $1040.00
      - Cuota por socio: $520.00
    """
    resultado = calcular_metricas_presupuesto(presupuesto=1000, socios=2, meses=2)
    assert resultado["presupuesto"] == 1000.0
    assert resultado["intereses"] == 40.00
    assert resultado["total"] == 1040.00
    assert resultado["cuota_por_socio"] == 520.00


def test_socios_cero_invalido_cp01():
    """
    CP-01: Validación de límite/invalidez con socios = 0.
    Previene ZeroDivisionError lanzando ValueError controlado.
    Entrada: presupuesto=100, socios=0, meses=10
    """
    with pytest.raises(ValueError, match="número de socios debe ser mayor a cero"):
        calcular_metricas_presupuesto(presupuesto=100, socios=0, meses=10)


def test_presupuesto_negativo_invalido_cp02():
    """
    CP-02: Validación de clase de equivalencia inválida (presupuesto < 0).
    Previene cálculos incoherentes lanzando ValueError controlado.
    Entrada: presupuesto=-3, socios=23, meses=23
    """
    with pytest.raises(ValueError, match="El presupuesto no puede ser negativo"):
        calcular_metricas_presupuesto(presupuesto=-3, socios=23, meses=23)


def test_meses_invalido_cero_o_negativo():
    """
    Validación de regla de negocio: la inversión debe durar al menos 1 mes.
    """
    with pytest.raises(ValueError, match="número de meses debe ser mayor a cero"):
        calcular_metricas_presupuesto(presupuesto=500, socios=2, meses=0)

    with pytest.raises(ValueError, match="número de meses debe ser mayor a cero"):
        calcular_metricas_presupuesto(presupuesto=500, socios=2, meses=-5)


def test_caso_borde_un_socio():
    """
    Caso de borde: Inversión individual (1 socio) durante 12 meses.
    Entrada: presupuesto=5000, socios=1, meses=12
    Intereses: 5000 * 0.02 * 12 = 1200.00
    Total: 6200.00
    Cuota por socio: 6200.00
    """
    resultado = calcular_metricas_presupuesto(presupuesto=5000, socios=1, meses=12)
    assert resultado["intereses"] == 1200.00
    assert resultado["total"] == 6200.00
    assert resultado["cuota_por_socio"] == 6200.00


def test_presupuesto_cero_limite_valido():
    """
    Caso límite válido: presupuesto inicial de 0.
    """
    resultado = calcular_metricas_presupuesto(presupuesto=0, socios=4, meses=6)
    assert resultado["presupuesto"] == 0.0
    assert resultado["intereses"] == 0.0
    assert resultado["total"] == 0.0
    assert resultado["cuota_por_socio"] == 0.0
