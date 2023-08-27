from src.Ac01Exercicios import Ac01Exercicios
import pytest


def test_calculo_salario_liquido():
    assert Ac01Exercicios.calcular_salario_liquido(6.25, 160, 1.3) == 987.00
    assert Ac01Exercicios.calcular_salario_liquido(20.5, 240, 1.7) == 4836.36
    assert Ac01Exercicios.calcular_salario_liquido(13.9, 200, 6.48) == 2599.86

def test_calculo_valor_com_desconto():
    assert Ac01Exercicios.calcular_valor_com_desconto(100) == 91.00
    assert Ac01Exercicios.calcular_valor_com_desconto(1500) == 1365.00
    assert Ac01Exercicios.calcular_valor_com_desconto(60000) == 54600.00

def test_calculo_valor_promocao():
    assert Ac01Exercicios.calcular_valor_promocao(500.00, 50.00) == 450.00
    assert Ac01Exercicios.calcular_valor_promocao(10500.00, 500.00) == 10000.00
    assert Ac01Exercicios.calcular_valor_promocao(90.00, 0.80) == 89.20

def test_calculo_conta_e_gorjeta():
    assert Ac01Exercicios.calcular_conta_e_gorjeta(75.00) == (82.50, 7.5)
    assert Ac01Exercicios.calcular_conta_e_gorjeta(125.00) == (137.50, 12.5)
    assert Ac01Exercicios.calcular_conta_e_gorjeta(350.87) == (385.96, 35.09)