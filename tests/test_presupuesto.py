import pytest
from presupuesto_analisis import calcular_presupuesto


def test_caso_feliz(monkeypatch, capsys):
    """
    Caso Feliz: Ejecución con valores válidos estándar.
    Entrada: presupuesto=1000, socios=2, meses=2.
    Verifica que el cálculo y la salida en consola sean correctos.
    """
    entradas = ["1000", "0", "2"]
    monkeypatch.setattr("builtins.input", lambda _: entradas.pop(0))

    calcular_presupuesto()

    salida = capsys.readouterr().out
    assert "Presupuesto inicial: $1000.00" in salida
    assert "Total con intereses: $1080.00" in salida
    assert "Cuota por socio (2 socios): $540.00" in salida


def test_caso_limite(monkeypatch, capsys):
    """
    Caso Límite: Inversión individual con 1 solo socio y 1 mes.
    Entrada: presupuesto=5000, socios=1, meses=1.
    Verifica el comportamiento en los límites inferiores válidos.
    """
    entradas = ["5000", "1", "1"]
    monkeypatch.setattr("builtins.input", lambda _: entradas.pop(0))

    calcular_presupuesto()

    salida = capsys.readouterr().out
    assert "Presupuesto inicial: $5000.00" in salida
    assert "Cuota por socio (1 socios): $5100.00" in salida


def test_division_por_cero(monkeypatch):
    """
    División por Cero (CP-01): Entrada inválida de 0 socios.
    Entrada: presupuesto=100, socios=0, meses=10.
    Verifica que el código detone ZeroDivisionError al no tener validación.
    """
    entradas = ["100", "0", "10"]
    monkeypatch.setattr("builtins.input", lambda _: entradas.pop(0))

    with pytest.raises(ZeroDivisionError):
        calcular_presupuesto()


def test_inputs_negativos(monkeypatch, capsys):
    """
    Inputs Negativos (CP-02): Entrada inválida con presupuesto negativo.
    Entrada: presupuesto=-3, socios=23, meses=23.
    Verifica que el programa no bloquee números negativos y procese $-3.00.
    """
    entradas = ["-3", "23", "23"]
    monkeypatch.setattr("builtins.input", lambda _: entradas.pop(0))

    calcular_presupuesto()

    salida = capsys.readouterr().out
    assert "Presupuesto inicial: $-3.00" in salida
