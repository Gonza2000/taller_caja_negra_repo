from presupuesto_analisis import calcular_presupuesto


def test_calcular_presupuesto(monkeypatch):
    # Valores de entrada simulados: presupuesto=1000, socios=2, meses=2
    entradas = ["1000", "2", "2"]
    monkeypatch.setattr("builtins.input", lambda _: entradas.pop(0))

    # SABOTAJE (FALLO INTENCIONAL):
    # Afirmamos que la función devuelve "Cálculo exitoso", pero devuelve None.
    # Esto causa un AssertionError que hace fallar a PyTest y pone el pipeline en ROJO (FAIL).
    assert calcular_presupuesto() == "Cálculo exitoso"
