from presupuesto_analisis import calcular_presupuesto


def test_calcular_presupuesto(monkeypatch):
    # Valores de entrada simulados: presupuesto=1000, socios=2, meses=2
    entradas = ["1000", "2", "2"]
    monkeypatch.setattr("builtins.input", lambda _: entradas.pop(0))

    # Verifica que la función se ejecute sin errores
    assert calcular_presupuesto() is None
