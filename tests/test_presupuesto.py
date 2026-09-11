import pytest
from presupuesto_analisis import calcular_presupuesto


def test_calculo_presupuesto_ejecucion(monkeypatch, capsys):
    """
    Prueba de ejecución del script original con valores estándar (1000, 2, 2).
    Verifica la salida generada en consola por la función calcular_presupuesto.
    """
    entradas = iter(["1000", "2", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    calcular_presupuesto()

    salida = capsys.readouterr().out
    assert "Presupuesto inicial: $1000.00" in salida
    assert "Intereses generados: $80.00" in salida
    assert "Total con intereses: $1080.00" in salida
    assert "Cuota por socio (2 socios): $540.00" in salida


def test_calculo_un_socio(monkeypatch, capsys):
    """
    Prueba de ejecución con 1 solo socio y 1 mes.
    Intereses: 5000 * 0.02 * (1 ** 2) = 100.00
    Total: 5100.00
    Cuota: 5100.00
    """
    entradas = iter(["5000", "1", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    calcular_presupuesto()

    salida = capsys.readouterr().out
    assert "Presupuesto inicial: $5000.00" in salida
    assert "Intereses generados: $100.00" in salida
    assert "Total con intereses: $5100.00" in salida
    assert "Cuota por socio (1 socios): $5100.00" in salida


def test_defecto_cp01_division_cero(monkeypatch):
    """
    CP-01: Demuestra el fallo de división por cero cuando socios = 0.
    El script original no valida socios <= 0 y detona ZeroDivisionError.
    """
    entradas = iter(["100", "0", "10"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    with pytest.raises(ZeroDivisionError):
        calcular_presupuesto()


def test_defecto_cp02_presupuesto_negativo(monkeypatch, capsys):
    """
    CP-02: Demuestra la falta de validación ante presupuesto negativo.
    El script original no bloquea entradas negativas y procesa -3.
    """
    entradas = iter(["-3", "23", "23"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    calcular_presupuesto()

    salida = capsys.readouterr().out
    assert "Presupuesto inicial: $-3.00" in salida
