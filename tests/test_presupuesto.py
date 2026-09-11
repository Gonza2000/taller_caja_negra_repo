from presupuesto_analisis import calcular_presupuesto


def test_caso_prueba_01(monkeypatch):
    # Caso de Prueba 01: presupuesto=100, socios=0, meses=10
    # Entrada con 0 socios (fallo intencional / sabotaje)
    entradas = ["100", "0", "10"]
    monkeypatch.setattr("builtins.input", lambda _: entradas.pop(0))

    # Al ingresar 0 socios, el código intenta dividir para cero (ZeroDivisionError)
    # provocando que PyTest falle y el pipeline de GitHub Actions se marque en ROJO (FAIL).
    assert calcular_presupuesto() is None
