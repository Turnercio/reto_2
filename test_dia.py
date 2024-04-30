from Calendario import Dia
import pytest

def test_instanciar_dia_por_defecto():
    dia = Dia()
    assert dia.anyo == 1970
    assert dia.mes == 1
    assert dia.dia == 1

def test_instanciar_cumple_didier():
    dia = Dia(2024, 11, 28)
    assert dia.anyo == 2024
    assert dia.mes == 11
    assert dia.dia == 28

def test_mes_incorrecto():
    with pytest.raises(ValueError):
        dia= Dia(2024, 13, 1)

def test_dia_entre_1_y_31():
    with pytest.raises(ValueError):
        dia = Dia(2024, 12, 32)

def test_anyo_positivo():
    with pytest.raises(ValueError):
        dia = Dia(-2024, 12, 1)

def test_dia_incorrecto_meses_menos_de_31():
    with pytest.raises(ValueError):
        dia = Dia(2023,2,29)
    with pytest.raises(ValueError):
        dia = Dia(2024,4,31)
    with pytest.raises(ValueError):
        dia = Dia(2024,6,31)
    with pytest.raises(ValueError):
        dia = Dia(2024,9,31)
    with pytest.raises(ValueError):
        dia = Dia(2024,11,31)  
    
def test_dia_correcto_29_febrero_en_bisiesto():
    dia = Dia(2024, 2, 29)
    assert dia.dia == 29

def test_anyos_bisiesto():
    dia = Dia(2024, 1, 1)
    assert dia.es_bisiesto() == True

    dia = Dia(2022, 1, 1) 
    assert dia.es_bisiesto() == False

    dia = Dia(2000, 1, 1)
    assert dia.es_bisiesto() == True
    
    dia = Dia(1900, 1, 1)


def test_create_dia_con_tipos_incorrectos():
    with pytest.raises(ValueError) as excp:
        d = Dia("a", "b", "c")
        assert "Día" in str(excp.value)